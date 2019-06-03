"""Setup script for pyogt."""
from setuptools import setup, find_packages

setup(
    name='pysystembolaget',
    version='0.2.0',
    author='Claes Hallstrom',
    author_email='hallstrom.claes@gmail.com',
    description='Wrapper for Systembolaget API',
    license='MIT License',
    url='https://github.com/claha/pysystembolaget',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
