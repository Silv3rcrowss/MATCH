# 🔍 MATCH: Mission Alignment and Talent Candidate Hub

## Overview

🔍 MATCH is an application designed to serve as a copilot for analyzing consultant resumes. It aims to match the skills, experiences, and interests of consultants with the missions that best align with them. Leveraging the power of the OpenAI API, 🔍 MATCH provides intelligent insights and suggestions to help consulting sales representative navigate their client interactions more effectively and efficiently.
By streamlining the process of resume analysis, 🔍 MATCH ensures that consultants are paired with projects that not only suit their skill set but also enhance their career growth. This alignment leads to higher job satisfaction and better outcomes for both consultants and clients. Additionally, the application features a user-friendly interface that makes accessing and interpreting data straightforward for consulting sales representatives. 
Whether dealing with large volumes of resumes or searching for the ideal candidate for a niche mission, 🔍 MATCH optimizes the selection process, enabling sales representatives to focus more on building relationships and closing deals.

## Project Structure

The 🔍 MATCH project is structured into three core components:

1. **cv_assistant.py**: This is the heart of the application, where the Streamlit interface is set up. It handles user interactions, displays the conversation history, and manages the application's state using Streamlit's session state.

2. **common.py**: Contains utility functions and classes that are utilized across the application. This includes AWS service interactions, file operations, and a custom event handler for the assistant stream.

3. **personal_assitant.py**: Manages the interaction with the OpenAI API. It includes classes for creating and managing conversations, as well as for managing assistants and vector stores.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- OpenAI Python client
- AWS CLI configured with appropriate permissions

### Installation

1. Clone the repository:
git clone https://github.com/your-repo/match-mission-alignment.git

2. Navigate to the project directory:
cd match-mission-alignment

3. Install the required Python packages:
pip install -r requirements.txt


### Running the Application

To run the application, execute the following command in your terminal:

streamlit run cv_assistant.py


This will start the Streamlit server, and you can access the application by navigating to the provided URL in your web browser.

## Usage

# Step 1: Open the 🔍 MATCH Application
Access the 🔍 MATCH application through your preferred web browser. Since it is a proof of concept, there is no login required at this stage.

# Step 2: Entering Mission Requirements
Navigate to the "Mission Requirements" section to input specific details about the mission you are staffing. Here, you can enter skills, required experiences, preferred certifications, and other relevant details for the mission.

# Step 3: Initiate the Matching Process
Click on "Match Candidates" to start the analysis. 🔍 MATCH, already pre-loaded with a comprehensive resume database, utilizes AI-driven algorithms to identify the best candidates for the specified mission requirements.

# Step 4: Review Matched Candidates
The application will display a list of candidates who best match the mission criteria. For each candidate, you will see details such as their current role, specialized skills, relevant experiences, and certifications.

# Step 5: Detailed Examination and Conversation
Leverage the conversational interface to inquire further about each candidate. The system, using a light RAG (retrieval augmented generation) implementation of a GPT-assistant, can pull detailed insights and contextual information from the integrated knowledge base.

# Step 6: Making a Decision
Select the most appropriate consultant for the mission based on the detailed analysis provided. The interface allows you to note decisions and rationale for future reference.

# Step 7: Extend and Customize
🔍 MATCH is not only designed for analyzing resumes but also serves as a platform for creating new GPT-assistant instances with different directives. The included codebase allows you to provide any files as a knowledge base and tailor the assistant to meet specific needs.
## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any questions or support, please contact the project maintainers at [your-email@example.com](mailto:your-email@example.com).