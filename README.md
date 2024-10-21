# Chatbot 
This chatbot is designed to engage in conversations, provide answers to questions about the weather, and recognize when to conclude the interaction.


## Features

- **LLM-Powered Chatbot**: A chatbot that uses a Language Learning Model (LLM) to have conversations.

- **Weather Questions**: Can answer simple questions about the weather, giving you helpful information.

- **Conversation Exit**: Knows when to wrap up the conversation, making it a smooth experience for users.


## Setup
### Step-by-step Guide
1. Clone the repository:
    ```bash
    git clone https://github.com/Wonderofyou/Chatbot_app.git
    ```
2. Navigate into the directory:
    ```bash
    cd Chatbot_app
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Visit the following websites to obtain your API keys:
   - [Groq](https://groq.com/) for the Groq API key.
   - [Visual Crossing](https://www.visualcrossing.com/account) for the Visual Crossing weather API key.

5. Open the `.env` file located in the project directory, and update the environment variables with your API keys:

   ```plaintext
   VISUAL_CROSSING_API = 'your_api_key_on_VC'
   GROQ_API_KEY = 'your_api_key_on_groq'

6. To run the chatbot:
   - **CMD Mode**: Open a terminal and run the following command:
     ```bash
     python Chat.py CMD
     ```

   - **UI Mode**: To run the chatbot with a graphical interface, use:
     ```bash
     python Chat.py UI
     ```
## Prompt 
The Prompt is vital, If the prompt is not good enough, the LLM may unnecessarily invoke tools even when it could answer the question on its own.

## Framework

### LangChain

- **Modularity**: LangChain allows for the customization of prompt templates, LLMs, and tools. Additionally, it has extensive documentation and a large community for support.

- **Tool Integration**: LangChain supports various tools, and developers can customize these tools to fit their needs.

- **Agent Support**: LangChain provides agent support that handles tool logic, enabling the LLM to effectively utilize external tools.

### LLM: Groq

- **Speed**: Groq offers very fast response times, making it suitable for chatbot applications.

- **API Access**: Groq allows seamless access to powerful models like `llama3-70b-8192`, which is an advanced LLM from Meta. The `llama3-70b` model is robust enough to accurately decide whether to use tools or not. Initially, I used the `llama3-8b` model, which was unstable and did not make accurate decisions regarding tool usage.

### Tool: Visual Crossing

- **Weather API**: Visual Crossing provides an API that can fetch historical weather data, allowing the chatbot to access weather information.

### Tkinter: 
- Tkinter is used for a simple Chatbot UI.
## Future Developments

Looking ahead, there are several enhancements planned for the chatbot:

- **Chat History Management**: Implementing a more efficient system for storing and managing chat history will enhance the user experience and allow for better continuity in conversations.

- **User Interface Improvements**: Upgrading the user interface to make it more intuitive and visually appealing will improve user engagement and satisfaction.

- **Tool Enhancements**: Further developing and refining the existing tools will increase the chatbot's capabilities and improve its responsiveness and accuracy in providing information.




