import streamlit as st

#Step 1: Header First (Text Elements)
st.title("Course Manager")
st.header("Course Assignments Manager")
st.subheader("Course Assignments Manager")

st.divider()


#Step 2: Define Assignments List (Data Continuity)
assignments = [
    {
        "id" : "HW1",
        "title" : "Intro to Database",
        "description" : "Basics of database design",
        "points" : 100,
        "type" : "homework"
    } ,

    {
        "id" : "HW2",
        "title" : "Normalization",
        "description" : "Normalizing",
        "points" : 100,
        "type" : "homework"
    }
]


#Step 3: Add a New Assignment Section (Inputs & Layout)

st.subheader("Add New Assignment")

with st.container(border = True):
    ##col1, col2 = st.columns(2) --> this will give you 50/50 on size of "run app.py"
    col1, col2 = st.columns([2,1]) #this makes one column smaller than the other
    #col1,col2,col3 = st.columns([1,6,1])
    with col1:
        with st.container(border = True):
            st.markdown("### Assignment Details") #number of hashtags changes size - more #'s = smaller text 
            title = st.text_input("Assignment title", placeholder = "Homework 1", help = "Enter a short name")
            description = st.text_area("Assignment Description", placeholder = "ex. details...")
    with col2:
        st.markdown("**Due Date Selection**")
        due_date = st.date_input("Due Date")