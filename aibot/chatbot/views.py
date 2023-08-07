from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003"
        prompt = message
        max_tokens=150,
        stop = None,
        temperature=0.7,


    )
    print(response)
    answer = response.choice[0].text.strip()


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        #This will be replaced by api responce in the future
        response = 'I\'m doing great! How about you?'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')