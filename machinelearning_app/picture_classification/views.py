from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

from django.views.decorators.http import require_POST

import numpy as np
import pickle
import csv
from sklearn.linear_model import LogisticRegression
from picture_classification.models import Logistic_Predict
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
    return redirect(to='/list')
  else:
    return render(request, 'numeric_analysis.html')

  
def npl_view(request):

  return render(request, 'nlp.html')

'''
def list_view(request):

  object_list = Logistic_Predict.objects.all() 
  context = {'object_list': object_list}

  return render(request, 'list.html', context)
'''

def list_view(request):

  page_obj = Logistic_Predict.objects.order_by('id').all()
  query = request.GET.get('query')

  if query:
    page_obj = Logistic_Predict.objects.filter(name__contains=query)

  paginator = Paginator(page_obj, 3)
  page = request.GET.get("page")

  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:
    page_obj = paginator.get_page(1)
  except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)

  return render(request, 'list.html', {"page_obj": page_obj} )

'''
  paginator = Paginator(object_list, 3)

  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  return render(request, 'list.html', {"page_obj": page_obj} )
'''
'''
def edit_view(request, id):

  return
'''

'''
@require_POST
def delete_view(request):
  object_list = 
  return
'''

def graph_view(request):

  data_counts = Logistic_Predict.objects.values('sex', 'occupation')

  sex_counts = []
  occupation_counts = []

  for c in data_counts:
    sex_counts.append(c['sex'])
    occupation_counts.append(c['occupation'])

  context = {
        'male' : sex_counts.count(0),
        'female' : sex_counts.count(1),
        'government_worker' : occupation_counts.count(0),
        'private_sector' : occupation_counts.count(1),
        'unemployed' : occupation_counts.count(2),
    }

  return render(request, 'graph.html', context)