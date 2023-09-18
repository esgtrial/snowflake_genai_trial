# Import python packages
import streamlit as st
import pandas as pd

conn = st.experimental_connection('snowflake')

# Perform query.
df = conn.query('OPENAI.PUBLIC.CUSTOMER_SALES;', ttl=600)



st.set_page_config(
    page_title="Generative AI using ❄️ Snowflake External Functions and OpenAI",
    layout='wide'
)

st.title("Generative AI using Snowflake External Functions and OpenAI")
st.write(st.secrets.snowflake.user)

# Establish Snowflake session
#@st.cache_resource
#def create_session():
#    return Session.builder.configs(st.secrets.snowflake).create()

#session = create_session()
st.success("Connected to Snowflake!")
