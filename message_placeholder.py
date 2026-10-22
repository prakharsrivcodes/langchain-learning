from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder    
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chat_template = ChatPromptTemplate([
    ('system', 'you are  helpful customer supprt')
    MessagePlaceholder(variable_name = 'chat_history')
    ('human', 'I have a problem with my order')
])