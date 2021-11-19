from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateKudoAPIView.as_view(), name='create_kudo'),
    path('<int:pk>/', views.RetrieveUpdateDestroyKudoAPIView.as_view(), name='get_delete_update_kudo'),
    path('employee/<int:pk>/', views.RetrieveEmployeeAPIView.as_view(), name='get_employee_kudo'),
    path('team/<int:pk>/', views.RetrieveTeamAPIView.as_view(), name='get_team_kudo'),
    path('department/<int:pk>/', views.RetrieveDepartmentAPIView.as_view(), name='get_department_kudo'),
]