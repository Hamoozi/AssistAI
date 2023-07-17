from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        #This will be replaced by api responce in the future
        response = "Response"
        return JsonResponse({'message' : message, 'response' : response})
    return render(request, 'chatbot.html')