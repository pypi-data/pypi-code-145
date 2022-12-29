from setuptools import setup, find_namespace_packages


setup(
    name='qtoggleserver-zigbee2mqtt',
    version='1.0.0-beta.1',
    description='qToggleServer integration with Zigbee2MQTT',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages(),

    install_requires=[
        'asyncio-mqtt',
    ]
)
