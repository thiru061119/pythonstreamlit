import streamlit as st
import sqlite3

# Connect to database
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    Doe Dafault datetime
)
""")
conn.commit()

st.title("User Data")

# Form
with st.form("user_form"):
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=21, max_value=45)
    submit = st.form_submit_button("Save")

# Save to DB
if submit:
    if name:
        cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, age)
        )
        conn.commit()
        st.success("Saved to database ✅")
    else:
        st.error("Name is required")

# Show data
st.subheader("Saved Users")
rows = cursor.execute("SELECT name, age FROM users").fetchall()
st.table(rows)

