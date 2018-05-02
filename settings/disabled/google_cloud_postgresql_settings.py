LOCAL_SETTINGS_LOADED = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'testing',
#         'USER': 'testing',
#         'PASSWORD': 'testing',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#         # 'OPTIONS': {'ssl': {'key': '/map/to/ca-cert.pem'}}
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '35.198.146.54',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'verify-ca',
            'sslrootcert': '/home/gpl/Desktop/google_cloud_testing/server-ca.pem',
            "sslcert": "/home/gpl/Desktop/google_cloud_testing/client-cert.pem",
            "sslkey": "/home/gpl/Desktop/google_cloud_testing/client-key.pem",
        }
    }
}
