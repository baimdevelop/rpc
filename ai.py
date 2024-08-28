import openai

# API key bawaan
api_key = 'sk-d2sBeA0BxoQ2EqD-zEN0zOw84NdKJ6TAUVVOu1IgsNT3BlbkFJDBOA83Dg_grqDRKrtlb7LL0vsFrLggahNTSXbdCJ4A'
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
