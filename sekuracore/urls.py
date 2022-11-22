from django.urls import path

from . import views

urlpatterns = [
    path("agent/", views.Agent.as_view(), name="agent"),
    path("agent/register", views.AgentRegister.as_view(), name="agent-register"),
    path("employee/", views.Employee.as_view(), name="employee"),
    path("access/", views.Access.as_view(), name="access"),
]
