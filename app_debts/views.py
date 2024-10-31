from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializer import *


@api_view(['GET', 'POST'])
@permission_required(IsAuthenticated)
def debts_view(request):
    if request.method == 'GET':
        debts = DebtModel.objects.all(user=request.user)
        page = request.query_params.get('page', 1)
        paginator = request.query_params.get('paginator', 10)
        search = request.query_params.get('search', None)
        if page is not None:
            debts = debts[(int(page) - 1) * int(paginator):int(page) * int(paginator)]
        if search is not None:
            debts = debts.filter(description__icontains=search)
        serializer = DebtSerializer(debts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        data['user'] = request.user.id
        serializer = DebtSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Debt added successfully"})


@api_view(['GET', 'POST'])
@permission_required(IsAuthenticated)
def get_my_borrowed_view(request):
    if request.method == 'GET':
        debts = DebtModel.objects.filter(user=request.user, debt_type='borrowed')
        page = request.query_params.get('page', 1)
        paginator = request.query_params.get('paginator', 10)
        search = request.query_params.get('search', None)
        if page is not None:
            debts = debts[(int(page) - 1) * int(paginator):int(page) * int(paginator)]
        if search is not None:
            debts = debts.filter(description__icontains=search)
        serializer = DebtSerializer(debts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        data['user'] = request.user.id
        data['debt_type'] = 'borrowed'
        serializer = DebtSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Debt added successfully"})


@api_view(['GET'])
@permission_required(IsAuthenticated)
def get_my_lent_view(request):
    if request.method == 'GET':
        debts = DebtModel.objects.filter(user=request.user, debt_type='lent')
        serializer = DebtSerializer(debts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        data['user'] = request.user.id
        data['debt_type'] = 'lent'
        serializer = DebtSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Debt added successfully"})


@api_view(['GET'])
@permission_required(IsAuthenticated)
def inactivate_debt_view(request, pk):
    debt = DebtModel.objects.get(id=pk)
    debt.status = False
    debt.save()
    return Response({"message": "Debt inactivated successfully"})
