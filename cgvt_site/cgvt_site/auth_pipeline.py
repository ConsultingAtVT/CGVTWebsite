import requests

from apps.core.models import UserProfile
from django.conf import settings
from social.exceptions import AuthFailed


USER_INFO_LI_REQUEST_URL = ('https://api.linkedin.com/v1/people/~:('
                            'id,'
                            'firstName,'
                            'lastName,'
                            'emailAddress,'
                            'pictureUrl,'
                            'publicProfileUrl)'
                            '?oauth2_access_token={}'
                            '&format=json')


def update_or_create_user_profile(backend, user, response, *args, **kwargs):
    li_access_token = response.get('access_token')
    li_resp = requests.get(USER_INFO_LI_REQUEST_URL.format(li_access_token))
    li_resp_json = li_resp.json()

    li_email = li_resp_json.get('emailAddress')
    if li_email not in settings.VALID_EMAILS:
        raise AuthFailed(backend, 'This is not a whitelisted email')

    user_profile, created = UserProfile.objects.get_or_create(user=user)
    user_profile.li_email = li_email
    user_profile.li_first_name = li_resp_json.get('firstName')
    user_profile.li_last_name = li_resp_json.get('lastName')
    user_profile.li_picture_url = li_resp_json.get('pictureUrl')
    user_profile.li_profile_url = li_resp_json.get('publicProfileUrl')
    user_profile.save()
