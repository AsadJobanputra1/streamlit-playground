import streamlit as st

def show(navigate_to):
    st.title("Create Your Article")

    # Input fields with sample text
    title = st.text_input("Title", "The Future of AI in Education")
    objective = st.text_input("Objective", "To inform about AI advancements in educational settings")
    target_audience = st.text_input("Target Audience", "CIO at a university")
    key_points = st.text_area(
        "Key Points",
        "- AI integration in classrooms\n- Personalized learning\n- Data analytics for student performance"
    )

    # Next button to navigate to the completion screen
    if st.button('Next'):
        # Save the inputs to the session state
        st.session_state['title'] = title
        st.session_state['objective'] = objective
        st.session_state['target_audience'] = target_audience
        st.session_state['key_points'] = key_points
        navigate_to('completion')
