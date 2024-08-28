import requests
from bs4 import BeautifulSoup
import json

def search_and_scrape(query, num_results=10):
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    # Lakukan request ke Google Search
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Ekstrak link dari hasil pencarian
        search_results = []
        for g in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
            title = g.get_text()
            link = g.find_parent('a')['href']
            search_results.append({"title": title, "link": link})
        
        return search_results
    else:
        print(f"Error: {response.status_code}")
        return None

def summarize_page_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ekstrak semua teks dari paragraf di halaman
        paragraphs = soup.find_all('p')
        page_text = ' '.join([para.get_text() for para in paragraphs])
        
        # Untuk saat ini, kita hanya return beberapa kalimat pertama sebagai ringkasan sederhana
        summary = '. '.join(page_text.split('. ')[:2])
        return summary
    
    except Exception as e:
        print(f"Failed to fetch or summarize content from {url}: {e}")
        return None

def save_to_json(data, filename="data.json"):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    query = "Teknologi terbaru dalam AI"  # Contoh query pencarian
    search_results = search_and_scrape(query)
    
    if search_results:
        summarized_data = []
        for result in search_results:
            summary = summarize_page_content(result['link'])
            if summary:
                summarized_data.append({
                    "title": result['title'],
                    "link": result['link'],
                    "summary": summary
                })
        
        save_to_json(summarized_data)
        print(f"Data has been saved to data.json")
    else:
        print("No search results found or failed to scrape data.")
