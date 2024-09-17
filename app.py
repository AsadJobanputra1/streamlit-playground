import streamlit as st
import pandas as pd
import os

# Load external CSS file
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css('styles.css')

# Sidebar
st.sidebar.title("GoTestPro")
st.sidebar.markdown("### Projects")
st.sidebar.markdown("- Tests")
st.sidebar.markdown("- Executions")
st.sidebar.markdown("- Results")
st.sidebar.markdown("- Dashboard")
st.sidebar.markdown("- Users")
st.sidebar.markdown("---")
st.sidebar.markdown("### Project Settings")
st.sidebar.markdown("- Page Elements")
st.sidebar.markdown("- Configuration")

# Main header
st.markdown("<div class='main-header'>Manage Test</div>", unsafe_allow_html=True)

# Test details container
st.markdown("""
<div class='container-box'>
    <p><strong>Test Name:</strong> Name_01</p>
    <p><strong>Description:</strong> Lorem Ipsum has been the industry standard since the 1500s.</p>
    <p><strong>Created On:</strong> 2023-06-23, 13:20:05</p>
    <p><strong>Platform:</strong> Windows 8.1</p>
    <p><strong>Browser:</strong> Chrome</p>
</div>
""", unsafe_allow_html=True)

# Test steps table
st.markdown("<h3>Steps</h3>", unsafe_allow_html=True)

# Create a table for test steps
data = {
    "Step": ["Open App", "Click", "Click", "Send Keys", "Assert Element Present", "Click"],
    "Page Name": ["Something"] * 6,
    "Element Name": ["Test Demo"] * 6,
    "Locator ID": ["Something"] * 6,
    "Locator Type": ["URL"] * 6,
    "Locator Value": ["https://www.flipkart.com"] * 6
}

df = pd.DataFrame(data)

# Display the table
st.table(df)

# Action buttons
st.markdown("<div class='test-action'>Run</div>", unsafe_allow_html=True)
st.markdown("<div class='test-action'>Delete</div>", unsafe_allow_html=True)
