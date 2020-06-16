INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps.users',
)

INSTALLED_APPS += LOCAL_APPS

MIGRATION_MODULES = {
    app_name: 'config.migrations.{}'.format(app_name)
    for app_name in map(lambda app_path: app_path.split('.')[1], LOCAL_APPS)
}
