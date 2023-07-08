from .base import *

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
PRODUCTION_APPS = []
INSTALLED_APPS += PRODUCTION_APPS
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  os.environ.get('DATABASE_NAME', 'BlogDatabase'),
        'HOST':  os.environ.get('MYSQL_HOST', 'database'),
        'USER': os.environ.get('MYSQL_USER', 'user'),
        'PASSWORD': os.environ.get('MYSQL_ROOT_PASSWORD', 'd'),
        'PORT': 3306
    }
}


# STATIC_URL = "/static/"
STATICFILE_DIR = [
    os.path.join(BASE_DIR, 'static')
]


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('')
# EMAIL_HOST_PASSWORD = os.environ.get('')


# LOGGING
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_FILE = '/ERROR.log'
LOG_PATH = LOG_DIR + LOG_FILE

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

if not os.path.exists(LOG_PATH):
    f = open(LOG_PATH, 'a').close()  # create empty log file
else:
    f = open(LOG_PATH, "w").close()  # clear log file

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH,
            'formatter': 'simple',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'core.plots.plot': {
            'handlers': ['file', ],
            'level': 'ERROR'
        }
    },
    'formatters': {
        'simple': {
            'format': ' {name}- {levelname} {module} {asctime} {message}',
            'style': '{',
        },
    }
}
