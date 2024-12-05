import re
import streamlit as st
from llm_funcs import generate_and_display_about_subtopic
def section_splitting(response):
    bullet_regex = re.compile(r"^(\d+\..+?)(?=^\d+\.|\Z)", re.MULTILINE | re.DOTALL)

    bullet_points = bullet_regex.findall(response)
    return bullet_points

def subtopic_splitting(text):
    sub_point_regex = re.compile(r"^\s+(.+)", re.MULTILINE)
    sub_points = sub_point_regex.findall(text)
    return sub_points

def populate_sidebar(course_content):
    topic_buttons = {}
    subtopic_buttons = {}

    st.sidebar.title("Course Topics")
    for topic, subtopics in course_content.items():
        topic_buttons[topic] = st.sidebar.button(topic)

        with st.sidebar.expander(topic):
            for subtopic in subtopics:
                subtopic_buttons[subtopic] = st.button(subtopic, key=subtopic)  # Ensure unique keys for buttons

    return topic_buttons, subtopic_buttons

# def populate_sidebar(course_content):
#     # st.sidebar.title("Course Topics")
#     for topic, subtopics in course_content.items():
#         topic_button = st.sidebar.button(topic)
#         if topic_button:
#             st.header(topic)
#             # st.write("Content for the topic will be displayed here.")
        
#         with st.sidebar.expander(topic):
#             for subtopic in subtopics:
#                 subtopic_button = st.button(subtopic, key=subtopic)  # Ensure unique keys for buttons
#                 if subtopic_button:
#                     generate_and_display_about_subtopic(subtopic)
#                     # st.subheader(subtopic)
#                     # st.write(f"Content for {subtopic} will be displayed here.")
