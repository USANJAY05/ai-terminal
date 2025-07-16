import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found! Please set it in the .env file.")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=api_key
)

# Prompt Templates
command_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a Linux command-line expert.

Return only the simplest and most direct Linux command(s) to accomplish the given task.
- Put each command on a new line.
- Do not explain or number them.
- Avoid unsafe commands (rm -rf, mkfs, dd, etc.).
- If unsure, return an empty line.

Request: {question}
"""
)

summary_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
You are a text summarizer.

Summarize the following text in a clear and concise way (3-5 sentences):

Text:
{content}
"""
)
