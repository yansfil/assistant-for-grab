from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes


load_dotenv()
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="Hello, how are you?"),
]

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(
    title="Langchain API",
    version="0.1",
    description="API for Langchain",
)

add_routes(
    app, chain, path="/chain"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)