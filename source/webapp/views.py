from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

import json


class Operation:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AddView(View):
    def post(self, request, *args, **kwargs):
        if request.body:
            data = json.loads(request.body)
            op = Operation(**data)
            print(op.first, op.second)
        return JsonResponse([{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'test2'}], safe=False)


class SubtractView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse([{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'test2'}], safe=False)


class MultiplyView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse([{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'test2'}], safe=False)


class DivideView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse([{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'test2'}], safe=False)
