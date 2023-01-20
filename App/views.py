from django.shortcuts import render
from django.views.generic import FormView
from App.forms import *
from django.http import HttpResponse
from App.models import *
# Create your views here.
class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=nameform
    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))
    
class CBV_ModelForm(FormView):
    template_name='CBV_ModelForm.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('Data Submitted Successfully')