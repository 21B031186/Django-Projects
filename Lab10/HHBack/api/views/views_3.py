from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from api.models import Company,Vacancy
from api.serializers import CompanySerializer,VacancySerializer
from django.http.response import JsonResponse

@api_view(['GET', 'POST'])
def companies_list(req):
    if req.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        data = json.loads(req.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer)

@api_view(['GET', 'POST'])
def company_vacancy(req,id):
    try:
        company = Company.objects.get(id=id)
        vacancies_json = Vacancy.objects.filter(company_id=int(id))
        serializer = VacancySerializer(vacancies_json, many=True)
    except Company.DoesNotExist as e:
        return Response({"message": str(e)}, status=400)
    if req.method == 'GET':
        return Response(serializer.data )
    elif req.method == 'POST':
        data = json.loads(req.body)
        data['company'] = id
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message":"error"}, status=400)

@api_view(['GET', 'DELETE', 'PUT'])
def get_company(req, id):
    try:
        company = Company.objects.get(id=id)
        serializer = CompanySerializer(company)
    except Company.DoesNotExist as e:
        return Response({"message": str(e)}, status=400)
    if req.method == 'GET':
        return Response(serializer.data)
    elif req.method == 'PUT':
        data = json.loads(req.body)
        serializer = CompanySerializer(instance=company,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif req.method == 'DELETE':
        company.delete()
        return Response({"message": "company deleted successfully"})

@api_view(['GET',])
def vacancy_list(req):
    if req.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def get_vacancy(req,id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        serializer = VacancySerializer(vacancy)
    except Vacancy.DoesNotExist as e:
        return Response({"message": str(e)}, status=400)
    if req.method == 'GET':
        return Response(serializer.data)
    elif req.method == 'PUT':
        data = json.loads(req.body)
        serializer_update = VacancySerializer(instance = vacancy,data=data)
        if serializer_update.is_valid():
            serializer_update.save()
            return Response(serializer_update.data)
        return Response(serializer_update.errors)
    elif req.method == 'DELETE':
        vacancy.delete()
        return Response({"message": "vacancy deleted successfully"})
@api_view(['GET',])
def top_vacancy(req):
    if req.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        sorted_vacs = sorted(serializer.data, key=lambda x: x["salary"], reverse=True)
        n = 10
        if len(sorted_vacs) < 10:
            n = len(sorted_vacs)
        sorted_vacs = sorted_vacs[0:n]
        return Response(sorted_vacs)