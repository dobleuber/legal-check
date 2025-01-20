from langchain_core.documents import Document
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda
from langchain.text_splitter import RecursiveCharacterTextSplitter

from typing import List
from pydantic import BaseModel, Field
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser

from dotenv import load_dotenv
load_dotenv()

import os

class Suspect(BaseModel):
    """Tag the information about the suspect"""
    name: str = Field(..., description="The name of the suspect")
    age: int = Field(..., description="The age of the suspect")
    country: str = Field(..., description="The country of the suspect")

class SuspectList(BaseModel):
    """Tag the list of suspects"""
    suspects: List[Suspect] = Field(..., description="The list of suspects")

extraction_functions = [convert_pydantic_to_openai_function(SuspectList)]

llm = ChatOpenAI(
    model='gpt-4o-mini',
)

extraction_model = llm.bind(functions=extraction_functions, function_call={"name": "SuspectList"})

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract the relevant information, if not explicitly provided do not guess. Extract partial info"),
    ("human", "{input}")
])

extraction_chain = prompt | extraction_model | JsonKeyOutputFunctionsParser(key_name="suspects")

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]

def flatten(matrix):
  flat_list = []
  for row in matrix:
    flat_list += row
  return flat_list

text_explitter = RecursiveCharacterTextSplitter(chunk_overlap=0)

prep = RunnableLambda(
    lambda x: [{"input": doc} for doc in text_explitter.split_text(x)]
)

prepare_documents = RunnableLambda(
    lambda x: "\n\n".join([doc.page_content for doc in x])
)

full_chain = prepare_documents | prep | extraction_chain.map() | flatten

def fugitive_list():
    loader = WebBaseLoader([
        "https://eumostwanted.eu/es/list",
        "https://www.interpol.int/es/Como-trabajamos/Notificaciones/Notificaciones-rojas/Ver-las-notificaciones-rojas",
        "https://www.fbi.gov/wanted/topten",
        "https://www.fbi.gov/wanted/fugitives",
        "https://www.dea.gov/es/node/11286",
        "https://scsanctions.un.org/6ooznen-all.html",
    ])

    documents = loader.load()
    
    results = full_chain.invoke(documents)
    
    print(results)

def main() -> None:
    print("hello world!")

    fugitive_list()

if __name__ == "__main__":
    main()