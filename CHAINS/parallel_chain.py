from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableParallel

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model3 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt1 = PromptTemplate(
    template ='generate short notes from this text {text}',
    input_variables = ['text']
)
prompt2 = PromptTemplate(
    template = 'generate 5 short ques from this \n {text}',
    input_variables = ['text']

)
prompt3 = PromptTemplate(
    template = 'merge the notes and qui into single \n notes -> {notes}, quiz -> {quiz}',
    input_variables = ['notes', 'quiz']
)
parser = StrOutputParser()
parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})
merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain
text = """Cricket is a bat-and-ball game played between two teams of eleven players on a field at the center of which is a 22-yard pitch with a wicket at each end, each comprising two bails balanced on three stumps. The batting side scores runs by striking the ball bowled at the wicket with the bat, while the bowling and fielding side tries to prevent this and dismiss each player (so they are "out"). Means of dismissal include being bowled, when the ball hits the stumps and dislodges the bails, and by the fielding side catching the ball after it is hit by the bat, but before it hits the ground. When ten players have been dismissed, the innings ends and the teams swap roles. The game is adjudicated by two umpires, aided by a third umpire and match referee in international matches. They communicate with two off-field scorers who record the match's statistical information."""
result = chain.invoke({'text': text})
print(result)

  
