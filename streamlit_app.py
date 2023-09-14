# Import python packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

st.set_page_config(
    page_title="Generative AI using Snowflake External Functions and OpenAI",
    layout='wide'
)

st.title("Generative AI using Snowflake External Functions and OpenAI")
st.write(st.secrets.snowflake.user)

# Get the current credentials
session = get_active_session()
model = "gpt4"
