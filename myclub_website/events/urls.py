from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home") 
    # path converters{int>numbsers, str>text, path>whole urls & /, 
    # slug:hyphens and underscores, UUID: universally uinique identifier}
]
