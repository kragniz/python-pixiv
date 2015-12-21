#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests',
    'six'
]

test_requirements = [
    'pytest',
    'betamax-serializers',
    'betamax',
]

setup_requires = [
    'pytest-runner',
]

setup(
    name='pixiv',
    version='0.1.1',
    description="Pixiv API client.",
    long_description=readme + '\n\n' + history,
    author="Louis Taylor",
    author_email='louis@kragniz.eu',
    url='https://pixiv.readthedocs.org',
    packages=[
        'pixiv',
    ],
    package_dir={'pixiv':
                 'pixiv'},
    include_package_data=True,
    install_requires=requirements,
    license="LGPLv3",
    zip_safe=False,
    keywords='pixiv',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requires,
)
