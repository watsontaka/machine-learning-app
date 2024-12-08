from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

from django.views.decorators.http import require_POST

import numpy as np
import pickle
import csv
from picture_classification.models import Loan_Data
from picture_classification.forms import Loan_Data_Form

app_name = 'picture_classification'

file_model_name = 'finalized_model.sav'
loaded_model = pickle.load(open(file_model_name, 'rb'))

def index_view(request):

  return render(request, 'index.html')


def image_recognize_view(request):

  return render(request, 'image_recognize.html')


def numeric_analysis_view(request):

  # one-hotベクトルに変換する関数
  def one_hot(dicts, post):
    zero = np.zeros(len(dicts))
    zero[dicts[post]]=1
    return zero
    
    # 金額調整
  def money_exchange(x):
    return x*10000
    
  if request.method == 'POST':
    form = Loan_Data_Form(request.POST)
    if form.is_valid():
      name = request.POST['name']
      age = request.POST['age']
      gender = request.POST['gender']
      education = request.POST['education']
      income = request.POST['income']
      emp_exp = request.POST['emp_exp']
      loan_amount = request.POST['loan_amount']
      home_ownership = request.POST['home_ownership']
      loan_intent = request.POST['loan_intent']
      default = request.POST['default']
    
      # 辞書
      gender_dict = {'男性':0, '女性':1}
      education_dict = {'高卒':0, '短大卒':1, '学士卒':2, '修士卒':3, '博士卒':4}
      home_ownership_dict = {'賃貸':0, '自己所有':1, 'ローン付き':2, 'その他':3}
      loan_intent_dict = {'債務返済':0, '教育':1, 'リフォーム':2, '医療':3, '私的':4, '事業':5}
      default_dict = {'はい':0, 'いいえ':1}

      # 予測に使用する説明変数の加工
      variable_x = np.array([age, gender_dict[gender], education_dict[education], money_exchange(int(income)), emp_exp, money_exchange(int(loan_amount)), default_dict[default]], dtype=np.int64)
      one_hots = np.concatenate([one_hot(home_ownership_dict, home_ownership), one_hot(loan_intent_dict, loan_intent)])
      variable_x = np.concatenate([variable_x, one_hots])
      variable_x = variable_x[np.newaxis,:]
      loan_status = loaded_model.predict(variable_x)[0]
      loan_status_dict = {0:'承認', 1:'不承認'}
      loan_status = loan_status_dict[loan_status]

      # データの保存
      object = Loan_Data.objects.create(
        name = name, age = age, gender = gender, education = education, income = income, emp_exp = emp_exp, loan_amount = loan_amount, 
        home_ownership = home_ownership, loan_intent = loan_intent, default=default, loan_status=loan_status,
      )
      object.save()
      return redirect(to='/list')
    else:
      return render(request, 'numeric_analysis.html', {'form': form})
  else:
    return render(request, 'numeric_analysis.html')

  
def npl_view(request):

  return render(request, 'nlp.html')


def list_view(request):

  page_obj = Loan_Data.objects.order_by('id').all()
  query = request.GET.get('query')

  if query:
    page_obj = Loan_Data.objects.filter(name__contains=query)

  paginator = Paginator(page_obj, 3)
  page = request.GET.get("page")

  try:
    page_obj = paginator.page(page)
    page_number_list = page_obj.paginator.get_elided_page_range()
  except PageNotAnInteger:
    page_obj = paginator.get_page(1)
    page_number_list = page_obj.paginator.get_elided_page_range()
  except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)

  return render(request, 'list.html', {"page_obj": page_obj, 'page_number_list': page_number_list})


def csv_export(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="loan_data.csv"'
  writer = csv.writer(response)
  for ld in Loan_Data.objects.all():
    writer.writerow([ld.name, ld.age, ld.gender, ld.education, ld.income, ld.emp_exp, ld.loan_amount, 
        ld.home_ownership, ld.loan_intent, ld.default, ld.loan_status])
  return response

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

  data_counts = Loan_Data.objects.values('gender')

  gender_counts = []

  for c in data_counts:
    gender_counts.append(c['gender'])

  context = {
        'male' : gender_counts.count('男性'),
        'female' : gender_counts.count('女性'),
    }

  return render(request, 'graph.html', context)