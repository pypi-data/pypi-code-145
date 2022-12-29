from setuptools import setup
setup(
    name='sequoia',
    version='0.0.3',
    author='An Awesome Coder',
    author_email='hanirizo@gmail.com',
    packages=['sequoia'],
    # scripts=['bin/script1', 'bin/script2'],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    # long_description=open('README.txt').read(),
    install_requires=[
        "fastapi",
        "sentry-sdk",
        "SQLAlchemy",
        "psycopg2-binary",
        "uvicorn",
        "PyJWT",
        "passlib",
        "bugsnag",
        "bcrypt",
        "python-slugify",
        "redis",
        "dnspython",
        "requests",
        "google-cloud-pubsub",
        "python-dotenv",
        "boto3",
        "toml",
        "python-multipart",
        "pydantic",
        "pydantic[email]",
        "device-detector",
        "pandas",
        "openpyxl",
        "munch",
        "pymongo",
        "click",
        "asyncpg",
        "ujson",
        "aioredis",
        "schedule",
        "slowapi"
    ],
)
