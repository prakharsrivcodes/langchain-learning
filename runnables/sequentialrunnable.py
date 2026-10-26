from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parser import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv() 
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template = 'wrote joke on {topic}',
    input_variables = ['topic'],
)
parser = StrOutputParser()
prompt2 = PromptTemplate(

)
chain =RunnableSequence(prompt, model, parser, prompt, model, parser)
print(chain.invoke({'topic': 'chicken'}))

