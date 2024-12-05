from llm_funcs import user_prompt_generate,get_response_from_llm
from config import url,model,llm_api,course_generate_prompt
from processing import section_splitting,subtopic_splitting

def course_outline_generate(topic):
    _,user_prompt = user_prompt_generate(topic)
    course = get_response_from_llm(url,model,course_generate_prompt,user_prompt,llm_api,gr_only=True)

    section_split = section_splitting(course)

    topic_subtopics_dict = {}
    for section in section_split:
        topic = section.split('\n')[0]
        subtopics = subtopic_splitting(section)
        topic_subtopics_dict[topic] = subtopics

    return topic_subtopics_dict