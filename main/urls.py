from django.urls import path
from . import views

urlpatterns = [
    # Department URLs
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
]
