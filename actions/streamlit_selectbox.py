import streamlit as st

CHOICES = {1: "dataset a", 2: "dataset b", 3: "dataset c"}

def format_func(option):
    return CHOICES[option]

#option = st.selectbox("Select option", options=list(CHOICES.keys()), format_func=format_func)
option = st.selectbox("Select option", options=list(CHOICES.keys()), format_func=lambda opt: CHOICES[opt])
st.write(f"You selected option {option} called {format_func(option)}")

# https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox