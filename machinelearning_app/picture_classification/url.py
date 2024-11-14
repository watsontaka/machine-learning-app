from django.urls import path
from . import views

app_name = 'picture_classification'

urlpatterns = [
  path('',views.index_view, name='index'),
  path('image_recognize/', views.image_recognize_view, name='image_recognize'),
  path('numeric_analysis/', views.numeric_analysis_view, name='numeric_analysis'),
  path('nlp/', views.npl_view, name='nlp'),
  path('list/', views.list_view, name='list'),
  path('graph/', views.graph_view, name='graph'),
]

