from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

class Career(BaseModel):
    Question : Literal["tech","other"] = Field(description='Enter the type of career advice ')

parser2 = PydanticOutputParser(pydantic_object=Career)

prompt1 = PromptTemplate(
    template='Classify the following question into the tech related query or other \n {text} {format_instruction}',
    input_variables=['text'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Generate an appropriate guidance to this tech related question \n {text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Generate an appropriate guidance to this other career related question and guide the user how to tackle that question \n {text}',
    input_variables=['text']
)

cond_chain = RunnableBranch(
    (lambda x : x.Question == 'tech' , prompt2 | model | parser),
    (lambda x : x.Question == 'other' , prompt3 | model | parser),
    RunnableLambda(lambda x : 'could not found any question')
)

chain = classifier_chain | cond_chain

text = """
How does the genetic algorithm in the TSP solver ensure diversity in the population to avoid premature convergence?
"""
result = chain.invoke({'text':text})
print(result)