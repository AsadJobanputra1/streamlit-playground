import streamlit as st
import pandas as pd

# Custom CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #1c1f3b;
        color: white;
    }
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #2A9DF4;
        padding: 10px;
    }
    .container-box {
        background-color: #f7f9fc;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 1px solid #dedede;
    }
    .test-action {
        background-color: #2A9DF4;
        color: white;
        padding: 5px;
        border-radius: 5px;
        text-align: center;
        width: 100px;
        cursor: pointer;
        margin-top: 10px;
    }
    .table-header {
        font-weight: bold;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    td, th {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

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
