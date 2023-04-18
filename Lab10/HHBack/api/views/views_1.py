from django.shortcuts import render
from django.http import JsonResponse
from api.models import Company, Vacancy

def getCompaniesList(request):
    data = Company.objects.all()
    companies_json = [company.to_json() for company in data]
    return JsonResponse(companies_json, safe=False)

def getCompanyByID(request, **kwargs):
    try:
        company = Company.objects.get(id=int(kwargs['id']))
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(company.to_json(), safe=False)

def getVacancyList(request):
    data = Vacancy.objects.all()
    vacancy_json = [vacancy.to_json() for vacancy in data]
    return JsonResponse(vacancy_json, safe=False)

def getVacancyByID(request, **kwargs):
    try:
        vacancy = Vacancy.objects.get(id=int(kwargs['id']))
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json(), safe=False)

def getVacanciesByCompany(request, **kwargs):
    data = Vacancy.objects.filter(company_id=int(kwargs['id']))
    vacancy_json = [vacancy.to_json() for vacancy in data]

    return JsonResponse(vacancy_json, safe=False)

def topTenVacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]

    return JsonResponse(vacancy_json, safe=False)