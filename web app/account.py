import firebase_admin
import streamlit as st
from firebase_admin import credentials, auth

# Firebase setup
cred = credentials.Certificate(r"C:\Users\3ASHOUR\Desktop\project\graduation\Streamlit\pathcoder-8e50a-d624c04d2a65.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def app():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0D1117;
            color: #C9D1D9;
        }
        .stTextInput>div>div>input {
            background-color: #161B22;
            color: #C9D1D9;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.5em 1em;
            border: none;
        }
        .stButton>button:hover {
            background-color: #2EA043;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color:#58A6FF;'>🔐 Welcome to <span style='color:#A970FF;'>Pathcoder</span></h2>", unsafe_allow_html=True)

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    # Helper functions
    def login_user():
        try:
            user = auth.get_user_by_email(email)
            st.success("✅ Login Successful!")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True
        except:
            st.error("❌ Invalid Email or Password")

    def logout():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
        st.session_state.useremail = ''

    # Main Logic
    if not st.session_state.signedout:
        st.markdown("---")
        action = st.selectbox("Choose Action", ["Login", "Register"], key='account_choice')

        st.markdown("### ✉️ Enter your credentials")

        email = st.text_input("Email address")
        password = st.text_input("Password", type="password")

        if action == "Login":
            st.button("Login", on_click=login_user)

        else:
            username = st.text_input("Choose a unique username")

            def register_user():
                try:
                    user = auth.create_user(email=email, password=password, uid=username)
                    st.success("🎉 Account created successfully!")
                    st.info("Now you can login with your credentials.")
                    st.balloons()
                except:
                    st.error("⚠️ Registration failed. Check details or email might already be in use.")

            st.button("Register", on_click=register_user)

    if st.session_state.signout:
        st.markdown("---")
        st.markdown("### 👤 Logged in as")
        st.text(f"Username: {st.session_state.username}")
        st.text(f"Email: {st.session_state.useremail}")
        st.button("Sign Out", on_click=logout)

