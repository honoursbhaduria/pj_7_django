from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator

# Create your views here.
def home(request):
    if request.method == 'POST':
        text = request.POST['translate']
        language = request.POST['language']
        translator = Translator(to_lang=language)  # using the translate package in this which help to translate text hehebeeheheheheheh
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request, 'main/index.html')

    