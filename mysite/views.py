from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home_page/index.html') # in articles/tamplates
    # return HttpResponse("<h3><li><a href='http://127.0.0.1:8000/polls/'>polls</a></li></h3>\n"
    #                     "<h3><li><a href='http://127.0.0.1:8000/articles/'>articles</a></li></h3>\n"
                        # "<h2><li><a href='http://127.0.0.1:8000/admin/'>ADMIN</a></li></h2>")
