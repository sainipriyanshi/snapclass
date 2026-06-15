import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen


def main():
    st.set_page_config(
        page_title="Making Attendance faster using AI",
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )
    st.markdown("""
             
      <style>
            button{
                background-color: #5865F2 !important;
                color: white !important;
                border: 1px solid transparent !important;
                transition: all 0.2s ease-in-out !important;
                }
            button:hover, button:focus, button:active {
                background-color: #5865F2 !important;
                color: white !important;
                border-color: white !important;
                outline: none !important;
                box-shadow: none !important;
                }
            input, textarea {
                caret-color: black !important;
                }
                </style>
    """, unsafe_allow_html=True)

    # Initialization
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        
        case 'student':
            student_screen()    

        case None:
            home_screen()

main()