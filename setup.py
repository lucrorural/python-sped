# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from sped import __version__


requirements = ["six"]
test_requirements = ["pytest", "pytest-cov", "pytest-mock", "coverage"]

setup(
    use_scm_version=True,
    setup_requires=["setuptools_scm", "pytest-runner"],
    name='python-sped',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    # include_package_data=True,
    # package_data={
    #     'sped': ['leiautes/*'],
    # },
    version=__version__,
    description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.',
    long_description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para '
                     'Python.',
    author='Sergio Garcia',
    author_email='sergio@ginx.com.br',
    url='',
    download_url='',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sped fiscal contábil contabilidade receita federal',
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite="tests",
)
