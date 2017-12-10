from django.contrib import messages
from django.shortcuts import redirect

from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social.exceptions import AuthCanceled, AuthFailed


class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        exc_type = type(exception)

        if exc_type == AuthCanceled:
            request.session['login_error_msg'] = 'Looks like you didn\'t want to login.'
        elif exc_type == AuthFailed:
            request.session['login_error_msg'] = 'You don\'t have permission to login.'

        return redirect('/home/')
