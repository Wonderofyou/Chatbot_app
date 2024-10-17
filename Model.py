import os
import dotenv
from langchain_groq import ChatGroq
dotenv.load_dotenv()

# Load api_key in .env file for private
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

#load LLM model.
model = ChatGroq(model="llama3-70b-8192") 

