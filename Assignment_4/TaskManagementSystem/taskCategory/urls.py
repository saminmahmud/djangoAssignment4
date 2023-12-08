from django.urls import path
from . import views
urlpatterns = [
    path('add/<int:id>', views.add_category, name='add_category'),
]
