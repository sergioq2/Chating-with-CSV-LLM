import pandas as pd
import numpy as np
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import create_pandas_dataframe_agent
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

from preprocessing import preprocesamiento
import re

os.environ["OPENAI_API_KEY"] = "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"

def estimator(user, df):
    llm = OpenAI(temperature=0.2)
    agent_one = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

    template = """List the top 5 job vacancy names with more accuracy for the candidate with the next description'{user}' along with their respective match values.
    Example:
        vacancy_name: match_value,
        ....
    """
    prompt_template = PromptTemplate(input_variables=["user"], template=template)
    agent_two = LLMChain(llm=llm, prompt=prompt_template) 

    overall_chain = SimpleSequentialChain(
                    chains=[agent_one, agent_two],
                    verbose=True)


    question = "What is the best 5 vacancy job names with more accuracy (only the vacancy_name) for the candidate with the next description: {user} with the value of the match? "
    answer = overall_chain.run(question)
    return answer

def clean_string(string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s,]', '', string)
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string)
    return cleaned_string

def principal(user):
    vacantes, vacantes_summary, users = preprocesamiento()
    salida = clean_string(estimator(user, vacantes_summary))
    return salida

if __name__ == '__main__':
    result = principal()
    print(result)
