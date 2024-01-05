from django.urls import path
from flow import views

app_name = 'flow'

urlpatterns = [
    path('', views.index, name="index"),

    path('flow/<int:process_id>/detail/', views.showFlow, name="showFlow"),
    path('flow/create/', views.addFlow, name="addFlow"),
    path('flow/<int:process_id>/update/', views.editFlow, name="editFlow"),

    path('notification/<int:notification_id>/detail/', views.showNotif, name="showNotif"),
    path('notification/create/', views.addNotif, name="addNotif"),
    path('notification/<int:notification_id>/update/', views.editNotif, name="editNotif"),
]