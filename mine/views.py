from django.shortcuts import render
from django.http import HttpResponse
from . models import Article

# Create your views here.
def home(request):

    articles=Article.objects.all()

    context={'articles': articles}

    return render(request, 'mine/index.html',context=context)

def singuler_article(request,pk):
    
    article=Article.objects.get(id=pk)

    content={'article':article}

    return render(request, 'mine/article.html',context=content)