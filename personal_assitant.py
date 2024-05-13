import logging
import sys
from openai import OpenAI
from common import get_secret, retrieve_file_list_from_folder
from typing import Any

logging.basicConfig(level=logging.INFO)


class Conversation:
    """
    A class to manage a conversation with the OpenAI API
    """

    client: OpenAI
    assistant_id: str
    thread: Any = None
    messages: list[dict[str, str | list | None]] = []

    def __init__(
        self,
        credential_name: str,
        region_name: str = "eu-west-1",
    ):
        """
        Initialize the conversation with the OpenAI API

        Args:
        - credential_name (str): The name of the secret containing the API credentials
        - region_name (str): The name of the AWS region
        """
        assistant_secrets = get_secret(
            secret_name=credential_name, region_name=region_name
        )
        self.client = OpenAI(
            organization=assistant_secrets["Organization"],
            api_key=assistant_secrets["Api_Key"],
            project=assistant_secrets["Project_ID"],
        )
        self.assistant_id = assistant_secrets["Assistant_ID"]
        self._create_thread()

    def _create_thread(self):
        """
        Create a new thread
        """
        if self.thread:
            return
        try:
            self.thread = self.client.beta.threads.create()
        except Exception as e:
            logging.error(
                msg=(
                    "Error in method"
                    f" {self.__class__.__name__}.{sys._getframe().f_code.co_name}:"
                    f" {e}\nFailed to create a new thread"
                )
            )
            raise

    def create_message(self, message: str):
        """
        Creates a new message in the thread

        Args:
        - message (str): The message to be sent
        """
        try:
            self.client.beta.threads.messages.create(
                thread_id=self.thread.id, role="user", content=f"{message}"
            )
        except Exception as e:
            logging.error(msg=f"Error creating message: {e}")
            raise

    def retrieve_messages_from_thread(
        self,
    ) -> list[dict[str, str | list | None]]:
        """
        Retrieves and returns the list of messages from the thread

        Returns:
        - list[str]: List of assistant messages
        """
        if not self.thread:
            return []
        # Retrieve messages from the thread in ascending order
        self.messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id, order="asc"
        ).data
        return self.messages

    def reset_conversation(self):
        self.thread = None
        self.messages.clear()


class AssistantManagement:
    """
    A class to manage assistant and vector store creation
    """

    client: OpenAI
    assistant_id: str
    vector_store: Any = None

    def __init__(
        self,
        credential_name: str,
        region_name: str = "eu-west-1",
    ):
        """
        Initialize the conversation with the OpenAI API

        Args:
        - credential_name (str): The name of the secret containing the API credentials
        - region_name (str): The name of the AWS region
        """
        assistant_secrets = get_secret(
            secret_name=credential_name, region_name=region_name
        )
        self.client = OpenAI(
            organization=assistant_secrets["Organization"],
            api_key=assistant_secrets["Api_Key"],
            project=assistant_secrets["Project_ID"],
        )

    def _create_new_vector_store(
        self, folder_path: str, vector_store_name: str
    ) -> str:
        """
        Create a new vector store from a folder of files

        Args:
        - folder_path (str): The path to the folder containing the files
        - vector_store_name (str): The name of the vector store

        Returns:
        - str: The ID of the created vector store
        """
        # Create a new vector store
        self.vector_store = self.client.beta.vector_stores.create(
            name=vector_store_name
        )
        logging.info(
            msg=(
                "Vector store created successfully.\nVector store ID :"
                f" {self.vector_store.id}"
            )
        )

        file_paths = retrieve_file_list_from_folder(folder_path=folder_path)
        try:
            # Load profided the files into a list of file streams
            file_streams = [open(file=path, mode="rb") for path in file_paths]

            # Upload the files to the vector store
            file_batch = (
                self.client.beta.vector_stores.file_batches.upload_and_poll(
                    vector_store_id=self.vector_store.id, files=file_streams
                )
            )

            logging.info(f"File upload status: {file_batch.status}")

            # We check if all files were uploaded successfully
            if file_batch.file_counts.completed != len(file_paths):
                logging.warning(
                    msg=(
                        "Some files could not be uploaded. File count:"
                        f" {file_batch.file_counts}"
                    )
                )
                # raise Exception("File upload failed")
            else:
                logging.info("All files uploaded successfully")

        finally:
            # Ensure all file streams are closed properly
            for file in file_streams:
                file.close()
        return self.vector_store.id

    def create_new_assistant(
        self,
        assistant_name: str,
        system_prompt: str,
        vector_store_name: str,
        vector_store_content_path: str | None = None,
    ) -> str:
        """
        Create a new assistant with the given name and system prompt

        Args:
        - assistant_name (str): The name of the assistant
        - system_prompt (str): The system prompt for the assistant
        - vector_store_name (str): The name for the new vector store
        - vector_store_content_path (str | None): The path to the folder containing the files to be indexed in the vector store

        Returns:
        - str: The ID of the created assistant
        """
        # Create a new assistant with the given name and system prompt
        # Create a new vector store if vector_store_content_path is provided
        assistant = self.client.beta.assistants.create(
            name=assistant_name,
            instructions=system_prompt,
            model="gpt-4-turbo",
            tools=[{"type": "file_search"}],
            tool_resources=(
                {
                    "file_search": {
                        "vector_store_ids": [
                            self._create_new_vector_store(
                                folder_path=vector_store_content_path,
                                vector_store_name=vector_store_name,
                            )
                        ]
                    }
                }
                if vector_store_content_path
                else {}
            ),
        )
        self.assistant_id = assistant.id
        logging.info(msg=f"Assistant created: {self.assistant_id}")
        return self.assistant_id
