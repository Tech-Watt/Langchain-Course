from api_key import *
import os 
import streamlit as st
os.environ['OPENAI_API_KEY'] = API_KEY
from langchain.llms import OpenAI
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain


                       # setting up langchain
llm = OpenAI(temperature=0.7)
result = llm('What is AI')
print(result)



                      # using prompt templeate
# template = PromptTemplate(
#     input_variables=['country_name'],
#     template ='I need a brief history about {country_name}'
# )
# print(template.format(country_name = 'CHINA'))


            # Creating chain for prompt template
# country_chain = LLMChain(
#     llm=llm,
#     prompt=template
# )
# result = country_chain.run('India')
# print(result)



                #   Using SimpleSequentialChains
# hist_template = PromptTemplate(
#     input_variables=['country_name'],
#     template ='I need a brief history about {country_name}'
# )

# resource_template = PromptTemplate(
#     input_variables=['history'],
#     template ='What impact do their {history} have on them',
    
# )

# hist_chain = LLMChain(llm=llm,prompt = hist_template)
# resource_chain = LLMChain(llm=llm,prompt=resource_template)


# country_chain = SimpleSequentialChain(
#     chains=[hist_chain,resource_chain]
# )
# result = country_chain.run('Ghana')
# print(result)



                  # Using Sequential chain
# hist_template = PromptTemplate(
#     input_variables=['country_name'],
#     template ='I need a brief history about {country_name}'
# )

# resource_template = PromptTemplate(
#     input_variables=['history'],
#     template ='What impact do their {history} have on them',
    
# )

# hist_chain = LLMChain(llm=llm,prompt=hist_template, output_key='history')
# resource_chain = LLMChain(llm=llm,prompt=resource_template, output_key='impact')

# country_chain = SequentialChain(
#     chains=[hist_chain,resource_chain],
#     input_variables =['country_name'],
#     output_variables = ['history','impact']
# )

# result = country_chain({'country_name':'Ghana'})

# print(result['history'])
# print(' ')
# print(result['impact'])






              # Building out the final project using langchain
# st.title('🦜️🔗 LangChain History Generator')
# prompt = st.text_input('Enter your prompt here')
# if prompt:
#     hist_template = PromptTemplate(
#     input_variables=['country_name'],
#     template ='I need a brief history about {country_name}'
#     )

#     resource_template = PromptTemplate(
#     input_variables=['history'],
#     template ='What impact do their {history} have on them',
        
#     )


#     hist_chain = LLMChain(llm=llm,prompt=hist_template, output_key='history')
#     resource_chain = LLMChain(llm=llm,prompt=resource_template, output_key='impact')


#     country_chain = SequentialChain(
#         chains=[hist_chain,resource_chain],
#         input_variables =['country_name'],
#         output_variables = ['history','impact']
#     )

    
#     result = country_chain({'country_name':prompt})
#     st.title('History')
#     st.write(result['history'])
#     st.title('Impact')
#     st.write(result['impact'])
#     print(result['history'])
#     print(result['impact'])
        