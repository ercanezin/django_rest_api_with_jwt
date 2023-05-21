from rest_framework_simplejwt.tokens import RefreshToken
from integration_api.models import Logs

import logging

error_log = logging.getLogger('error')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "username": user.username,
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_agent_info(request):
    return request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],


def logged_in_success(user, request):
    try:
        user_login_activity_log = Logs()
        user_login_activity_log.user = user
        user_login_activity_log.user_name = user.username
        user_login_activity_log.user_ip = get_client_ip(request)
        user_login_activity_log.user_agent_info = get_agent_info(request)
        user_login_activity_log.login_status = Logs.SUCCESS
        user_login_activity_log.save()
    except Exception as e:
        error_log.error("log_user request: %s, error: %s" % (request, e))


def logged_in_failed(serializer, request):
    try:
        user_login_activity_log = Logs()
        user_login_activity_log.user = None
        user_login_activity_log.user_name = serializer.data['username']
        user_login_activity_log.user_ip = get_client_ip(request)
        user_login_activity_log.user_agent_info = get_agent_info(request)
        user_login_activity_log.login_status = Logs.FAILED
        user_login_activity_log.save()

    except Exception as e:
        error_log.error("log_user request: %s, error: %s" % (request, e))
