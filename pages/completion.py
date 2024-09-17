import streamlit as st

def show(navigate_to):
    st.title("Your Article")

    # Retrieve the stored inputs
    title = st.session_state.get('title', '')
    objective = st.session_state.get('objective', '')
    target_audience = st.session_state.get('target_audience', '')
    key_points = st.session_state.get('key_points', '')

    # Layout columns for article and summary
    col1, col2 = st.columns(2)

    with col1:
        # Display the generated article
        st.subheader(title)
        st.write(f"**Objective:** {objective}")
        st.write(f"**Target Audience:** {target_audience}")
        st.write("**Article:**")
        # For demonstration, we simply format the key points as bullet points
        article = key_points.replace('-', '•')
        st.write(article)

    with col2:
        # Display a summary of the inputs
        st.subheader("Summary")
        st.write(f"**Title:** {title}")
        st.write(f"**Objective:** {objective}")
        st.write(f"**Target Audience:** {target_audience}")
        st.write("**Key Points:**")
        st.write(key_points)
