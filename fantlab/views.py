from django.shortcuts import render
from requests import get
import requests, json


def fantlab_index(request):
    base = json.loads(get('https://api.fantlab.ru/user/50656/marks?page=1&sort=date&type=novel').text)
    works_list = base['items']
    anotation = []
    for work in works_list:
        work_id = work['work_id']
        work_base = json.loads(get(f'https://api.fantlab.ru/work/{work_id}').text)
        work_description = work_base['work_description']
        anotation.append(work_description)
    
    
    
    return render(request, 'fantlab/fantlab_list.html', {
        'ano' : anotation[1],
        'list' : works_list,
        })
