from setuptools import setup, find_packages

setup(
    name='ipinfo',
    version='0.1.0',
    description='A package to to get information on an IP address using whatismyipaddress.com',
    author='Julien de la Bruère-Terreault',
    author_email='drgfreeman@tuta.io',
    url='https://github.com/DrGFreeman/IP-Info',
    license='MIT',
    python_requires='>=3.6',
    install_requires=['requests'],
    packages=find_packages(),
)
