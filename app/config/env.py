SECRET_KEY = 'django-insecure-1e39_+od948qav9wfv9hnizmkko=w(he#w5h^gz_wym)hu_s##'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '0.0.0.0',
        'NAME': 'db_name',
        'USER': 'root',
        'PASSWORD': 'password',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}
