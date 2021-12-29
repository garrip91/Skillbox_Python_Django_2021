from django.shortcuts import render

from .models import Vacancy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required



# Create your views here:
@permission_required('app_employment.view_vacancy')
def vacancy_list(request):

    vacancies = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})