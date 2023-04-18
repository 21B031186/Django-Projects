from django.urls import path
from api.views import CompanyListAPIView, CompanyVacanciesAPIView,VacancyItemAPIView,VacancyListAPIView, TopVacancyAPIView, CompanyItemAPIView

# urlpatterns = [
#     path('companies/', views.getCompaniesList),
#     path('companies/<int:id>/', views.getCompanyByID),
#     path('vacancies/', views.getVacancyList),
#     path('vacancies/<int:id>/', views.getVacancyByID),
#     path('companies/<int:id>/vacancies/', views.getVacanciesByCompany),
#     path('vacancies/top_ten/', views.topTenVacancies),
# ]

urlpatterns = [
    path('companies/',CompanyListAPIView.as_view() ),
    path('companies/<int:id>/', CompanyItemAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>/', VacancyItemAPIView.as_view()),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view()),
    path('vacancies/top_ten/', TopVacancyAPIView.as_view()),
]