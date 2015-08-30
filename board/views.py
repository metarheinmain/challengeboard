from django.shortcuts import render, get_object_or_404
from .models import Challenge
import markdown

def index(request):
    ctx = {
        'challenges': Challenge.objects.all().order_by('datetime').prefetch_related('participants')
    }
    for c in ctx['challenges']:
        c.descr = markdown.markdown(c.description)
    return render(request, 'board/index.html', ctx)
