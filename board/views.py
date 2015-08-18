from django.shortcuts import render, get_object_or_404
from .models import Challenge
import markdown

def index(request):
    ctx = {
        'challenges': Challenge.objects.all().order_by('-id')
    }
    return render(request, 'board/index.html', ctx)


def detail(request, id):
    challenge = get_object_or_404(Challenge, id=id)
    descr = markdown.markdown(challenge.description)
    ctx = {
        'challenge': challenge,
        'descr': descr,
        'highscore': challenge.get_highscore()
    }
    return render(request, 'board/detail.html', ctx)
