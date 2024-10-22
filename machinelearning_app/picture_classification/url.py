from django.urls import path
from . import views

app_name = 'picture_classification'

urlpatterns = [
  path('',views.index_view, name='index'),
  path('image_recognize/', views.image_recognize_view, name='image_recognize'),
  path('numeric_analysis/', views.numeric_analysis_view, name='numeric_analysis')
]

