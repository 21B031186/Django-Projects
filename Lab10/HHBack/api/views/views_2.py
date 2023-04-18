import json
from django.http import HttpRequest
from api.models import Company, Vacancy
from django.views import View
from api.serializers import CompanySerializer, VacancySerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getCompaniesList(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer, safe=False)

@csrf_exempt
def getCompanyById(req, **kwargs):
    try:
        company = Company.objects.get(id=int(kwargs['id']))
        serializer = CompanySerializer(company)
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=400)
    if req.method == 'GET':
        return JsonResponse(serializer.data)
    elif req.method == 'PUT':
        data = json.loads(req.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif req.method == 'DELETE':
        company.delete()
        return JsonResponse({"message": "company deleted successfully"})

@csrf_exempt
def getVacanciesByCompany(req, **kwargs):
    try:
        company = Company.objects.get(id=int(kwargs['id']))
        vacancies_json = Vacancy.objects.filter(company_id=int(id))
        serializer = VacancySerializer(vacancies_json, many=True)
    except Company.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=400)
    if req.method == 'GET':
        return JsonResponse(serializer.data, safe=False)
    elif req.method == 'POST':
        data = json.loads(req.body)
        data['company'] = id
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({"message":"error"}, status=400)

def getVacancyList(req):
    if req.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def getVacancyByID(req, **kwargs):
    try:
        vacancy = Vacancy.objects.get(id=int(kwargs['id']))
        serializer = VacancySerializer(vacancy)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({"message": str(e)}, status=400)
    if req.method == 'GET':
        return JsonResponse(serializer.data)
    elif req.method == 'PUT':
        data = json.loads(req.body)
        serializer_update = VacancySerializer(instance=vacancy, data=data)
        if serializer_update.is_valid():
            serializer_update.save()
            return JsonResponse(serializer_update.data)
        return JsonResponse(serializer_update.errors)
    elif req.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({"message": "vacancy deleted successfully"})

def topTenVacancies(req):
    if req.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        sorted_vacs = sorted(serializer.data, key=lambda x: x["salary"], reverse=True)
        n = 10
        if len(sorted_vacs) < 10:
            n = len(sorted_vacs)
        sorted_vacs = sorted_vacs[0:n]
        return JsonResponse(sorted_vacs, safe=False)