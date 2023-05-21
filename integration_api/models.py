from django.db import models


# Create your models here.
class Logs(models.Model):
    # Login Status
    SUCCESS = 'S'
    FAILED = 'F'

    LOGIN_STATUS = ((SUCCESS, 'Success'),
                    (FAILED, 'Failed'))

    user = models.ForeignKey('auth.User', related_name='user_id', on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=40, null=True, blank=True)
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent_info = models.CharField(max_length=255, blank=True)
    login_status = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)
    attempted_at = models.DateTimeField(auto_now_add=True)
