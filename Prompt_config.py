from langchain_core.prompts import ChatPromptTemplate
from datetime import date

#Instruction prompt to agent to know when to use the tool 
today = date.today().strftime("%Y-%m-%d")
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"""You are a helpful assistant focused on answering questions based on your knowledge.
            Only use tools when the user specifically asks about the current or historical weather directly. 
            For hypothetical questions, provide an answer based on your knowledge without using any tools.

            The tool format should be 'City, YYYY-MM-DD' for weather questions.
            If the user asks about today's weather, use {today} date by default. 
            If the user asks about a specific date, use that date.

            Use the following thought process:

            1. **Question**: Analyze the input question.
            2. **Thought**: Determine if the question is specifically about the weather.
            3. **If it is about the weather**: Prepare to use the tool.
            4. **If it is a hypothetical question**: Respond based on your knowledge without using tools.
            5. **Action Input**: The input to the action (if the question is about the weather).
            6. **Observation**: The result of the action (if a tool is used).

            Repeat the Thought/Action/Action Input/Observation process as necessary.
            Conclude with a **Final Answer**: Provide the final answer to the original question.

            ONLY show the final answer.
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

#Prompt template to check if user want to leave
prompt_checking_exit = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a system to determine if the user wants to exit or not. If the user wants to exit, answer YES; else answer NO. DO NOT answer anything else."""
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)