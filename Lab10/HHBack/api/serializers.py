from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, valid_data):
        company = Company.objects.create(id=valid_data.get('id'), name=valid_data.get('name'),
                                         description=valid_data.get('description'), city=valid_data.get('city'),
                                         address=valid_data.get('address'))
        return company

    def update(self, instance, valid_data):
        setattr(instance, 'name', valid_data['name'])
        setattr(instance, 'description', valid_data['description'])
        setattr(instance, 'city', valid_data['city'])
        setattr(instance, 'address', valid_data['address'])
        instance.save()
        return instance

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('name', 'description', 'salary', 'company')