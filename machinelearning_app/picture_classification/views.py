from django.shortcuts import render

def index_view(request):

  my_dicts = {
    'title':'画像認識プログラム',
    'name':'磯野貴慎',
  }

  return render(request, 'index.html', my_dicts)
