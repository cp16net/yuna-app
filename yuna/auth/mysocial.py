from social.backends.twitter import TwitterOAuth


# def social_auth_user(backend, uid, user=None, *args, **kwargs):
#     """Return UserSocialAuth account for backend/uid pair or None if it
#     doesn't exists.

#     Raise AuthAlreadyAssociated if UserSocialAuth entry belongs to another
#     user.
#     """
#     social_user = UserSocialAuth.get_social_auth(backend.name, uid)
#     if social_user:
#         if not user:
#             user = social_user.user
#     return {'social_user': social_user,
#             'user': user,
#             'new_association': False}


def get_user_avatar(backend, details, response, social_user, uid,
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == TwitterOAuth:
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        profile = user.get_profile()
        profile.photo = url
        profile.save()