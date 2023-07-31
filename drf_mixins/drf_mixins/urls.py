from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentAPIIstCreate/', views.StudentAPIIstCreate.as_view()),
    path('StudentAPIRetrieveUpdate/<int:pk>', views.StudentAPIRetrieveUpdate.as_view()),
]
