import streamlit as st
from course_generate import course_outline_generate
from llm_funcs import generate_and_display_about_subtopic
from processing import populate_sidebar
def main():
    st.set_page_config(page_title="AI Based Course Generation", page_icon=":mortar_board:", layout="wide")
    
    st.title("AI Based Course Generation")
    
    # Sidebar
    st.sidebar.header("Course Outline")
    # Main content
    
    st.header("Welcome to AI Based Course Generation!")
    st.write("This app helps you generate course content using AI.")
    
    # Add your main functionality here
    
    # Example input form
    with st.form(key='course_form'):
        course_topic = st.text_input("Course Topic")
        # course_description = st.text_area("Course Description")
        submit_button = st.form_submit_button(label='Generate Course')
    
    if submit_button:
        st.session_state.outline = course_outline_generate(course_topic)
        # topic_buttons, subtopic_buttons = populate_sidebar(outline)

    if 'outline' in st.session_state:
        topic_buttons = {}
        subtopic_buttons = {}

        st.sidebar.title("Course Topics")
        for topic, subtopics in st.session_state.outline.items():
            topic_buttons[topic] = st.sidebar.button(topic)

            with st.sidebar.expander(topic):
                for subtopic in subtopics:
                    unique_key = f"{topic}_{subtopic}"
                    subtopic_buttons[subtopic] = st.button(subtopic, key=unique_key)
                    
    # Process the input and generate the course content
    if 'outline' in st.session_state:
        st.subheader("Generated Course Content")
        
        # Check if any subtopic button is pressed
        for subtopic in subtopic_buttons:
            if subtopic_buttons[subtopic]:
                # Generate and display content about the selected subtopic in the main content area
                generate_and_display_about_subtopic(subtopic)
                    
if __name__ == '__main__':
    main()