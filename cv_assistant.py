from personal_assitant import Conversation
from common import EventHandler
import streamlit as st

ROLE_AVATARS = {
    "user": "🤔",
    "assistant": "🔍",
}

ROLES_PREFIX = {
    "user": "**> User**",
    "assistant": "**> MATCH**",
}


def display_message_history(message_history):

    for message in message_history:
        with st.chat_message(
            message.role, avatar=st.session_state.ROLE_AVATARS[message.role]
        ):
            st.markdown(
                f"{ROLES_PREFIX[message.role]} :"
                f" {message.content[0].text.value}"
            )


st.set_page_config(
    page_title="Resume Assistant", page_icon=ROLE_AVATARS["assistant"]
)

st.title("Resume Assistant")
st.subheader(
    f"{ROLE_AVATARS['assistant']} MATCH: Mission Alignment and Talent"
    " Candidate Hub"
)

if "conversation" not in st.session_state:
    st.session_state.conversation = Conversation(
        credential_name="my_secret",
        region_name="region",
    )


if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = False

if "assistant_text" not in st.session_state:
    st.session_state.assistant_text = [""]

if "code_input" not in st.session_state:
    st.session_state.code_input = []

if "code_output" not in st.session_state:
    st.session_state.code_output = []

if "disabled" not in st.session_state:
    st.session_state.disabled = False

if "text_boxes" not in st.session_state:
    st.session_state.text_boxes = []


display_message_history(
    message_history=st.session_state.conversation.retrieve_messages_from_thread()
)

if prompt := st.chat_input(placeholder="Comment puis-je vous aider ?"):

    st.session_state.conversation.create_message(prompt)
    st.session_state.text_boxes.append(st.empty())
    st.session_state.text_boxes[-1].success(
        f"**> {ROLE_AVATARS['user']} User:** {prompt}"
    )

    with st.session_state.conversation.client.beta.threads.runs.stream(
        thread_id=st.session_state.conversation.thread.id,
        assistant_id=st.session_state.conversation.assistant_id,
        event_handler=EventHandler(),
    ) as stream:
        stream.until_done()
        st.toast("Response complete", icon="👌")
