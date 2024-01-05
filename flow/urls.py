from django.urls import path
from flow import views

app_name = 'flow'

urlpatterns = [
    path('', views.index, name="index"),
    path('flow/<int:process_id>/detail/', views.showFlow, name="showFlow"),
]