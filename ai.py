import openai

# API key bawaan
api_key = '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'
openai.api_key = api_key

# Minta prompt dari pengguna
prompt_text = input("Masukkan prompt untuk OpenAI: ")

# Buat permintaan ke API OpenAI
response = openai.Completion.create(
    engine="text-davinci-003",  # Anda bisa mengganti model sesuai kebutuhan
    prompt=prompt_text,
    max_tokens=50
)

# Tampilkan respons
print("Respons dari OpenAI:")
print(response.choices[0].text.strip())
