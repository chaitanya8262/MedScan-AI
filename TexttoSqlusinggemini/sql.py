from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Gemini Key

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

## Function To load Google Gemini Model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    for row in rows:
        print(row)
    return rows    

## define your prompt
prompt=[
    """
You are an expert in converting English questions to sql query!
The SQL database has the name STUDENT and has the following columns - Name, Class, 
Section \n\n For example, \n Example 1 - How many entries of records are present?,
\n Example 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
also the sql code should  not have ''' in beginning or  end sql word in output

"""
]


## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App to Retrieve Any SQL Query")

question = st.text_input("Input:", key="input")
submit=st.button("Ask the Question")

# if submit is clicked
if submit:
    response=get_gemini_response(question, prompt)
    response=read_sql_query(response, "student.db")
    st.header("The Response is")
    for row in response:
        print(row)
        st.header(row)

