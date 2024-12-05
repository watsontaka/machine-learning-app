from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from picture_classification.models import Loan_Data
from django.forms import ModelForm

class Loan_Data_Form(ModelForm):
  name = forms.CharField(label='氏名')

  class Meta:
    model = Loan_Data
    exclude = ['loan_status']