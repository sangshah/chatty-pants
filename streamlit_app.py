import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

#st.title('🎈 ChattyPants - AI Chatbot')
st.set_page_config(page_title="🤗💬 ChattyPants")


st.write('🎈 ChattyPants - AI Chatbot')

with st.sidebar:
    st.title('🤗💬 ChattyPants')
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
        st.success('HuggingFace Login credentials already provided!', icon='✅')
        hf_email = st.secrets['EMAIL']
        hf_pass = st.secrets['PASS']
    else:
        hf_email = st.text_input('Enter E-mail:', type='password')
        hf_pass = st.text_input('Enter password:', type='password')
        if not (hf_email and hf_pass):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')
Use the with statement 
