import streamlit as st
from streamlit_modal import Modal

'''

->> streamlit run .\streamlit_modal.py

'''

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.logo('./../images/qrcode.png', size='large')

modal = Modal(key="3d_EffmnAQc", title="Título do Modal")

left, middle, right = st.columns(3)

if left.button("Plain button", use_container_width=True):
  left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
  modal.open()
if right.button("Material button", icon=":material/mood:", use_container_width=True):
  right.markdown("You clicked the Material button.")

if modal.is_open():
  with modal.container():
    st.video("https://www.youtube.com/watch?v="+ modal.key)

