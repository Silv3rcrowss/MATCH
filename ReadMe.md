# 🔍 MATCH: Mission Alignment and Talent Candidate Hub

## Overview

🔍 MATCH is an AI application designed to serve as a copilot for analyzing consultant resumes. It aims to match the skills, experiences, and interests of consultants with the missions that best align with them. Leveraging the power of the OpenAI API, 🔍 MATCH provides intelligent insights and suggestions to help consulting sales representative navigate their client interactions more effectively and efficiently.
By streamlining the process of resume analysis, 🔍 MATCH ensures that consultants are paired with projects that not only suit their skill set but also enhance their career growth. This alignment leads to higher job satisfaction and better outcomes for both consultants and clients. Additionally, the application features a user-friendly interface that makes accessing and interpreting data straightforward for consulting sales representatives. 
Whether dealing with large volumes of resumes or searching for the ideal candidate for a niche mission, 🔍 MATCH optimizes the selection process, enabling sales representatives to focus more on building relationships and closing deals.

## Project Structure

The 🔍 MATCH project is structured into three core components:

1. **cv_assistant.py**: This is the heart of the application, where the Streamlit interface is set up. It handles user interactions, displays the conversation history, and manages the application's state using Streamlit's session state.

2. **common.py**: Contains utility functions and classes that are utilized across the application. This includes AWS service interactions, file operations, and a custom event handler for the assistant stream.

3. **personal_assitant.py**: Manages the interaction with the OpenAI API. It includes classes for creating and managing conversations, as well as for managing assistants and vector stores.

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

### Step 6: Making a Decision
Select the most appropriate consultant for the mission based on the detailed analysis provided. The interface allows you to note decisions and rationale for future reference.

### Step 7: Extend and Customize
While primarily designed for resume and mission matching, 🔍 MATCH also supports creating new GPT-assistant instances for various purposes. Utilize the provided codebase to adapt the assistant for different datasets or directives, enhancing its utility across different contexts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
