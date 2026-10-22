from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", max_output_tokens=512, temperature=1.0)
result = model.invoke("history of humayun tomb very crisp")
print(result.content)

