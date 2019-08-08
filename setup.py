# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "onfido"
VERSION = "4.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Onfido API",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Onfido API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Onfido API is used to submit check requests.  # noqa: E501
    """
)
