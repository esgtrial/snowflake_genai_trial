# Import python packages
import streamlit as st
import pandas as pd

st.write(st.secrets.snowflake.user)


st.set_page_config(
    page_title="Generative AI using Snowflake External Functions and OpenAI",
    layout='wide'
)

st.title("Generative AI using Snowflake External Functions and OpenAI")

