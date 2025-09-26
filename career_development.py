import streamlit as st
import requests

def app():
    API_BASE = "http://127.0.0.1:5000"  # Update if hosted elsewhere

    st.markdown("""
        <style>
        .stApp {
            background-color: #0D1117;
            color: #C9D1D9;
        }
        .stButton>button {
            background-color: #238636;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
            border: none;
        }
        .stButton>button:hover {
            background-color: #2EA043;
            cursor: pointer;
        }
        .stSelectbox, .stMultiSelect, .stTextInput {
            background-color: #161B22;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color:#58A6FF;'>📈 Career Development</h2>", unsafe_allow_html=True)
    st.write("🚀 Use this tool to explore career paths and discover the skills you need.")

    # Step 1: Fetch skills and job list
    @st.cache_data
    def fetch_skills_and_jobs():
        try:
            response = requests.get(f"{API_BASE}/skills")
            if response.status_code == 200:
                data = response.json()
                return data["Skills"], data.get("target_job", [])
            else:
                st.error("⚠️ Failed to fetch skill data from API.")
                return {}, []
        except Exception as e:
            st.error(f"🚫 Could not connect to the API: {e}")
            return {}, []

    skills_data, target_jobs = fetch_skills_and_jobs()

    # Step 2: Skill Selection
    st.markdown("### 🛠️ Select Your Existing Skills")
    selected_skills = []
    for category, options in skills_data.items():
        selected = st.multiselect(f"**{category}**", options)
        selected_skills.extend(selected)

    # Step 3: Target Job Dropdown
    st.markdown("### 🎯 Choose a Target Job (Optional)")
    target_job = st.selectbox("Select a career goal", [""] + target_jobs)

    # Step 4: Recommendation Button
    if st.button("🔍 Get Skill Recommendations"):
        if not selected_skills:
            st.warning("⚠️ Please select at least one skill to continue.")
        else:
            with st.spinner("⏳ Analyzing your skills and finding recommendations..."):
                try:
                    payload = {
                        "skills": selected_skills,
                        "target_job": target_job.strip() if target_job else ""
                    }
                    response = requests.post(f"{API_BASE}/recommend_skills", json=payload)
                    if response.status_code == 200:
                        result = response.json()

                        st.markdown(f"### 📊 Predicted Job Probabilities")
                        st.image(f"{API_BASE}{result['job_plot_url']}")

                        st.markdown(f"### 🧠 Recommended Skills for: `{result['target_job_used']}`")
                        st.image(f"{API_BASE}{result['skills_plot_url']}")

                        st.markdown("### 🧾 Skill List")
                        st.json(result["recommended_skills"])
                    else:
                        st.error("❌ Error fetching recommendations. Try again or check your input.")
                except Exception as e:
                    st.error(f"🚨 An error occurred: {e}")




