import requests
from search_results import scrape_google_results
import streamlit as st
from config import url,model,llm_api
def get_response_from_llm(endpoint,model,system_prompt,user_prompt,pplx_api,gr_only=False):
    """
    Input:
    endpoint : the endpoint to be queried for response
    model: model to be used 
    system_prompt: system prompt
    user_prompt: user prompt
    pplx_api: api provided by perplexity
    gr_only:generated response only True or False

    Output:
    response: response string or generated response
    """
    payload = {
        "model": f"{model}",
        "messages": [
            {
                "role": "system",
                "content": f"{system_prompt}"
            },
            {
                "role": "user",
                "content": f"{user_prompt}"
            }
        ],
        "max_tokens": 8000
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {pplx_api}"
    }
    response = requests.post(endpoint, json=payload, headers=headers)

    if gr_only:
        response = eval(response.text)['choices'][0]['message']['content']

    return response

def user_prompt_generate(topic):
    data = scrape_google_results(f"What to learn in {topic}?")
    google_data = [d['content'][:4000] for d in data]
    user_prompt = f"""I want to learn about {topic}.\n<google_search_data>{google_data}</google_search_data>"""
    return google_data,user_prompt

def generate_content_on_subtopic(subtopic):
    scraped_data = scrape_google_results(subtopic)
    google_data = [d['content'][:4000] for d in scraped_data]
    system_prompt = "Write about the topic in well formatted form including linebreaks. The writing should be entertaining and informative. Not more than 10 context focused paragraphs. Use the given Google search data to provide a factual answer"
    user_prompt = f"Google scraped data:{google_data}"
    subtopic_llm_generated_info = get_response_from_llm(url,model,system_prompt,user_prompt,llm_api,gr_only=True)
    return subtopic_llm_generated_info


def generate_and_display_about_subtopic(subtopic):
    subctopic_generated_info = generate_content_on_subtopic(subtopic)
    st.subheader(subtopic)
    st.write(subctopic_generated_info)