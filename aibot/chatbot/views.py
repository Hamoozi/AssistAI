from django.shortcuts import render
from django.http import JsonResponse
import openai

#API Key hidden for privacy, get key from https://platform.openai.com/docs/api-reference


openai_api_key =  'YOURAPIKEY'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        prompt = message,
        max_tokens=150,
        stop = None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
