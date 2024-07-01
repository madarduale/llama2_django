# views.py
from django.shortcuts import render
import requests
import json
import ollama
def index(request):
    return render(request, 'index.html')

def ask_question(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        llama_response = send_question_to_llama(question)
        if llama_response is not None:
            return render(request, 'index.html', {'response': llama_response['message']['content']})
        else:
            return render(request, 'error.html', {'message': 'Invalid response from Llama 2'})
    return render(request, 'index.html')

def send_question_to_llama(question):
    
    response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': question,
    },
    ])
    print(response)
    print(response['message']['content'])
    # try:
    #     response_json = response.json()
    #     return response_json.get('response')
    # except json.JSONDecodeError as e:
    #     print("JSONDecodeError:", e)
    #     print("Response content:", response.content)
    #     return None
    return response
