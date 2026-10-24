from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableParallel
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field

parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback, either positive or negative.")


prompt1 = PromptTemplate(
    template ='classify teh sentiment postive or negateibe \n {feedback}',
    input_variables = ['feedback']

)
classifier_chain = prompt1 | model | parser
result = classifier_chain.invoke({'feedback': 'this is a terrible smartphone'})
print(result)