from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Article


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        view_article_text = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')
    latest_coment_list = view_article_text.coment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'view_article_text': view_article_text,
                                                    'latest_coment_list': latest_coment_list,
                                                    })


def leave_comment(request, article_id):
    try:
        view_article_text = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')
    view_article_text.coment_set.create(coment_autor=request.POST["name"], coment_text=request.POST["text"])
    return HttpResponseRedirect(reverse('articles:detail', args=(view_article_text.id,)))