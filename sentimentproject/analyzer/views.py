from django.shortcuts import render
from textblob import TextBlob

def home(request):
    result = ""

    if request.method == "POST":
        text = request.POST.get("text")

        analysis = TextBlob(text)

        if analysis.sentiment.polarity > 0:
            result = "Positive 😊"
        elif analysis.sentiment.polarity < 0:
            result = "Negative 😞"
        else:
            result = "Neutral 😐"

    return render(request, "home.html", {"result": result})