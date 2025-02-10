# Llama-Index QnA Bot

## Overview
Llama-Index QnA Bot is a Flask-based application that allows users to ask questions based on uploaded documents. Using LlamaIndex and OpenAI's API, the bot extracts relevant answers from stored materials in the `data` folder. Supported document formats include `.txt` and `.pdf`.

## Requirements

Ensure you have the following installed:

1. Python (latest stable version recommended)
2. Flask - Web framework for the application
3. OpenAI API Key - Required for generating responses
4. LlamaIndex - For indexing and querying documents

## Getting Started

To get started using this application, please follow the steps below:

1. Install Python on your computer.
2. Navigate to the directory where you have cloned this repository.
3. Run the command `pip install -r requirements.txt` to install the necessary Python packages.
4. To use OpenAI’s models, you need to set up an API key.
    * macOS / Linux   `export OPENAI_API_KEY=your_api_key_here`
    * Windows     `set OPENAI_API_KEY=your_api_key_here`
5. Run the command `python app.py` to start the application.
6. Access the web interface:
    * Open index.html in your browser.
    * Enter your question, and the bot will retrieve answers from the uploaded documents using LlamaIndex.

## Features

Once the application is running, you can use it to generate text based on a prompt that you provide. Simply enter a prompt, and the application will use OpenAI's API to generate a response.

Additionally, the application supports document-based Q&A (Retrieval-Augmented Generation - RAG), allowing users to upload .txt and .pdf files for intelligent responses. It leverages OpenAI's language models to provide accurate and context-aware answers.

The user-friendly web-based UI ensures easy interaction, making the experience seamless and efficient.

## References

[LlamaIndex introduction](https://docs.llamaindex.ai/en/stable/#introduction)

[Starter Tutorial (OpenAI) LlamaIndex](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)

<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/9eb95803-9fcf-48b3-8c61-9fd0df08f427" />
