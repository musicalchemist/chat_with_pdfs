# PDF Chatbot

## Description

PDF Chatbot is a Streamlit-based interactive web application that allows users to extract and chat with the content in their uploaded PDF documents. The chatbot leverages LLMs, Langchain, and NLP tools and algorithms to understand and answer user queries related to the content of the PDF documents.

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.10 or later.
- You have installed pip, the Python package installer.
- You have a Mac/Linux/Windows machine with a stable internet connection.

### Installing PDF Chatbot

To install PDF Chatbot, follow these steps:

1. Clone the repository:
   `git clone https://github.com/musicalchemist/chat_with_pdfs.git`

2. Navigate to the project directory:
   `cd chat_with_pdfs`

3. Install the required packages:
   `pip install -r requirements.txt`

### Obtain OpenAI API Key

PDF Chatbot uses OpenAI's language model to understand and generate responses. In order to use this service, you will need an API key from OpenAI.

To obtain the API key, follow these steps:

1. Navigate to [OpenAI's platform](https://platform.openai.com/signup).

2. Sign up for a new account if you don't have one or log in.

3. After logging in, navigate to the API section.

4. Here you should be able to generate a new API key.

Once you have obtained the API key, you need to store it in a `.env` file in your project's src directory (same directory as `app.py`).

The `.env` file should look like this:
`OPENAI_API_KEY='your-api-key'`

Replace `'your-api-key'` with the actual API key you obtained from OpenAI.

> :warning: **IMPORTANT**: Make sure to add `.env` to your `.gitignore` file to prevent it from being committed to your repository, as it contains sensitive information.

## Usage

After installation, you can start using PDF Chatbot by following these steps:

1. Navigate to the source directory:
   `cd src`

2. Run the Streamlit app:
   `streamlit run app.py`

3. Open a web browser and navigate to the address provided in the console. The default address is typically `http://localhost:8501`.
