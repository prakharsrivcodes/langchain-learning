from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
class Review(TypedDict):
    pros: Annotated[Optional[list[str]], "The positive aspects of the product or service"]
    key_themes: Annotated[list[str], "The key themes of the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review (positive/negative/neutral)"]

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("history of humayun tomb very crisp, the history of the mughal art the changing empires in the delhi in years who htoight whey willl last forever")
print(result)  