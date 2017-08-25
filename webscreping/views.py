from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
from django.http import JsonResponse


def home(request):
    pprint("a")
    return render(request, 'index.html', {})

def data(request):
    data = request.GET.get('data', 'name')
    r = requests.get(data)
    data = r.text

    main = BeautifulSoup(data)
    all_data = {}
    z = []
    b = []
    c = []
    d = []
    for a in main.find_all("meta"):

        if a.get('name') ==  "title" :
            z.append(a.get('content'))
        elif a.get('name') == "description":
            b.append(a.get('content'))
            pprint(b)
        elif a.get('itemprop') == "thumbnailUrl":
            c.append(a.get('content'))
        elif a.get('name') == "author":
            d.append(a.get('content'))

    all_data['Title'] = z
    all_data['Description'] = b
    all_data['Thumbnails'] = c
    all_data['Author'] = d
    # return render(request, 'detail.html', {'data': data, 'all_data': all_data})
    return JsonResponse(all_data)