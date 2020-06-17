INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party packages
    'rest_framework',
    'django_filters',
)

LOCAL_APPS = (
    'apps.users',
    'apps.products',
    'apps.invoices',
)

INSTALLED_APPS += LOCAL_APPS

MIGRATION_MODULES = {
    app_name: 'config.migrations.{}'.format(app_name)
    for app_name in map(lambda app_path: app_path.split('.')[1], LOCAL_APPS)
}
