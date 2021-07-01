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

# def fantlab_index(request):
#     with open('/home/ara/python/Django_project/fantlab/data.json', 'r') as js:
#         json_file = json.load(js)
#     paginator = Paginator(json_file['items'], 20)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'fantlab/fantlab_list.html', {
#         'list': page_obj,
#     })



def fantlab_index(request):
    with open('fantlab/data.json', 'r') as js:
        json_file = json.load(js)

    new_dic = {}
    base = json.loads(get('https://api.fantlab.ru/user/50656/marks?page=1&sort=date&type=novel').text)
    works_list = base['items']
    for work in works_list:
        work_id = str(work['work_id'])
        if work_id not in json_file:
            work_base = json.loads(get(f'https://api.fantlab.ru/work/{work_id}').text)
            work_description = work_base['work_description']
            di = {work_id: {
                    "work_author": work["work_author"],
                    "work_image": work["work_image"],
                    "work_name": work["work_name"],
                    "work_type": work["work_type"],
                    "work_year": work["work_year"],
                    "work_anotation": work_description,
                    "mark": work["mark"],
                    "mark_date": work["mark_date"]
                }}
            new_dic.update(di)
    if new_dic:
        new_dic.update(json_file)
        with open('fantlab/data.json', 'w', encoding='utf-8') as f:
            json.dump(new_dic, f, indent=4)
    new_dic.update(json_file)

    book_list = []
    for book_info in new_dic.values():
        book_list.append(book_info)
    paginator = Paginator(book_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'fantlab/fantlab_list.html', {
        'list': page_obj,
    })
