import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signalrcoreplus",
    version="0.10.0",
    author="mandrewcito",
    author_email="anbaalo@gmail.com",
    description="A Python SignalR Core client(json and messagepack), with invocation auth and two way streaming. Compatible with azure / serverless functions. Also with automatic reconnect and manually reconnect.",
    keywords="signalr core client 3.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license_file="LICENSE",
    url="https://github.com/dcmeglio/signalrcore",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3.6"],
    install_requires=["requests>=2.22.0", "websocket-client==1.4.2", "msgpack==1.0.2"],
)
