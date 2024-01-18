# |Good parts:
# |1. The code imports the necessary libraries, including pandas and the pandasai library, which suggests that it will be working with data analysis and manipulation.
# |2. The code initializes the OpenAI language model, which indicates that it will be used for natural language processing tasks.
# |3. The code reads the Titanic dataset from a CSV file into a pandas DataFrame, which is a common and efficient way to handle tabular data.
# |4. The code uses the `head()` function to display the first 5 rows of the DataFrame, which helps in quickly inspecting the data.
# |5. The code creates a SmartDataframe object, which suggests that it will be using advanced features provided by the pandasai library for data analysis and interaction with the language model.
# |6. The code uses the `chat()` method of the SmartDataframe object to ask a question about the "Age" column, which demonstrates the ability to interact with the data using natural language queries.
# |
# |Bad parts:
# |1. The code imports the `apikey` module, but it is not clear how the `getOpenai()` function is implemented or what it does. This could lead to confusion or errors if the function is not properly defined or if the API key is not retrieved correctly.
# |2. The code does not handle any exceptions or errors that may occur during the execution, which could result in unexpected behavior or crashes if something goes wrong.
# |3. The code does not include any comments or explanations, making it difficult for others to understand the purpose and functionality of the code.
# |4. The code does not include any error handling or validation for the file path when reading the CSV file, which could lead to errors if the file does not exist or is in an incorrect format.
# |5. The code does not include any error handling or validation for the question asked in the `chat()` method, which could lead to unexpected results or errors if an invalid or unsupported question is provided.
# |
from openai import OpenAI
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from api import apikey

# Get the OpenAI API key
apikey.getOpenai()


# Initialize the OpenAI language model
llm = OpenAI(temperature=0)

# Read the Titanic dataset into a pandas DataFrame
df = pd.read_csv("data/titanic.csv")

# Display the first 5 rows of the DataFrame
df.head(5)

# Create a SmartDataframe object with the DataFrame and the OpenAI language model
df_ai = SmartDataframe(df, config={"llm": llm})

# Chat with the SmartDataframe and ask a question about the "Age" column
df_ai.chat("Age에서 누가 제일 많이 survived했을까요")

# Create a Streamlit app
st.title("SmartDataframe Chat")
question = st.text_input("Ask a question about the 'Age' column")
button = st.button("Submit")
if button:
    answer = df_ai.chat(question)
    st.write(answer)
