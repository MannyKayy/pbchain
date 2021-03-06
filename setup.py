"""
setup script settings
"""

from setuptools import setup

setup(
    name='pbchain',
    version='0.1.0',
    description='Probabilistic Programming with Python and Chainer',
    author='Yuki Nagae',
    author_email='yuki.nagae1130@gmail.com',
    url='https://github.com/yukinagae/pbchain',
    license='MIT License',
    install_requires=[
        'numpy>=1.9.0',
        'scipy>=0.12.0',
        'six>=1.9.0',
        'chainer==3.2.0',
        # test
        'pytest',
    ],
)
