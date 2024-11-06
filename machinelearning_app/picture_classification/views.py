from django.shortcuts import render, redirect

import numpy as np
import pickle
import csv
from sklearn.linear_model import LogisticRegression
from .models import Logistic_Predict
from .forms import Logistic_Predict_Form

app_name = 'picture_classification'

file_model_name = 'finalized_model.sav'
loaded_model = pickle.load(open(file_model_name, 'rb'))

def index_view(request):

  return render(request, 'index.html')


def image_recognize_view(request):

  return render(request, 'image_recognize.html')

def numeric_analysis_view(request):
  if request.method == 'POST':
    name = request.POST['name']
    age = request.POST['age']
    sex = request.POST['sex']
    occupation = request.POST['occupation']
    education = request.POST['education']
    income = request.POST['income']
    loan = request.POST['loan']
    loan_history = request.POST['loan-history']

    variable_x = np.array([[age, sex, education, occupation, income, loan, loan_history]], dtype=np.int64)
    default_pred = loaded_model.predict(variable_x)

    object = Logistic_Predict.objects.create(
      name = name, age = age, sex = sex, education = education, occupation = occupation,
      income = income, loan = loan, loan_history = loan_history, default_pred = default_pred
    )
    object.save()
    return redirect(to='/')
  else:
    return render(request, 'numeric_analysis.html')

def list_view(request):

  object_list = Logistic_Predict.objects.all()
  context = {'object_list': object_list}

  return render(request, 'list.html', context)

def npl_view(request):

  return render(request, 'nlp.html')

