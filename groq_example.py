import requests

api_key = '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'

# Set up headers for authorization
headers = {'Authorization': f'Bearer {api_key}'}

instruction = "Be a psychologist"

question = 'Who is founding father of psychology?'

# Data for the request
data = {
    "model": "llama-3.1-8b-instant",  # You can change the model if needed
    "messages": [{"role": "system", "content": instruction},
                 {"role": "user", "content": question}]
}

# Make the POST request to GroqCloud API
response = requests.post(
    'https://api.groq.com/openai/v1/chat/completions',
    headers=headers,
    json=data
)

# Check if the response is successful and print the model's response
if response.status_code == 200:
    response_data = response.json()
    # Extract and print the assistant's message
    message = response_data['choices'][0]['message']['content']
    print(message)
else:
    print("Error:", response.status_code, response.text)