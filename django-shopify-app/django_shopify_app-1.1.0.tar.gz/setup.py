from setuptools import find_packages, setup

setup(
    name='django_shopify_app',
    version='1.1.0',
    author='Moship',
    author_email='hello@moship.io',
    packages=find_packages(),
    scripts=[],
    url='http://pypi.python.org/pypi/django_shopify_app/',
    license="MIT",
    description='A django app with all the tools required to make a Shopify app',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    package_data={
        'shopify_app': ['templates/shopify_app/*.html']
    },
    install_requires=[
        "Django >= 4.0.0",
        "pytest",
        "shopifyapi",
        "google-cloud-pubsub",
        "google-auth",
    ],
)
