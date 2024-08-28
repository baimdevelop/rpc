import requests

# Ganti dengan kunci API Anda
API_KEY = 'YOUR_API_KEY_HERE'

# Ganti dengan URL endpoint API Gemini
API_URL = 'https://api.gemini.ai/v1/ask'

def query_ai_gemini(question):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'question': question
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.text}

# Contoh penggunaan
if __name__ == '__main__':
    question = 'Apa itu AI Gemini?'
    result = query_ai_gemini(question)
    print(result)
