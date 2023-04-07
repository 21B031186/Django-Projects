from django.urls import path
from . import views
urlpatterns = [
    path('companies/', views.getCompaniesList),
    path('companies/<int:id>/', views.getCompanyByID),
    path('vacancies/', views.getVacancyList),
    path('vacancies/<int:id>/', views.getVacancyByID),
    path('companies/<int:id>/vacancies/', views.getVacanciesByCompany),
    path('vacancies/top_ten/', views.topTenVacancies),
]