"""
Django settings for fdm2 project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from collections import OrderedDict

from constance import config as cconfig
from decouple import config, Csv

SITE_ID = 1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

CONSTANCE_ADDITIONAL_FIELDS = {
	'acc_auth_method_select'     : ['django.forms.ChoiceField', {
		'widget' : 'django.forms.Select',
		'choices': (
			('username', "Username"),
			('email', "Email"),
			('username_email', "Username/Email")
		)
	}],
	'acc_protocol_select'        : ['django.forms.ChoiceField', {
		'widget' : 'django.forms.Select',
		'choices': (
			('http', "HTTP"),
			('https', "HTTPS"),
		)
	}],
	'acc_session_remember_select': ['django.forms.ChoiceField', {
		'widget' : 'django.forms.Select',
		'choices': (
			(None, "None"),
			(True, "True"),
			(False, "False")
		)
	}],
	'cache_type_select'          : ['django.forms.ChoiceField', {
		'widget' : 'django.forms.Select',
		'choices': (
			(None, "------"),
			('database', "Database"),
			('dummy', "Dummy"),
			('file', "File"),
			('local', "Local Memory"),
			('mem', "Memcahced"),
			('mem-py', "Py-Memcached"),)
	}],
	'db_engine_select'           : ['django.forms.ChoiceField', {
		'widget' : 'django.forms.Select',
		'choices': (
			('django.db.backends.postgresql_psycopg2', 'PostgreSQL'),
		)
	}]
}

CONSTANCE_CONFIG = {
	'SITE_NAME'                             : ('ERP', 'Website Title', str),
	'SITE_DESCRIPTION'                      : ('', 'Website Description', str),
	'DEBUG'                                 : (config('DEBUG', cast=bool), 'Debug Mode', bool),
	'DB_ENGINE'                             : (config('DB_ENGINE'), 'Database Engine', 'db_engine_select'),
	'DB_NAME'                               : (config('DB_NAME'), 'Database Name', str),
	'DB_USER'                               : (config('DB_USER'), 'Database User', str),
	'DB_PASSWORD'                           : (config('DB_PASSWORD'), 'Database Password', str),
	'DB_HOST'                               : (config('DB_HOST'), 'Database Host', str),
	'DB_PORT'                               : (config('DB_PORT', cast=int), 'Database Port', int),
	'LANGUAGE_CODE'                         : (config('LANGUAGE_CODE'), 'Language Code', str),
	'TIME_ZONE'                             : (config('TIME_ZONE'), 'Time Zone', str),
	'USE_I18N'                              : (
		config('USE_I18N', cast=bool), 'Enable Internationalization support?', bool),
	'USE_L10N'                              : (config('USE_L10N', cast=bool), 'Enable Localization support?', bool),
	'USE_TZ'                                : (config('USE_TZ', cast=bool), 'Enable Time Zone support?', bool),
	'CACHE_TYPE'                            : (config('CACHE_TYPE'), 'Type of cache to use', 'cache_type_select'),
	'CACHE_KEY_PREFIX'                      : (config('CACHE_KEY_PREFIX'), 'A string that will be automatically '
	                                                                       'prepended to all the cache keys', str),
	'CACHE_LOCATION'                        : (config('CACHE_LOCATION'), 'The location of the cache to use', str),
	'CACHE_TIMEOUT'                         : (
		config('CACHE_TIMEOUT', cast=int), 'The number of seconds before a cache entry '
		                                   'is considered stale', int),
	'CACHE_MAX_ENTRIES'                     : (config('CACHE_MAX_ENTRIES', cast=int), 'Maximum entries to keep', int),
	'ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS' : (config('ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS', cast=bool),
	                                           'Redirect authenticated users to LOGIN_REDIRECT_URL '
	                                           'when try accessing login/signup pages', bool),
	'ACCOUNT_AUTHENTICATION_METHOD'         : (config('ACCOUNT_AUTHENTICATION_METHOD'),
	                                           'Specifies the login method to use', 'acc_auth_method_select'),
	'ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS': (config('ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS', cast=int),
	                                           'Determines the expiration date of email confirmation mails '
	                                           '(# of days)', int),
	'ACCOUNT_EMAIL_REQUIRED'                : (config('ACCOUNT_EMAIL_REQUIRED', cast=bool),
	                                           'The user is required to hand over an e-mail address when '
	                                           'signing up', bool),
	'ACCOUNT_USERNAME_REQUIRED'             : (config('ACCOUNT_USERNAME_REQUIRED', cast=bool),
	                                           'The user is required to hand over the username when signing up', bool),
	'ACCOUNT_EMAIL_VERIFICATION'            : (config('ACCOUNT_EMAIL_VERIFICATION', cast=bool),
	                                           'Determines e-mail verification during signup', bool),
	'ACCOUNT_DEFAULT_HTTP_PROTOCOL'         : (config('ACCOUNT_DEFAULT_HTTP_PROTOCOL'),
	                                           'The default protocol used for when '
	                                           'generating URLs', 'acc_protocol_select'),
	'ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN'   : (config('ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN', cast=int),
	                                           'The cooldown period (sec) after a confionrmation email is sent', int),
	'ACCOUNT_LOGIN_ATTEMPTS_LIMIT'          : (config('ACCOUNT_LOGIN_ATTEMPTS_LIMIT', cast=int),
	                                           'Number of failed login attempts', int),
	'ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT'        : (config('ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT', cast=int),
	                                           'Time period, in seconds, from last unsuccessful login attempt', int),
	'ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE'     : (config('ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE', cast=bool),
	                                           'Log out after changing the password', bool),
	'ACCOUNT_LOGIN_ON_PASSWORD_RESET'       : (config('ACCOUNT_LOGIN_ON_PASSWORD_RESET', cast=bool),
	                                           'Log in user after password reset', bool),
	'ACCOUNT_LOGOUT_REDIRECT_URL'           : (config('ACCOUNT_LOGOUT_REDIRECT_URL'),
	                                           'The URL to return to after the user logs out', str),
	'ACCOUNT_PRESERVE_USERNAME_CASING'      : (config('ACCOUNT_PRESERVE_USERNAME_CASING', cast=bool),
	                                           'Determines whether the username is stored in lowercase (False)', bool),
	'ACCOUNT_SESSION_REMEMBER'              : (config('ACCOUNT_SESSION_REMEMBER'),
	                                           'Controls the life time of the session', 'acc_session_remember_select'),
	'ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE'      : (config('ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE', cast=bool),
	                                           'Ask the user to type their email twice during signup', bool),
	'ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE'   : (config('ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE', cast=bool),
	                                           'Ask the user to type their password twice during signup', bool),
	'ACCOUNT_USERNAME_BLACKLIST'            : (config('ACCOUNT_USERNAME_BLACKLIST'), 'Banned usernames', str),
	'ACCOUNT_UNIQUE_EMAIL'                  : (config('ACCOUNT_UNIQUE_EMAIL', cast=bool),
	                                           'Enforce uniqueness of email addresses', bool),
	'ACCOUNT_USERNAME_MIN_LENGTH'           : (config('ACCOUNT_USERNAME_MIN_LENGTH', cast=int),
	                                           'Minimum allowed length of a username', int),
	'LOGIN_REDIRECT_URL'                    : (config('LOGIN_REDIRECT_URL'), 'Login Redirect URL', str),
	'SOCIALACCOUNT_AUTO_SIGNUP'             : (config('SOCIALACCOUNT_AUTO_SIGNUP', cast=bool),
	                                           'Bypass the signup form', bool),
}

CONSTANCE_CONFIG_FIELDSETS = OrderedDict([
	('General Settings', ('SITE_NAME', 'SITE_DESCRIPTION',)),
	('Site Settings', (
		'DEBUG',
		'LANGUAGE_CODE', 'TIME_ZONE', 'USE_I18N', 'USE_L10N', 'USE_TZ',)),
	('Database Settings', ('DB_ENGINE', 'DB_HOST', 'DB_PORT', 'DB_NAME', 'DB_USER', 'DB_PASSWORD',)),
	('Cache Settings', ('CACHE_TYPE', 'CACHE_KEY_PREFIX', 'CACHE_LOCATION', 'CACHE_TIMEOUT', 'CACHE_MAX_ENTRIES')),
	('Account Settings', ('ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS', 'ACCOUNT_AUTHENTICATION_METHOD',
	                      'ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS', 'ACCOUNT_EMAIL_REQUIRED',
	                      'ACCOUNT_USERNAME_REQUIRED', 'ACCOUNT_EMAIL_VERIFICATION', 'ACCOUNT_DEFAULT_HTTP_PROTOCOL',
	                      'ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN', 'ACCOUNT_LOGIN_ATTEMPTS_LIMIT',
	                      'ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT', 'ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE',
	                      'ACCOUNT_LOGIN_ON_PASSWORD_RESET', 'ACCOUNT_LOGOUT_REDIRECT_URL',
	                      'ACCOUNT_PRESERVE_USERNAME_CASING', 'ACCOUNT_SESSION_REMEMBER',
	                      'ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE', 'ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE',
	                      'ACCOUNT_USERNAME_BLACKLIST', 'ACCOUNT_UNIQUE_EMAIL', 'ACCOUNT_USERNAME_MIN_LENGTH',
	                      'LOGIN_REDIRECT_URL', 'SOCIALACCOUNT_AUTO_SIGNUP')),
])

# CELERY_BROKER_URL = 'amqp://localhost'
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_RESULT_PERSISTENT = False
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = config('TIME_ZONE')
# CELERY_ENABLE_UTC = True
# CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERYD_TASK_SOFT_TIME_LIMIT = 60


# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'



# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = cconfig.DEBUG
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition
INSTALLED_APPS = [
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',
	'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.google',
	#'constance',
	'guardian',
	'django_celery_results',
	'django_extensions',
	'bootstrap3',
	'widget_tweaks',
	'jquery',
	'django_celery_beat',
	'rest_framework',
	'dashboards',
	'groveapi',

	'djcelery_email',

	#To know the database
	'django_tables2',
	
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
	'django.middleware.http.ConditionalGetMiddleware',
	'django.middleware.gzip.GZipMiddleware'

]

ROOT_URLCONF = 'fdm2.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS'   : [os.path.join(BASE_DIR, '.', 'templates')],

		'OPTIONS': {
			'context_processors': [
	#			'constance.context_processors.config',
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'loaders'           : [
				'apptemplates.Loader',
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
				'admin_tools.template_loaders.Loader',
			],
		},
	},
]




AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
	'guardian.backends.ObjectPermissionBackend'
)




#For Constance backend
# CONSTANCE_BACKEND = 'constance.backends.redisd'






WSGI_APPLICATION = 'fdm2.wsgi.application'

#For sending an email from google[gmail]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com',
EMAIL_HOST_USER = 'testqashack@gmail.com',
EMAIL_HOST_PASSWORD = 'testqashack@123',
EMAIL_PORT = 587,
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'myemail@gmail.com'
SERVER_EMAIL = 'myemail@gmail.com'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE'  : config('DB_ENGINE'),
		'NAME'    : config('DB_NAME'),
		'USER'    : config('DB_USER'),
		'PASSWORD': config('DB_PASSWORD'),
		'HOST'    : config('DB_HOST'),
		'PORT'    : config('DB_PORT')
	}
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE')
TIME_ZONE = config('TIME_ZONE')
USE_I18N = config('USE_I18N')
USE_L10N = config('USE_L10N')
USE_TZ = config('USE_TZ')

REST_FRAMEWORK = {
	'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



LOGGING = {
	'version'                 : 1,
	'disable_existing_loggers': False,
	'formatters'              : {
		'console': {
			# exact format is not important, this is the minimum information
			'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
		},
	},
	'handlers'                : {
		'console': {
			'class'    : 'logging.StreamHandler',
			'formatter': 'console',
		},
	},
	'loggers'                 : {
		'': {
			'level'   : 'INFO',
			'handlers': ['console'],
		},
	},
}

# Cache Settings
if cconfig.CACHE_TYPE is not None:
	if cconfig.CACHE_TYPE == 'database':
		CACHES = {
			'default': {
				'BACKEND'   : 'django.core.cache.backends.db.DatabaseCache',
				'TIMEOUT'   : cconfig.CACHE_TIMEOUT,
				'OPTIONS'   : {
					'MAX_ENTRIES': cconfig.CACHE_MAX_ENTRIES
				},
				'KEY_PREFIX': cconfig.CACHE_KEY_PREFIX,
			}
		}
	elif cconfig.CACHE_TYPE == 'dummy':
		CACHES = {
			'default': {
				'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
			}
		}
	elif cconfig.CACHE_TYPE == 'file':
		CACHES = {
			'default': {
				'BACKEND'   : 'django.core.cache.backends.filebased.FileBasedCache',
				'LOCATION'  : cconfig.CACHE_LOCATION,
				'TIMEOUT'   : cconfig.CACHE_TIMEOUT,
				'OPTIONS'   : {
					'MAX_ENTRIES': cconfig.CACHE_MAX_ENTRIES
				},
				'KEY_PREFIX': cconfig.CACHE_KEY_PREFIX,
			}
		}
	elif cconfig.CACHE_TYPE == 'local':
		CACHES = {
			'default': {
				'BACKEND'   : 'django.core.cache.backends.locmem.LocMemCache',
				'LOCATION'  : cconfig.CACHE_LOCATION,
				'TIMEOUT'   : cconfig.CACHE_TIMEOUT,
				'OPTIONS'   : {
					'MAX_ENTRIES': cconfig.CACHE_MAX_ENTRIES
				},
				'KEY_PREFIX': cconfig.CACHE_KEY_PREFIX,
			}
		}
	elif cconfig.CACHE_TYPE == 'mem':
		CACHES = {
			'default': {
				'BACKEND'   : 'django.core.cache.backends.memcached.MemcachedCache',
				'LOCATION'  : cconfig.CACHE_LOCATION,
				'TIMEOUT'   : cconfig.CACHE_TIMEOUT,
				'OPTIONS'   : {
					'MAX_ENTRIES': cconfig.CACHE_MAX_ENTRIES
				},
				'KEY_PREFIX': cconfig.CACHE_KEY_PREFIX,
			}
		}
	elif cconfig.CACHE_TYPE == 'mem-py':
		CACHES = {
			'default': {
				'BACKEND'   : 'django.core.cache.backends.memcached.PyLibMCCache',
				'LOCATION'  : cconfig.CACHE_LOCATION,
				'TIMEOUT'   : cconfig.CACHE_TIMEOUT,
				'OPTIONS'   : {
					'MAX_ENTRIES': cconfig.CACHE_MAX_ENTRIES
				},
				'KEY_PREFIX': cconfig.CACHE_KEY_PREFIX,
			}
		}

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = cconfig.ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS
ACCOUNT_AUTHENTICATION_METHOD = cconfig.ACCOUNT_AUTHENTICATION_METHOD
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = cconfig.ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS
ACCOUNT_EMAIL_REQUIRED = cconfig.ACCOUNT_EMAIL_REQUIRED
ACCOUNT_USERNAME_REQUIRED = cconfig.ACCOUNT_USERNAME_REQUIRED
ACCOUNT_EMAIL_VERIFICATION = cconfig.ACCOUNT_EMAIL_VERIFICATION
ACCOUNT_DEFAULT_HTTP_PROTOCOL = cconfig.ACCOUNT_DEFAULT_HTTP_PROTOCOL
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = cconfig.ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = cconfig.ACCOUNT_LOGIN_ATTEMPTS_LIMIT
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = cconfig.ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = cconfig.ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE
ACCOUNT_LOGIN_ON_PASSWORD_RESET = cconfig.ACCOUNT_LOGIN_ON_PASSWORD_RESET
ACCOUNT_LOGOUT_REDIRECT_URL = cconfig.ACCOUNT_LOGOUT_REDIRECT_URL
ACCOUNT_PRESERVE_USERNAME_CASING = cconfig.ACCOUNT_PRESERVE_USERNAME_CASING
ACCOUNT_SESSION_REMEMBER = cconfig.ACCOUNT_SESSION_REMEMBER
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = cconfig.ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = cconfig.ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE
ACCOUNT_USERNAME_BLACKLIST = cconfig.ACCOUNT_USERNAME_BLACKLIST
ACCOUNT_UNIQUE_EMAIL = cconfig.ACCOUNT_UNIQUE_EMAIL
ACCOUNT_USERNAME_MIN_LENGTH = cconfig.ACCOUNT_USERNAME_MIN_LENGTH
LOGIN_REDIRECT_URL = cconfig.LOGIN_REDIRECT_URL
SOCIALACCOUNT_AUTO_SIGNUP = cconfig.SOCIALACCOUNT_AUTO_SIGNUP

SITE_NAME = cconfig.SITE_NAME
SITE_DESCRIPTION = cconfig.SITE_DESCRIPTION
if DEBUG:
	INTERNAL_IPS = ('127.0.0.1', 'localhost' )

	MIDDLEWARE += (
		'debug_toolbar.middleware.DebugToolbarMiddleware',
	)

	INSTALLED_APPS += (
		'debug_toolbar',
	)

	DEBUG_TOOLBAR_PANELS = [
		'debug_toolbar.panels.versions.VersionsPanel',
		'debug_toolbar.panels.timer.TimerPanel',
		'debug_toolbar.panels.settings.SettingsPanel',
		'debug_toolbar.panels.headers.HeadersPanel',
		'debug_toolbar.panels.request.RequestPanel',
		'debug_toolbar.panels.sql.SQLPanel',
		'debug_toolbar.panels.staticfiles.StaticFilesPanel',
		'debug_toolbar.panels.templates.TemplatesPanel',
		'debug_toolbar.panels.cache.CachePanel',
		'debug_toolbar.panels.signals.SignalsPanel',
		'debug_toolbar.panels.logging.LoggingPanel',
		'debug_toolbar.panels.redirects.RedirectsPanel',
	]

	DEBUG_TOOLBAR_CONFIG = {
		'INTERCEPT_REDIRECTS': False,
	}
