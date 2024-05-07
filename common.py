import json
import boto3
from botocore.exceptions import ClientError

import os

from typing_extensions import override
import streamlit as st
from openai import AssistantEventHandler
from openai.types.beta.threads import Text, TextDelta


def get_secret(secret_name, region_name) -> dict[str, str] | None:
    """
    Retrieves a secret from AWS Secrets Manager
    :param secret_name: The name of the secret
    :param region_name: The AWS region where the secret is stored
    :return: The secret as a dictionary
    """
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name,
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as error:
        print(f"Error retrieving secret: {error}")
        return None

    return json.loads(response["SecretString"])


def get_parameter(parameter_name, region_name) -> dict[str, str] | None:
    """
    Retrieves a parameter  from AWS Systems Manager
    :param parameter_name: The name of the secret
    :param region_name: The AWS region where the secret is stored
    :return: The parameter as a dictionary
    """
    session = boto3.session.Session()
    client = session.client(
        service_name="ssm",
        region_name=region_name,
    )

    try:
        response = client.get_parameter(
            Name=parameter_name, WithDecryption=True
        )
    except ClientError as error:
        print(f"Error retrieving parameter: {error}")
        return None
    return response["Parameter"]["Value"]


def retrieve_file_list_from_folder(folder_path: str) -> list[str]:
    """retrieves list on files in a given folder"""
    file_list = []
    for file in os.listdir(path=folder_path):
        file_list.append(f"{folder_path}/{file}")
    print(file_list)
    return file_list


# This class is a custom event handler for the assistant stream, it defines custom behaviors for each event sent by openai.
# e.g. when a new text is created, it creates a new text box and displays the text in it.
# reference :https://platform.openai.com/docs/assistants/overview/step-4-create-a-run
class EventHandler(AssistantEventHandler):
    """
    Event handler for the assistant stream
    """

    @override
    def on_text_created(self, text: Text) -> None:
        """
        Handler for when a text is created
        """
        try:
            st.session_state[
                f"code_expander_{len(st.session_state.text_boxes) - 1}"
            ].update(state="complete", expanded=False)
        except KeyError:
            pass

        # Create a new text box
        st.session_state.text_boxes.append(st.empty())
        # Insert the text into the last element in assistant text list
        st.session_state.assistant_text[-1] += "**> 🔍 MATCH:** \n\n "
        # Display the text in the newly created text box
        st.session_state.text_boxes[-1].info(
            "".join(st.session_state["assistant_text"][-1])
        )

    @override
    def on_text_delta(self, delta: TextDelta, snapshot: Text):
        """
        Handler for when a text delta is created
        """
        # Clear the latest text box
        st.session_state.text_boxes[-1].empty()
        # If there is text written, add it to latest element in the assistant text list
        if delta.value:
            st.session_state.assistant_text[-1] += delta.value
        # Re-display the full text in the latest text box
        st.session_state.text_boxes[-1].info(
            "".join(st.session_state["assistant_text"][-1])
        )

    def on_text_done(self, text: Text):
        """
        Handler for when text is done
        """
        # Create new text box and element in the assistant text list
        st.session_state.text_boxes.append(st.empty())
        st.session_state.assistant_text.append("")

    def on_timeout(self):
        """
        Handler for when the api call times out
        """
        st.error("The api call timed out.")
        st.stop()
