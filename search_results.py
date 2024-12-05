from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time

def get_top_30_results(query):
    results = []
    for j in search(query, num_results=30):
        results.append(j)
    return results

def scrape_google_results(query,verbose = 0):
    # Get the top 30 search result links
    search_links = get_top_30_results(query)
    
    # Extract data from each search result link
    results = []
    for link in search_links:
        try:
            # Send a GET request to the search result link with a timeout of 2 seconds
            response = requests.get(link, timeout=2)
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract the title
            title = soup.find("title").text.strip()
            
            # Extract the main content (you may need to adjust this based on the website structure)
            main_content = ""
            for paragraph in soup.find_all("p"):
                main_content += paragraph.get_text().strip() + "\n"
            
            # Append the extracted data to the results list
            results.append({
                "title": title,
                "url": link,
                "content": main_content
            })
            if verbose>=2:
                print(f"Extracted from {link}, Title: {title}, content:{main_content}")
            # Break the loop if we have collected data from 10 websites
            if len(results) >= 5:
                break
            
            # Add a short delay of 0.5 seconds between each request to avoid overwhelming the websites
            time.sleep(0.5)
        except Exception as e:
            if verbose>=1:
                print(f"Error scraping {link}, skipping")
    
    return results
