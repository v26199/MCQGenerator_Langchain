import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerater import generate_evaluate_chain
from src.mcqgenerator.logger import logging


# loading the json file
with open("E:\AI & Machine Learning\LLM,OpenAI\Automated-MCQ-Generator-Using-Langchain-OpenAI-API\Response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)


# Create a title for the app
st.title("Automated MCQ Generator with LangChain ")

# Create a form using the st.form
with st.form("user_inputs"):
    # file uploader
    upload_file=st.file_uploader("Upload a file",type=["txt","pdf"])

    # Input Fields
    mcq_count=st.number_input("Number of MCQs",min_value=3,max_value=50)

    # subjects
    subject=st.text_input("Subject",max_chars=50)

    # Qize Tone
    tone=st.text_input ("Complexity Level of Questions", max_chars=20, placeholder="Easy, Medium, Hard")

    # Submit Button
    submit_button=st.form_submit_button(label="Generate MCQs")

# Check if the submit button is clicked and all fields have input
if submit_button and upload_file is not None and subject and tone:
    with st.spinner("Generating MCQs..."):
        try:
            text = read_file(upload_file)

            #Count tokens and the cost of API call
            with get_openai_callback() as cb:
                response = generate_evaluate_chain({
                    "text": text,
                    "number": mcq_count,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                })

            # Debugging statements
            #print("Response:", response)
            #if isinstance(response, dict):
                #print("Quiz Data:", response.get("quiz"))

            # table_data = get_table_data(response.get("quiz", {}))
            # print("Table Data:", table_data)

            # if table_data is not None:
            #     df = pd.DataFrame(table_data)
            #     df.index = df.index + 1
            #     st.table(df)
            #     st.text_area(label="Review", value=response["review"], key="review_text_area")

        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error(e)


        else:
            
            print(f"Total Tokens:{cb.total_tokens}")
            print(f"Prompt Tokens:{cb.prompt_tokens}")
            print(f"Completion Tokens:{cb.completion_tokens}")
            print(f"Total Cost:{cb.total_cost}")

            if isinstance(response, dict):

                #Extract the quiz data from the respose
                quiz=response.get("quiz", None)
                if quiz is not None:
                    table_data=get_table_data(quiz)
                    if table_data is not None:
                        df=pd.DataFrame(table_data)
                        df.index=df.index+1
                        st.table(df)

                        #Display the review in a text box as well
                        st.text_area(label="Review",value=response["review"])

                else:
                    st.error("Error in the table data")

            else:
                st.write(response)
                
