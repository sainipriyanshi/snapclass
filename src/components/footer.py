
import streamlit as st


def footer_home():

    logo_url = "https://th.bing.com/th/id/OIP.swmZNKP5bfPjJgZDyIWX4AHaDS?w=337&h=155&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"

    st.markdown(f"""
        <div style="margin-top:2rem; display: flex; gap:6px; justify-content:center; items-alignment:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>
        <img src='{logo_url}' style='max-height:25px;'/>
                """, unsafe_allow_html=True)