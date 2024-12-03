from django import forms
from django.core.exceptions import ValidationError
from .models import Loan_Data

class Loan_Data_Form(forms.Form):
  name = forms.CharField()
  age = forms.IntegerField()
  gender = forms.CharField()
  education = forms.CharField()
  income = forms.IntegerField()
  emp_exp = forms.IntegerField()
  loan_amount = forms.IntegerField()
  home_ownership = forms.CharField()
  loan_intent = forms.CharField()
  default = forms.CharField()
  loan_status = forms.CharField()