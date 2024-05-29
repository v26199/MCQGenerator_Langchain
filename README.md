# Automated MCQ Generator Using Langchain OpenAI API

## Description

This project utilizes Langchain's OpenAI API, specifically the GPT-3 model, to automatically generate multiple-choice questions (MCQs) from given text inputs. The application is built using Streamlit, providing an intuitive and interactive platform for users to input text and receive generated MCQs. Additionally, the project includes a command-line interface for testing and experimentation.

---
## Features

- Automatic generation of MCQs from text inputs using Langchain's OpenAI API.
- User-friendly interface designed with Streamlit for seamless interaction.
- Command-line interface for testing and experimentation.
- Easy deployment and scalability.

---
## Setup Instructions
#### 1. Clone the repository to your local machine.
https://github.com/v26199/MCQGenerator_Langchain.git

#### 2. Install the required dependencies.
pip install -r requirements.txt

#### 3. Obtain API keys for Langchain's OpenAI API and configure them in the application.
NOTE:- Add your OpenAI API key to the .env file
OPENAI_API_KEY=your_api_key_here

#### 4. Run the Streamlit application.
streamlit run StreamlitAPP.py

---
#### 5. Access the application in your web browser at `http://localhost:8501`.
## Project Structure

- **StreamlitAPP.py**: Main application file containing the user interface logic using Streamlit.
- **test.py**: Command-line interface for testing and experimentation.
- **requirements.txt**: File containing the list of dependencies required for the project.
- **README.md**: This file provides an overview of the project, setup instructions, and project structure.
- **.env**: Configuration file for storing sensitive information such as API keys. Ensure to keep this file secure and do not commit it to version control.
- **data.txt**: Sample text data for testing and experimentation.
- **Response.json**: Sample response JSON file.
- **src**: Directory containing source code files.
- **experiment**: Directory for experimentation and testing.
- **Logs**: Directory for storing application logs.
- **mcqgenerator.egg-info**: Metadata information for the Python package.
- **setup.py**: Setup script for installing the Python package.


## Contribution Guidelines

Contributions to the project are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request. Please ensure adherence to the project's coding standards and guidelines.

**Enjoy generating MCQs effortlessly with Langchain's OpenAI API and Streamlit!**



