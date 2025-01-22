![[GIF demo of the chatbot]](demo.gif)

# Gemini-based Chatbot with Streamlit

Welcome to the **Gemini-based Chatbot** built using **Streamlit** and the **Google Generative AI** API. This project allows you to interact with an AI model that generates text responses based on user input. 

Follow the steps below to set up and run this application.

## Prerequisites

Before running the application, make sure you have the following installed:
- **Python 3.8+** (recommended)
- **Pip** (for managing Python packages)

## Setup Instructions

### 1. Clone the repository

First, clone this repository to your local machine:

```
git clone <repository-url>
cd <repository-folder>
```
### 2. Install dependencies
Once you've cloned the repository, navigate to the project folder and install the required dependencies by running:

```
pip install -r requirements.txt
```
### 3. Set up your .env file
You will need a Gemini API key to interact with the Gemini model. Follow these steps to set it up:

1. Create a .env file in the root of the project directory.
2. 2. Add the following line to your .env file:
```
GEMINI_API_KEY="your_api_key_here"
```
Note: If you don't have a Gemini API key, Get one from [Google AI Studio](https://aistudio.google.com/apikey).

I've included a ```.env_template``` file in the repository for reference. You can copy its contents into your ```.env``` file and replace "your_api_key_here" with your actual Gemini API key.

### 4. Running the Streamlit App
After setting up the ```.env``` file with your API key, you can run the Streamlit app by executing the following command:

```
streamlit run app.py
```
The app will start, and a new tab will open in your browser displaying the chatbot interface.
