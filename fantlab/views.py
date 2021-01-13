from django.shortcuts import render
from requests import get
import requests, json


def fantlab_index(request):
    base = json.loads(get('https://api.fantlab.ru/user/50656/marks?page=1&sort=date&type=novel').text)
    works_list = base['items']
    work_id = base['items'][0]['work_id']
    work_base = json.loads(get(f'https://api.fantlab.ru/work/{work_id}').text)
    work_description = work_base['work_description']
    #print(autor_name)
    return render(request, 'fantlab/fantlab_list.html', {
        'ano' : work_description[:150],
        'list' : works_list,
        })
