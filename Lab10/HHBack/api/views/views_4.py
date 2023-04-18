from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


class CompanyListAPIView(APIView):
    def get(self, req):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, req):
        data = json.loads(req.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer)


class CompanyVacanciesAPIView(APIView):
    def get(self, req, id=None):
        try:
            company = Company.objects.get(id=id)
            vacancies_json = Vacancy.objects.filter(company_id=int(id))
            serializer = VacancySerializer(vacancies_json, many=True)
        except Company.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        return Response(serializer.data)

    def post(self, req, id=None):
        data = json.loads(req.body)
        data['company'] = id
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "error"}, status=400)


class VacancyListAPIView(APIView):
    def get(self, req):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


class VacancyItemAPIView(APIView):
    def get(self, req, id=None):
        try:
            vacancy = Vacancy.objects.get(id=id)
            serializer = VacancySerializer(vacancy)
        except Vacancy.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        return Response(serializer.data)

    def put(self, req, id=None):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        data = json.loads(req.body)
        serializer_update = VacancySerializer(instance=vacancy, data=data)
        if serializer_update.is_valid():
            serializer_update.save()
            return Response(serializer_update.data)
        return Response(serializer_update.errors)

    def delete(self, req, id=None):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        vacancy.delete()
        return Response({"message": "vacancy deleted successfully"})


class TopVacancyAPIView(APIView):
    def get(self, req):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        sorted_vacs = sorted(serializer.data, key=lambda x: x["salary"], reverse=True)
        n = 10
        if len(sorted_vacs) < 10:
            n = len(sorted_vacs)
        sorted_vacs = sorted_vacs[0:n]
        return Response(sorted_vacs)


class CompanyItemAPIView(APIView):
    def get(self, req, id=None):
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
        except Company.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        return Response(serializer.data)

    def put(self, req, id=None):
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
        except Company.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        data = json.loads(req.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, req, id=None):
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
        except Company.DoesNotExist as e:
            return Response({"message": str(e)}, status=400)
        company.delete()
        return Response({"message": "company deleted successfully"})