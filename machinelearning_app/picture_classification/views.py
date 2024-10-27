from django.shortcuts import render, redirect
from sklearn.linear_model import LogisticRegression
from .models import Logistic_Predict
from .forms import Logistic_Predict_Form

app_name = 'picture_classification'

def index_view(request):

  return render(request, 'index.html')


def image_recognize_view(request):

  return render(request, 'image_recognize.html')

def numeric_analysis_view(request):
  if request.method == 'POST':
    object = Logistic_Predict.objects.create(
      name = request.POST['name'],
      age = request.POST['age'],
      sex = request.POST['sex'],
      education = request.POST['education'],
      occupation = request.POST['occupation'],
      income = request.POST['income'],
      loan = request.POST['loan'],
      loan_history = request.POST['loan-history'],
    )
    object.save()
    return redirect(to='/')
  else:
    return render(request, 'numeric_analysis.html')

'''
def logistic_predict(request):
  feature = Logistic_Predict.objects.all()

  if request.method =='POST':
    form = Logistic_Predict_Form(request.POST)
    if form.is_valid():
      form.save()

    else:
      form = Logistic_Predict_Form
    


  return render(request)
'''

def npl_view(request):

  return render(request, 'nlp.html')

def list_view(request):

  object_list = Logistic_Predict.objects.all()
  context = {'object_list': object_list}

  return render(request, 'list.html', context)
