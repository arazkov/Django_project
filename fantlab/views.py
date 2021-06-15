from django.shortcuts import render
from requests import get
import json
from django.core.paginator import Paginator


# def fantlab_index(request):
#     base = json.loads(get('https://api.fantlab.ru/user/50656/marks?page=1&sort=date&type=novel').text)
#     works_list = base['items']
#     for work in works_list:
#         work_id = work['work_id']
#         work_base = json.loads(get(f'https://api.fantlab.ru/work/{work_id}').text)
#         work_description = work_base['work_description']
#         work['anotation'] = work_description
#     paginator = Paginator(works_list, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'fantlab/fantlab_list.html', {
#         'list': page_obj,
#     })

def fantlab_index(request):
    with open('/home/ara/python/Django_project/fantlab/data.json', 'r') as js:
        json_file = json.load(js)
    paginator = Paginator(json_file['items'], 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fantlab/fantlab_list.html', {
        'list': page_obj,
    })
