import streamlit as st
from PIL import Image

def app():
    # Optional logo
    # logo = Image.open("pathcoder_logo.png")
    # st.image(logo, use_column_width=True)

    # Set custom dark theme styling
    st.markdown(
        """
        <style>
            /* Background and text color */
            .main {
                background-color: #0D1117;
                color: #C9D1D9;
            }
            h1, h2, h3 {
                color: #58A6FF;
            }
            .stApp {
                background-color: #0D1117;
            }
            .stMarkdown, .stText, .stHeader {
                color: #C9D1D9;
            }

            /* Button style */
            .stButton>button {
                background-color: #238636;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 0.5em 1em;
                margin-top: 10px;
                border: none;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #2EA043;
                cursor: pointer;
            }

            /* Success message styling override */
            .stAlert {
                background-color: #161B22;
                color: #C9D1D9;
                border-left: 0.5rem solid #238636;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main content
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color:#238636;">👩‍💻 Welcome to <span style="color:#58A6FF;">Pathcoder</span></h1>
            <p style="font-size:18px; max-width:700px; margin:auto; color:#C9D1D9;">
                Pathcoder is your smart career assistant that helps you choose the right path based on your skills and ambitions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.header("🔍 Discover")
        st.write("Explore different tech careers tailored to your skill set.")

    with col2:
        st.header("🧠 Learn")
        st.write("Get personalized skill recommendations to grow your career.")

    st.markdown("### 🚀 Ready to begin?")
    st.success("Navigate to the **Career Development** section to get started!")
