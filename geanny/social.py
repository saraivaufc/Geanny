#Social Auth
SOCIAL_AUTH_USER_MODEL = 'manager.Attendee'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'email']
SOCIAL_AUTH_PIPELINE = (
	'social.pipeline.social_auth.social_details',
	'social.pipeline.social_auth.social_uid',
	'social.pipeline.social_auth.auth_allowed',
	'social.pipeline.social_auth.social_user',
	'social.pipeline.user.get_username',
	'social.pipeline.mail.mail_validation',
	'social.pipeline.social_auth.associate_by_email',
	'social.pipeline.user.create_user',
	'social.pipeline.social_auth.associate_user',
	'social.pipeline.social_auth.load_extra_data',
	'social.pipeline.user.user_details',
)



#https://apps.twitter.com/app/new 
SOCIAL_AUTH_TWITTER_KEY = 'CNm8mXbL2xASaxuNCiCWBhLYv'
SOCIAL_AUTH_TWITTER_SECRET = 'gxtQLYAvfSEZBmOkTnVPs9i3eueqfOCEOypU3k7SNOwhd2QBKS'

#https://developers.facebook.com/apps/?action=create
SOCIAL_AUTH_FACEBOOK_KEY = '1391002317873155'
SOCIAL_AUTH_FACEBOOK_SECRET ='4e3ffaef8381b4c17313e7ecbe4f6388'

#https://console.developers.google.com/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '768154434321-uq7olb58q3n5i4m1hipg16mco6fee4st.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'AIzaSyDtFlY5rnQnQk-2hPSMyQmDCjoee_wyTAE'
