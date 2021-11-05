SECRET_KEY = 'django-insecure-!agyh0%smgbknucyw^g32-*(j0-k*esylg0xg82=njt@3v_16='

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'SuperSeceretPassword2255!!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
