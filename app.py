import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Writing Workshop",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'welcome'

# Navigation function
def navigate_to(page_name):
    st.session_state['page'] = page_name
    st.experimental_rerun()

# Main function to control page navigation
def main():
    page = st.session_state['page']
    if page == 'welcome':
        import pages.welcome as welcome
        welcome.show(navigate_to)
    elif page == 'write_article':
        import pages.write_article as write_article
        write_article.show(navigate_to)
    elif page == 'completion':
        import pages.completion as completion
        completion.show(navigate_to)
    else:
        st.error("Page not found")

if __name__ == "__main__":
    main()
