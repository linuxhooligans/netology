from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework import viewsets, status, permissions
import logging
from django_tables2.views import SingleTableMixin
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from candydendy.models import Candy

from rest_framework.views import APIView
from candydendy.serializers import CandySerializerFull, CandySerializerFree
from candydendy.tables import CandyTable, CandyTableFree

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "form/home.html", {})


def contact(request):
    return render(request, "form/contact.html", {})

@login_required(login_url='/login/')
def candy(request):
    table = CandyTable(
        Candy.objects.all(),
        attrs={"class": "table table-borderless"}
    )
    return render(request, "form/candyfree.html", {
        "table": table
    })

def candyfree(request):
    table = CandyTableFree(
        Candy.objects.all(),
        attrs={"class": "table table-borderless"}
    )
    return render(request, "form/candyfree.html", {
        "table": table
    })


# class CandyListView(SingleTableView):
#     model = Candy
#     exclude = ("company_country","company_address")
#     template_name = 'form/candyfree.html'

class CandyViewSetFree(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        # candys = Candy.objects.all()
        candys = Candy.objects.filter()
        serializer = CandySerializerFree(candys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CandyViewSet(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # candys = Candy.objects.all()
        candys = Candy.objects.filter()
        serializer = CandySerializerFull(candys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'company': request.data.get('company'),
            'company_country': request.data.get('company_country'),
            'company_address': request.data.get('company_address'),
            'company_site': request.data.get('company_site'),
            'company_email': request.data.get('company_email'),
            'company_phone_number': request.data.get('company_phone_number'),
            'company_director': request.data.get('company_director'),
            'pricetag': request.data.get('pricetag'),
            'fats': request.data.get('fats'),
            'carbohydrates': request.data.get('carbohydrates'),
            'protein': request.data.get('protein'),
            'calories': request.data.get('calories'),
            'type': request.data.get('type'),
            'rating': request.data.get('rating'),
        }
        serializer = CandySerializerFull(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('candy')
    else:
        form = UserCreationForm()
    return render(request, 'form/register.html', {'form': form})