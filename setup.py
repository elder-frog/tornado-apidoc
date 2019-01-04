from os import path
from setuptools import setup

cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tornado-apidoc',
    version='1.0.0',
    packages=['tornado_apidoc'],
    url='https://github.com/wenhan-wu/tornado-apidoc',
    license='MIT',
    author='Wenhan Wu',
    author_email='sdwwh2259253@gmail.com',
    description='Adds ApiDoc support to Tornado',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['tornado', 'apidoc', 'doc', 'documentation', 'rest', 'restful'],
    install_requires=['tornado>=4.5.2'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
