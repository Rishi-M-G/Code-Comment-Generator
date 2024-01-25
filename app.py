import cohere
import streamlit as st

# Initialize Cohere API Key
co = cohere.Client('Nel6biNOKThlZ5heAFkesSi3kx7Cq8x3ppnUc47d') # Add your API key here

# Streamlit Title
st.title('Code Comment Generator')

# User Input
user_input = st.text_area("Enter your code here")
add_info = '''
In computer programming, a comment is a programmer-readable explanation or annotation in the source code of a computer program. They are added with the purpose of making the source code easier for humans to understand, and are generally ignored by compilers and interpreters.

give a comment line for this code and nothing more
'''

prompt = user_input + add_info

# Button to generate prediction
if st.button('Generate Comment'):
  response = co.generate(
    model='command',
    prompt= prompt,
    max_tokens=1376,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE'
  )
  st.text('Comment: {}'.format(response.generations[0].text))