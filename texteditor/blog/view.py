from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")

# I have created this file - Harry
def analyze(request):
    #Get the text
    text = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    smallcaps = request.POST.get('smallcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        text = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text = analyzed
    if(smallcaps=="on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.lower()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        text = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
    