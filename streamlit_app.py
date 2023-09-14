# Import python packages
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Generative AI using Snowflake External Functions and OpenAI",
    layout='wide'
)

st.title("Generative AI using Snowflake External Functions and OpenAI")

conn = st.experimental_connection("snowflake")
st.write(st.secrets.snowflake.user)

# Get the current credentials
session = get_active_session()
model = "gpt4"
