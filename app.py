import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title="Snapclass - Making Attendance faster using AI",
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

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
          
        is_logged_in = st.session_state.get("is_logged_in", False)
        user_role = st.session_state.get("user_role")

        if is_logged_in:
            if user_role == "student":
                # Trigger the dialog from dialog_auto_enroll.py
                auto_enroll_dialog(join_code)
            else:
                st.warning(
                    "⚠️ You are currently logged in as a Teacher. Please switch to a Student account to join this class."
                )
        else:
            st.info(
                f"🔑 Please log in or register as a Student to join class **{join_code}**."
            )

main()