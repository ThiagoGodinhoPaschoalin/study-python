import streamlit as st

if 'is_logged' not in st.session_state:
  st.session_state['is_logged'] = False

st.write(st.session_state['is_logged'])
button = st.empty()

if st.session_state['is_logged']:
  button = st.button('SAIR')
else:
  button = st.button('ENTRAR')

if button:
  if st.session_state['is_logged']:
    st.session_state['is_logged'] = False
  else:
    st.session_state['is_logged'] = True
  st.rerun()

st.write('eof')