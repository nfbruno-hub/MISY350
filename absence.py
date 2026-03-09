import streamlit as st
import json
from pathlib import Path
import time

st.set_page_config(page_title="Excused Absence App", layout="centered", initial_sidebar_state="expanded")

if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"

if "selected_request" not in st.session_state:
    st.session_state["selected_request"] = None

json_path = Path("absence_requests.json")

absence_requests = [
    {
        "request_id": "0111212",
        "status": "Pending",
        "course_id": "011101",
        "student_email": "jsmith@university.edu",
        "absence_date": "2026-03-25",
        "submitted_timestamp": "2026-03-19 08:30:00",
        "excuse_type": "Medical",
        "explanation": "I have a scheduled doctor's appointment that I cannot reschedule.",
        "instructor_note": ""
    }
]

if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        requests = json.load(f)
else:
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(absence_requests, f, indent=4)

with st.sidebar:

    if st.button("Dashboard", key="sidebar_dashboard_btn", type="primary", use_container_width=True):
        st.session_state["page"] = "dashboard"
        st.rerun()

    if st.button("Request", key="sidebar_request_btn", type="primary", use_container_width=True):
        st.session_state["page"] = "request"
        st.rerun()

st.title("Excused Absence Management System")
st.divider()

if st.session_state["page"] == "dashboard":
    st.header("Excused Absence Dashboard")

    col1, col2 = st.columns([2, 1])

    with col1:
        if len(requests) > 0:
            event = st.dataframe(
                requests,
                on_select="rerun",
                selection_mode="single-row",
                use_container_width=True
            )

            if event.selection.rows:
                selected_index = event.selection.rows[0]
                st.session_state["selected_request"] = requests[selected_index]
        else:
            st.warning("No excuse requests have been submitted yet.")

    with col2:
        st.metric("Total Requests", f"{len(requests)}")

        pending_count = 0
        for request in requests:
            if request["status"] == "Pending":
                pending_count += 1

        st.metric("Pending", f"{pending_count}")

    if st.session_state["selected_request"]:
        selected_request = st.session_state["selected_request"]

        st.divider()
        with st.container(border=True):
            st.subheader("Selected Request Details")
            st.markdown(f"**Request ID:** {selected_request['request_id']}")
            st.markdown(f"**Status:** {selected_request['status']}")
            st.markdown(f"**Course ID:** {selected_request['course_id']}")
            st.markdown(f"**Student Email:** {selected_request['student_email']}")
            st.markdown(f"**Absence Date:** {selected_request['absence_date']}")
            st.markdown(f"**Submitted Timestamp:** {selected_request['submitted_timestamp']}")
            st.markdown(f"**Excuse Type:** {selected_request['excuse_type']}")
            st.markdown(f"**Explanation:** {selected_request['explanation']}")
            st.markdown(f"**Instructor Note:** {selected_request['instructor_note']}")

            st.divider()

            updated_note = st.text_area(
                "Instructor Note",
                value=selected_request["instructor_note"],
                key=f"dashboard_instructor_note_{selected_request['request_id']}"
            )

            col3, col4, col5 = st.columns(3)

            with col3:
                if st.button("Save Note", key=f"dashboard_save_note_btn_{selected_request['request_id']}", use_container_width=True):
                    for request in requests:
                        if request["request_id"] == selected_request["request_id"]:
                            request["instructor_note"] = updated_note
                            st.session_state["selected_request"] = request
                            break

                    with json_path.open("w", encoding="utf-8") as f:
                        json.dump(requests, f, indent=4)

                    st.success("Instructor note updated!")
                    time.sleep(1)
                    st.rerun()

            with col4:
                if st.button("Approve", key=f"dashboard_approve_btn_{selected_request['request_id']}", use_container_width=True):
                    for request in requests:
                        if request["request_id"] == selected_request["request_id"]:
                            request["status"] = "Approved"
                            request["instructor_note"] = updated_note
                            st.session_state["selected_request"] = request
                            break

                    with json_path.open("w", encoding="utf-8") as f:
                        json.dump(requests, f, indent=4)

                    st.success("Request approved!")
                    time.sleep(1)
                    st.rerun()

            with col5:
                if st.button("Cancel", key=f"dashboard_cancel_btn_{selected_request['request_id']}", use_container_width=True):
                    for request in requests:
                        if request["request_id"] == selected_request["request_id"]:
                            request["status"] = "Cancelled"
                            request["instructor_note"] = updated_note
                            st.session_state["selected_request"] = request
                            break

                    with json_path.open("w", encoding="utf-8") as f:
                        json.dump(requests, f, indent=4)

                    st.success("Request cancelled!")
                    time.sleep(1)
                    st.rerun()

elif st.session_state["page"] == "request":
    st.header("Excused Absence Request Form")
    