from os.path import exists

from setuptools import find_packages, setup

if exists('README.rst'):
    with open('README.md') as f:
        long_description = f.read()
else:
    long_description = ''

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

test_requirements = ['pytest-cov']
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

setup(
    maintainer='Luke Gregor',
    maintainer_email='luke.gregor@usys.ethz.chu',
    description='Download Dataset for Oceanography',
    install_requires=install_requires,
    python_requires='>=3.6',
    license='MIT',
    long_description=long_description,
    classifiers=CLASSIFIERS,
    name='dataBrewery',
    packages=find_packages(),
    test_suite='databrewery/tests',
    tests_require=test_requirements,
    url='https://github.com/luke-gregor/dataBrewery',
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag',
    },
    setup_requires=[
        'setuptools_scm',
        'setuptools>=30.3.0',
        'setuptools_scm_git_archive',
    ],
    zip_safe=False,
)
