# 🔍 MATCH: Mission Alignment and Talent Candidate Hub

## Overview
Welcome to 🔍 MATCH, an AI-powered application designed to match consultant resumes with suitable missions. Leveraging OpenAI's GPT-4, this tool provides a seamless way to analyze resumes, match skills and experiences, and offer intelligent insights to consulting sales representatives.

## Features

- **AI-Powered Insights**: Utilizes GPT-4 with the latest assistant features for deep contextual understanding and response generation.
- **Efficient Matching**: Leverages a retrieval augmented generation (RAG) model to find the best matches between consultants and missions.
- **Streamlit Interface**: Provides an easy-to-use, conversational UI where users can input requirements and interact with the AI.
- **Document Retrieval**: Integrates a vector store for efficient searching through a large number of documents, enabling quick retrieval of relevant resume details.

## Components

- **cv_assistant.py**: Main application file with Streamlit interface, managing user interactions and state.
- **common.py**: Contains utility functions and classes for AWS interactions, file operations, and event handling.
- **personal_assistant.py**: Handles communication with the OpenAI API, including managing conversations and vector stores.


## Getting Started

### Prerequisites

- Python 3.10 or higher
- Streamlit
- OpenAI Python client
- AWS CLI configured with appropriate permissions

### Installation

1. Clone the repository:
`git clone https://github.com/Silv3rcrowss/MATCH.git`

2. Navigate to the project directory:
`cd MATCH`

3. Install the required Python packages:
`pip install -r requirements.txt`


### Running the Application

To run the application, execute the following command in your terminal:

`streamlit run cv_assistant.py`

This will start the Streamlit server, and you can access the application by navigating to the provided URL in your web browser.

## Configuration
- Please adjust paths, dependency versions, and personal information as necessary to fit your project specifics and organizational guidelines.
- Ensure your AWS credentials are configured to use services such as Secret Manager for credential retrieval, or set up environment variables for OpenAI API keys for seamless integration.

## Usage

### Step 1: Open the 🔍 MATCH Application
Access the 🔍 MATCH application through your preferred web browser. Since it is a proof of concept, there is no login required at this stage.

### Step 2: Engage with the MATCH Assistant
Interact with the MATCH assistant directly through the natural language input field located on the main page. Simply type your query or instruction related to the consultant profiles or mission details and press 'Enter' or click the 'Send' button.

### Step 3: Query Specific Details or Actions
You can perform specific queries such as "Tell me more about [Consultant's Name]" or "Find candidates for [specific mission requirements]". The assistant utilizes a retrieval-augmented generation model to analyze the embedded resume knowledge base and provide relevant information.

### Step 4: Review Responses and Further Interact
After submitting your query, the assistant will process the input and display a detailed response. You can continue the conversation by asking more specific questions or requesting further details about a candidate or a mission. Each interaction is designed to refine the results and assist you in making the best decisions.

### Step 5: Detailed Examination and Conversation
Leverage the conversational interface to inquire further about each candidate. The system, using a light RAG (retrieval augmented generation) implementation of a GPT-assistant, can pull detailed insights and contextual information from the integrated knowledge base.

### Step 6: Extend and Customize
While primarily designed for resume and mission matching, 🔍 MATCH also supports creating new GPT-assistant instances for various purposes. Utilize the provided codebase to adapt the assistant for different datasets or directives, enhancing its utility across different contexts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.