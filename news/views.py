from django.shortcuts import render


from .models import News

def news(request):
    all_news = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'news': all_news})

# Create your views here.
