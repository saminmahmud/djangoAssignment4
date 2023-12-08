from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index_page"),
    path('two/',views.index_two, name="index_two_page"),
]
