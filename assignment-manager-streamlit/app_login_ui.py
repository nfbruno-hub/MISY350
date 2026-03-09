import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")

st.title("Course Manager")
st.divider()

json_file = Path("users.json")

if json_file.exists():
    with json_file.open("r", encoding="utf-8") as f:
        users = json.load(f)
else:
    users = [
        {
    "id": "1",
    "email": "admin@school.edu",
    "full_name": "System Admin",
    "password": "123ssag@43AE",
    "role": "Admin",
    "registered_at": "..."
}
    ]

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

# Navigation
tab1, tab2 = st.tabs(["Login", "register"])


# Register Page
with tab1:
     with st.container():
        st.subheader("Login")

        login_email = st.text_input("Email")
        login_password = st.text_input("Password", type="password")

        login_button = st.button("Log In", width="stretch")

        if login_button:
            with st.spinner("Verifying credentials..."):
                time.sleep(2)

                matched_user = None

                for user in users:
                    if user["email"] == login_email and user["password"] == login_password:
                        matched_user = user
                        break

                if matched_user:
                    st.success(
                        f"Welcome back, {matched_user['full_name']}! "
                        f"Role: {matched_user['role']}"
                    )
                else:
                    st.error("Invalid email or password.")
        st.subheader("Current User Database")
        st.dataframe(users)

with tab2:
     with st.container():
        st.subheader("New Instructor Account")

        register_email = st.text_input("Email Address")
        full_name = st.text_input("First and Last Name")
        register_password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Instructor"])

        create_account = st.button("Create Account", width="stretch")

        if create_account:
            with st.spinner("Creating your account..."):
                time.sleep(2)

                new_user = {
                    "id": str(uuid.uuid4()),
                    "email": register_email,
                    "full_name": full_name,
                    "password": register_password,
                    "role": role,
                    "registered_at": str(datetime.now())
                }

                users.append(new_user)

                with json_file.open("w", encoding="utf-8") as f:
                    json.dump(users, f, indent=4)

                st.success("Account created successfully!")

   