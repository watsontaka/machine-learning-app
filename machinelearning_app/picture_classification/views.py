from django.shortcuts import render

app_name = 'picture_classification'

def index_view(request):

  return render(request, 'index.html')



def image_recognize_view(request):

  return render(request, 'image_recognize.html')
