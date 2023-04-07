from django.shortcuts import render
from django.http import JsonResponse
from .models import Company, Vacancy

def getCompaniesList(request):
    data = Company.objects.all()
    list = [
        {
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'city': i.city,
            'address': i.address
        } for i in data
    ]
    return JsonResponse(data=list, safe=False)

def getCompanyByID(request, **kwargs):
    company = Company.objects.get(id=int(kwargs['id']))
    data = [
        {
            'id': company.id,
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address
        }
    ]
    return JsonResponse(data=data, safe=False)

def getVacancyList(request):
    data = Vacancy.objects.all()
    list = [
        {
            'id': i.id,
            'description': i.description,
            'salary': i.salary,
            'company': i.company.name
        } for i in data
    ]
    return JsonResponse(data=list, safe=False)

def getVacancyByID(request, **kwargs):
    vacancy = Vacancy.objects.get(id=int(kwargs['id']))
    data = [
        {
            'id': vacancy.id,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company': vacancy.company.name
        }
    ]
    return JsonResponse(data=data, safe=False)

def getVacanciesByCompany(request, **kwargs):
    vacancy = Vacancy.objects.filter(company_id=int(kwargs['id']))
    data = [
        {
            'id': i.id,
            'description': i.description,
            'salary': i.salary,
            'company': i.company.name
        } for i in vacancy
    ]

    return JsonResponse(data=data, safe=False)

def topTenVacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = [{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'salary': i.salary,
        'company': i.company.name
    } for i in vacancies]

    return JsonResponse(data=data, safe=False)
