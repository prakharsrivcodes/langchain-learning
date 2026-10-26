from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parser import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableParallel, RunnableSequence
from regex import template
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt1 = PromptTemplate(
    template= "Write a tweet about {topic} in 280 characters or less."
    input_variables= ["topic"]  
)
prompt2 = PromptTemplate(
    template= "Write a LinkedIn post about {topic} in 1000 characters or less."
    input_variables= ["topic"]  
)
parser = StrOutputParser()
parallel_chain = RunnableParallel(
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser),

)
result  = parallel_chain.invoke({'topic': 'AI'})
print(result);