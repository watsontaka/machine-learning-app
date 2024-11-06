from django import forms
from django.core.exceptions import ValidationError
from .models import Logistic_Predict

class Logistic_Predict_Form(forms.Form):
  class Meta:
    model = Logistic_Predict
    fields = ['name', 'age', 'sex', 'education', 'occupation', 'income', 'loan', 'loan_history']