import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-coop-ionyweb-addons',
    version = '0.1',
    packages = ['page_coop_agenda', 'page_coop_exchange', 'page_members',
                'plugin_coop_agenda', 'plugin_coop_members_icons',
                'plugin_members'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Addons to ionyweb fro django-coop.',
    long_description = README,
    url = 'https://github.com/makinacorpus/django-coop-ionyweb-addons',
    author = 'Sylvain Beorchia',
    author_email = 'sylvain.beorchia@makina-corpus.com',
)
