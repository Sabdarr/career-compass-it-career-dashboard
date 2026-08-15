import streamlit as st 
import pandas as pd

df=pd.read_excel("career_dataset.xlsx")

st.markdown("""
<div style="
    background-color:#1E3A8A;
    padding:20px;
    border-radius:10px;
    text-align:center;
    color:white;
">
    <h1>🎯 Career Compass: IT Career Dashboard</h1>
    <p>Explore career paths, required skills, salary growth, and future opportunities.</p>
</div>
""", unsafe_allow_html=True)


# SIDEBAR
st.sidebar.title("🎯 Career Compass")
st.sidebar.caption("IT Career Dashboard")
st.sidebar.markdown("---")
st.sidebar.subheader("📂 Career Selection")
career_list = ["Select a Career"] + sorted(df["career"].unique())
selected_career = st.sidebar.selectbox(
    "Choose Career",
    career_list
)
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Dashboard Statistics")
st.sidebar.metric(
    "💼 Careers",
    df["career"].nunique()
)
st.sidebar.metric(
    "🏢 Domains",
    df["domain"].nunique()
)
st.sidebar.markdown("---")
st.sidebar.success(
    "Choose a career to explore salary, skills, roadmap and analytics."
)


st.sidebar.markdown("---")
st.sidebar.info(f"""
Total Careers : {df['career'].nunique()}
Domains : {df['domain'].nunique()}
""")
if selected_career == "Select a Career":
    st.info("👈 Please select a career from the sidebar to view complete details.")
    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        use_container_width=True
    )
    st.stop()
career_data = df[df["career"] == selected_career].iloc[0]

tab1,tab2,tab3,tab4 = st.tabs([
"Overview",
"Skills",
"Roadmap",
"Analytics"
])

with tab1:
    st.subheader(selected_career)
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)
with col1:
    st.metric(
        "💰 Starting Salary",
        f"{career_data['starting_salary_LPA']} LPA"
    )
with col2:
    st.metric(
        "📈 5-Year Salary",
        f"{career_data['salary_5yr_LPA']} LPA"
    )
with col3:
    st.metric(
        "🔥 Demand",
        career_data["demand_level"]
    )
with col4:
    st.write("### Domain")
    st.success(career_data["domain"])

    st.write("### Top Locations")
    st.write(career_data["top_locations"])

with col5:
    st.write("### Growth Potential")
    st.info(career_data["growth_potential"])

    st.write("### Opportunities")
    st.write(career_data["opportunities"])

with tab2:
    skills = career_data["skills"].split(",")
    cols = st.columns(len(skills))
    for i,skill in enumerate(skills):
        cols[i].success(skill.strip())

with tab3:
    roadmap = career_data["roadmap"].split(">")
    for i,step in enumerate(roadmap):
        st.write(f"### {i+1}. {step.strip()}")
        if i != len(roadmap)-1:
            st.write("⬇️")


with tab4:
    st.subheader("Salary Analytics")
    st.write("Compare starting and 5-year salaries accross different careers.")

    st.subheader("Starting Salary Comparison")
    st.bar_chart(
        df.set_index("career")["starting_salary_LPA"]
    )

    st.subheader("5-Year Salary Comparison")
    st.bar_chart(
        df.set_index("career")["salary_5yr_LPA"]
    )



