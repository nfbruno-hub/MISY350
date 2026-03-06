import streamlit as st

st.title("Course Management App")
st.markdown("") #Create space
st.header("Assignment Management")
st.subheader("Dashboard")

next_assignment_id_number = 3

st.divider()
#st.markdown("-----") #Same as st.divider


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


#Input

#More hashtags = smaller text:
#st.markdown("# Add New Assignment")
st.markdown("## Add New Assignment")
#st.markdown("### Add New Assignment")

title = st.text_input("Title")
description = st.text_area("Description", placeholder = "Ex. Normalization is covered here", 
                           help = "Here we are entering the assignment details")
points = st.number_input("Points") #what an assignment is worth in a numeric value

#do not want st.text_input for categorical inputs:
##radio = radio buttons
assignment_type = st.radio("Type", ["Homework" , "Lab"], horizontal = True) #Title, [choice 1, choice 2, etc.]; vertical is default
st.caption("Homework type")
##selectbox = dropdown
assignment_type2 = st.selectbox("Type", ["Select an option", "Homework", "Lab", "Other"]) #"Select an option" gives user optional choice to answer question

if assignment_type2 == "Other":
    assignment_type2 = st.text_input("Type", placeholder= "Enter the assignment type")

due_date = st.date_input("Due Date")

#Create a button to save the assignment
btn_save = st.button("Save", width = "stretch", disabled = False) #width changes button size

import time
import json
from pathlib import Path

json_path = Path("assignments.json")

# "if the button is clicked, create an action"
if btn_save: 
    if not title:
        st.warning("Title needs to be provided!")
    else:
        with st.spinner("Assignment is being recorded..."):
            time.sleep(5)

            new_assignment_id = "HW" + str(next_assignment_id_number)
            next_assignment_id_number += 1

            assignments.append(
                {
                    "id" : new_assignment_id,
                    "title" : title,
                    "description" : description,
                    "points" : points,
                    "type" : assignment_type
                }
            ) 

            #record into json file
            with json_path.open("w", encoding = "utf-8") as f: #open file, name it "f"
                json.dump(assignments, f) # "dump assignments into 'f"

            st.success("New assignment is recorded!")
            st.info("This is a new assignment")
            st.dataframe(assignments) #creates list of assignments after saving on Streamlit