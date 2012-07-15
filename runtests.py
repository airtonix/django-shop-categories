#!/usr/bin/env python
from djeasytests.testsetup import TestSetup, default_settings

default_settings.update(dict(
    ROOT_URLCONF='shop_categories.test_utils.project.urls',
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'shopexampledb.sqlite',
        }
    },
    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'treeadmin',
        'shop_categories',
        'shop_categories.test_utils.project'
    ],
    LANGUAGE_CODE = "en",
    LANGUAGES = (
        ('en', gettext('English')),
        ('fr', gettext('French')),
        ('de', gettext('German')),
        ('pt-BR', gettext("Brazil")),
        ('nl', gettext("Dutch")),
    ),
    SOUTH_TESTS_MIGRATE = False,
    ROOT_URLCONF = ROOT_URLCONF,
    SHOP_PRODUCT_MODEL = 'shop_categories.test_utils.project.models.product.Product',
    SHOP_CATEGORIES_CATEGORY_MODEL = 'shop_categories.test_utils.project.models.category.Category'
))

testsetup = TestSetup(appname='shop_example', default_settings=default_settings)

if __name__ == '__main__':
    testsetup.run('shell')