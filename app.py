import streamlit as st
import datetime

st.set_page_config(page_title="Teacher Dashboard", layout="wide")
st.markdown("""
    <style>
    .main {
        background-color: white;
    }
    .stButton>button {
        background-color: orange;
        color: white;
    }
    .stTextInput>div>div>input, .stTextArea textarea {
        background-color: #fffaf0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Teacher Profile")
st.sidebar.image("https://img.icons8.com/fluency/96/teacher.png", width=100)
st.sidebar.write("**Name:** Jane Doe")
st.sidebar.write("**Projects Managed:** 4")
st.sidebar.write("**Total Students:** 22")

# Tabs
tabs = st.tabs(["Create Rubric", "Create Project", "Attendance", "Feedback", "Dashboard"])

# Tab 1: Create Rubric
with tabs[0]:
    st.header("Create a New Rubric")
    rubric_name = st.text_input("Rubric Name")
    num_criteria = st.number_input("Number of Criteria", min_value=1, max_value=10, step=1)

    rubric = []
    for i in range(int(num_criteria)):
        with st.expander(f"Criterion {i + 1}"):
            name = st.text_input(f"Criterion Name {i + 1}", key=f"name_{i}")
            weight = st.slider(f"Weight {i + 1}", 0, 100, 20, key=f"weight_{i}")
            rubric.append((name, weight))

    if st.button("Save Rubric"):
        st.success("Rubric saved successfully!")

# Tab 2: Create Project
with tabs[1]:
    st.header("Create a New Project")
    project_name = st.text_input("Project Name")
    project_type = st.selectbox("Project Type", ["Single", "Couple", "Group"])
    assigned_rubric = st.selectbox("Assign Rubric", ["Rubric A", "Rubric B", "Create New..."])

    if st.button("Create Project"):
        st.success("Project created successfully!")

# Tab 3: Attendance
with tabs[2]:
    st.header("Mark Attendance")
    selected_date = st.date_input("Select Date", value=datetime.date.today())
    student_names = ["Alice", "Bob", "Charlie", "Diana"]
    for student in student_names:
        present = st.checkbox(f"{student} Present", key=student)

    if st.button("Submit Attendance"):
        st.success("Attendance recorded!")

# Tab 4: Feedback
with tabs[3]:
    st.header("Give Feedback")
    student = st.selectbox("Select Student", student_names)
    project = st.selectbox("Select Project", ["Project X", "Project Y"])
    feedback = st.text_area("Feedback")

    if st.button("Submit Feedback"):
        st.success("Feedback submitted!")

# Tab 5: Dashboard Summary
with tabs[4]:
    st.header("Dashboard Overview")
    st.metric("Projects Created", 4)
    st.metric("Rubrics Defined", 2)
    st.metric("Attendance Taken", "15 Days")
