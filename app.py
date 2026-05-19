import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen


def main():
    
    st.markdown("""
             
      <style>
            button{
                background:orange !important;
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