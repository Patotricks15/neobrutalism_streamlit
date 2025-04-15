import streamlit as st
import pandas as pd
import os

# Configure the page
st.set_page_config(page_title="Neobrutalism Components Demo", layout="centered")

# Function to load a CSS file and inject its content into the page
def local_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS files
css_path = os.path.join("css", "general.css")
local_css(css_path)

css_path = os.path.join("css", "components.css")
local_css(css_path)

# Main Header
st.markdown("<h1 style='text-align: center;'>Neobrutalism Components Demo</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Example of various components with a neobrutalism style</p>", unsafe_allow_html=True)

# ================================
# 1. Input Components
# ================================

# Text Input
with st.container():
    st.markdown("<div class='container-title'>Text Input</div>", unsafe_allow_html=True)
    name = st.text_input("Name", "Enter your name", key="input_name")
    st.markdown("</div>", unsafe_allow_html=True)

# Text Area
with st.container():
    st.markdown("<div class='container-title'>Comment</div>", unsafe_allow_html=True)
    comment = st.text_area("Comment", placeholder="Write your comment", key="textarea_comment")
    st.markdown("</div>", unsafe_allow_html=True)

# Checkbox
with st.container():
    st.markdown("<div class='container-title'>Checkbox</div>", unsafe_allow_html=True)
    accept_terms = st.checkbox("Accept terms and conditions", key="checkbox_terms")
    st.markdown("</div>", unsafe_allow_html=True)

# Radio Buttons
with st.container():
    st.markdown("<div class='container-title'>Radio Buttons</div>", unsafe_allow_html=True)
    option = st.radio("Choose an option", ('Option 1', 'Option 2', 'Option 3'), key="radio_options")
    st.markdown("</div>", unsafe_allow_html=True)

# SelectBox
with st.container():
    st.markdown("<div class='container-title'>SelectBox</div>", unsafe_allow_html=True)
    select_option = st.selectbox("Select an option", ['Item A', 'Item B', 'Item C'], key="selectbox_options")
    st.markdown("</div>", unsafe_allow_html=True)

# MultiSelect
with st.container():
    st.markdown("<div class='container-title'>MultiSelect</div>", unsafe_allow_html=True)
    multi_options = st.multiselect("Select multiple options", ['Option X', 'Option Y', 'Option Z'], key="multiselect_options")
    st.markdown("</div>", unsafe_allow_html=True)

# Number Input
with st.container():
    st.markdown("<div class='container-title'>Number Input</div>", unsafe_allow_html=True)
    number_value = st.number_input("Enter a number", min_value=0, max_value=100, value=10, key="number_input")
    st.markdown("</div>", unsafe_allow_html=True)

# ================================
# 2. Selection and Time Components
# ================================

# Slider
with st.container():
    st.markdown("<div class='container-title'>Slider</div>", unsafe_allow_html=True)
    slider_value = st.slider("Select a value", 0, 100, 50, key="slider_value")
    st.markdown("</div>", unsafe_allow_html=True)

# Date Input
with st.container():
    st.markdown("<div class='container-title'>Date Input</div>", unsafe_allow_html=True)
    date_value = st.date_input("Select a date", key="date_input")
    st.markdown("</div>", unsafe_allow_html=True)

# Time Input
with st.container():
    st.markdown("<div class='container-title'>Time Input</div>", unsafe_allow_html=True)
    time_value = st.time_input("Select a time", key="time_input")
    st.markdown("</div>", unsafe_allow_html=True)

# ================================
# 3. File Upload and Display
# ================================

# File Uploader
with st.container():
    st.markdown("<div class='container-title'>File Uploader</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a file", key="file_uploader")
    st.markdown("</div>", unsafe_allow_html=True)

# ================================
# 4. Feedback and Visualization Components
# ================================

# Progress Bar
with st.container():
    st.markdown("<div class='container-title'>Progress Bar</div>", unsafe_allow_html=True)
    progress = st.progress(50)  # Example: 50%
    st.markdown("</div>", unsafe_allow_html=True)

# Metric
with st.container():
    st.markdown("<div class='container-title'>Metric</div>", unsafe_allow_html=True)
    st.metric("Sales", "150", delta="5%")
    st.markdown("</div>", unsafe_allow_html=True)

# DataFrame
df = pd.DataFrame({
    "Column 1": [1, 2, 3],
    "Column 2": [4, 5, 6]
})
with st.container():
    st.markdown("<div class='container-title'>DataFrame</div>", unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown("</div>", unsafe_allow_html=True)

# Code Display
with st.container():
    st.markdown("<div class='container-title'>Example Code</div>", unsafe_allow_html=True)
    st.code("print('Hello, world!')", language='python')
    st.markdown("</div>", unsafe_allow_html=True)

# Download Button
with st.container():
    st.markdown("<div class='container-title'>Download Button</div>", unsafe_allow_html=True)
    st.download_button("Download Data", data="File content", file_name="data.txt")
    st.markdown("</div>", unsafe_allow_html=True)

# ================================
# 5. Final Action Button
# ================================
with st.container():
    if st.button("Submit Data"):
        st.success(
            f"**Name:** {name}\n\n"
            f"**Comment:** {comment}\n\n"
            f"**Number:** {number_value}\n\n"
            f"**Slider Value:** {slider_value}\n\n"
            f"**Date:** {date_value}\n\n"
            f"**Time:** {time_value}\n\n"
            f"**Terms Accepted:** {accept_terms}\n\n"
            f"**Radio:** {option}\n\n"
            f"**SelectBox:** {select_option}\n\n"
            f"**MultiSelect:** {multi_options}"
        )
    st.markdown("</div>", unsafe_allow_html=True)
