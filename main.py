import streamlit as st
from datetime import datetime
import pandas as pd
import os

# App title
st.set_page_config(page_title="Shared Positive Diary", page_icon="😊", layout="centered")
st.title("🌟 Shared Positive Diary App")

# File to store diary entries
DIARY_FILE = "diary_entries.csv"

# Load existing diary entries from file
def load_diary_entries():
    if os.path.exists(DIARY_FILE):
        return pd.read_csv(DIARY_FILE)
    else:
        return pd.DataFrame(columns=["Name", "Event", "Timestamp"])

# Save diary entries to file
def save_diary_entries(entries_df):
    entries_df.to_csv(DIARY_FILE, index=False)

# Initialize diary entries
diary_entries = load_diary_entries()

# Applying custom Bootstrap styling
st.markdown(
    """
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            font-family: 'Helvetica', sans-serif;
        }
        .submit-btn {
            background-color: #007bff;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #0056b3;
        }
        .diary-entries {
            margin-top: 30px;
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
    <div class="main-container">
        <h1 class="header">Shared Positive Diary</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Input form for diary entry
with st.form("diary_form"):
    st.markdown("### Add a Positive Event 🌈")
    name = st.text_input("Your Name", placeholder="Enter your name")
    event = st.text_area("Positive Event", placeholder="Describe the positive event")
    submitted = st.form_submit_button("Add Entry", type="primary")

    if submitted:
        if name and event:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_entry = pd.DataFrame({"Name": [name], "Event": [event], "Timestamp": [timestamp]})
            diary_entries = pd.concat([diary_entries, new_entry], ignore_index=True)
            save_diary_entries(diary_entries)  # Save updated entries to file
            st.success("Your entry has been added!")
        else:
            st.error("Please provide your name and a positive event.")

# Display diary entries
if not diary_entries.empty:
    st.markdown("### 📖 Diary Entries")
    st.dataframe(diary_entries.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])]))
else:
    st.markdown("### 📖 Diary Entries")
    st.info("No entries yet! Add your first positive event above.")

