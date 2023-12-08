from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show, name='show'),
    path('task/', include('taskModel.urls')),
    path('category/', include('taskCategory.urls')),
]
