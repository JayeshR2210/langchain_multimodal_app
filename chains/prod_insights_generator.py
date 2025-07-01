from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI() 
llm = HuggingFaceEndpoint (
    repo_id= "deepseek-ai/DeepSeek-R1-0528",
    task= "text-generation"
)
llm1 = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)
model2 = ChatHuggingFace(llm=llm)
model3 = ChatHuggingFace(llm=llm1)

prompt1 = PromptTemplate(
    template='Generate a one line summary on the {product}',
    input_variables=['product']
)
prompt2 = PromptTemplate(
    template='Extract potential audience for the {product}',
    input_variables=['product']
)
prompt3 = PromptTemplate(
    template='Suggest creative tagline for the {product}',
    input_variables=['product']
)
prompt4 = PromptTemplate(
    template='Write a single compelling paragraph combining:\nSummary: {summary}\nAudience: {audience}\nTagline: {tagline}',
    input_variables=['summary','audience','tagline']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'summary': prompt1|model1|parser,
    'audience': prompt2|model2|parser,
    'tagline': prompt3|model3|parser
})

merge_chain = prompt4|model1|parser

final_chain = parallel_chain | merge_chain

result = final_chain.invoke({'product':'airpods'})
print(result)