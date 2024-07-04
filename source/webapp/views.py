from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

import json

from .operation import Operand, Operation, OperationTypes


def operation_helper(body, type):
    if body:
        data = json.loads(body)
        first = Operand(data['first'])
        second = Operand(data['second'])
        if first.check_validity() and second.check_validity():
            operation = Operation(first, second, type)
            return JsonResponse({'amount': operation.get_result(), 'is_error': False}, safe=False)
        else:
            return JsonResponse({'amount': 'No numbers in data', 'is_error': True}, safe=False, status=400)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AddView(View):
    def post(self, request, *args, **kwargs):
        return operation_helper(request.body, OperationTypes.add)


class SubtractView(View):
    def post(self, request, *args, **kwargs):
        return operation_helper(request.body, OperationTypes.subtract)


class MultiplyView(View):
    def post(self, request, *args, **kwargs):
        return operation_helper(request.body, OperationTypes.multiply)


class DivideView(View):
    def post(self, request, *args, **kwargs):
        return operation_helper(request.body, OperationTypes.divide)
