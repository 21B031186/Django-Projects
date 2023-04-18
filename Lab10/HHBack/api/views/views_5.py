from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
import json


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = (IsAuthenticated,)


class CompanyItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'
    # permission_classes = (IsAuthenticated,)


class CompanyVacanciesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

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


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = 'id'


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
