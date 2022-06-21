from django.contrib import admin
from django.urls import path, include
from database0 import views

urlpatterns = [
    path('', include('database0.urls')),
    path('admin/', admin.site.urls),
    path('showform/', views.showform),
    path('accounts/', include('django.contrib.auth.urls')),
    # животные
    path('animals/', views.animals_list),
    path('animals/<int:animal_id>', views.animal_info),
    # клетки
    path('cages/', views.cages_info),
    path('cages/delete', views.cage_row_delete),
]
