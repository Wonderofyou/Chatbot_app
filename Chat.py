from langchain.agents import AgentExecutor, create_tool_calling_agent
from WeatherTool import historical_weather_tool_vc
import tkinter as tk
from tkinter import scrolledtext, messagebox
from Model import model
from Prompt_config import prompt, prompt_checking_exit
import sys


#tools for model 
tools = [historical_weather_tool_vc]

#construct the Tools agent (combine model and tool)
agent = create_tool_calling_agent(model, tools, prompt)

#create agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)



#using llm to extract name from user
def extract_name_from_input(input_text):

    prompt = f"""Extract the person's name from the following sentence: "{input_text}". 
    ONLY response the name."""
    response = model.invoke(prompt)
    
    return response.content

#CMD mode (chat bot run on cmd)
def chatbot():
    chat_history = []
    print("Bot: What's your name?")
    
    # Get the user's name and store it
    name = input("User: ")
    name = extract_name_from_input(name)
    print(f"Bot: Nice to meet you, {name}!")
    chat_history.append(f"name:{name}")
    while True:
        question = input(f"{name}: ")  # Personalize the prompt with the user's name
        
        if question.lower() == "exit":
            print(f"Bot: Goodbye!")
            break
        formatted_prompt = prompt_checking_exit.format(chat_history=chat_history, input=question)
        response = model.invoke(formatted_prompt)
        if response.content == "YES":
            print(f"Bot: Goodbye! {name}")
            break
        # Insert the question into the chat history
        chat_history.append({"role": "human", "content": f"{name}: {question}"})
        
        # Use the agent to generate a response
        ai_msg = agent_executor.invoke({"input": question, "chat_history": chat_history})
        
        # Add the assistant's response to chat history
        chat_history.append({"role": "assistant", "content": ai_msg["output"]})
        
        # Print the assistant's response
        print(f"Bot: {ai_msg["output"]}")


#UI Mode
class ChatBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI ChatBot")
        self.root.geometry("500x600")
        self.root.config(bg="#f0f0f0") 

        #chat display window
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled',
                                                       font=("Arial", 10), bg="#ffffff", fg="#000000")
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        #user input entry
        self.user_input = tk.Entry(self.root, font=("Arial", 12), bg="#e8e8e8", fg="#000000")
        self.user_input.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.user_input.bind("<Return>", self.process_input)

        #send button
        self.send_button = tk.Button(self.root, text="Send", command=self.process_input,
                                      font=("Arial", 14), bg="#4CAF50", fg="white", activebackground="#45a049")
        self.send_button.pack(padx=10, pady=(0, 10))

        #chat history
        self.chat_history = []
        self.display_message("Bot", "Hello! What's your name?")

    def process_input(self, event=None):
        user_message = self.user_input.get().strip()
        if not user_message:
            return

        self.display_message("You", user_message)
        self.user_input.delete(0, tk.END)

        #add user message to chat history
        self.chat_history.append({"role": "human", "content": user_message})

        #check if the user wants to exit using LLM
        if self.check_exit(user_message):
            self.display_message("Bot", "Goodbye!")
            self.root.after(2000, self.root.quit)
            return

        #Bot response
        ai_response = self.generate_response(user_message)
        self.display_message("Bot", ai_response)

    def display_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

    def generate_response(self, question):
        ai_msg = agent_executor.invoke({"input": question, "chat_history": self.chat_history})
        return ai_msg["output"]

    # Use the exit-checking prompt + LLM to know if user want to exit
    def check_exit(self, user_message):
        formatted_prompt = prompt_checking_exit.format(chat_history=self.chat_history, input=user_message)
        response = model.invoke(formatted_prompt)

        return response.content.strip() == "YES"

# Create the main application window
if __name__ == "__main__":
    if len(sys.argv) > 1: 
        if sys.argv[1] == 'CMD':
            chatbot()
        elif sys.argv[1] == "UI":
            root = tk.Tk()
            app = ChatBotUI(root)
            root.mainloop()
        

