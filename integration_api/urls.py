from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/login-logs', views.LogsApiView.as_view(),
         name='get_user_login_logs_by_user_id'),
]
