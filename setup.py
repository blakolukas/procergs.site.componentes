"""Installer for the procergs.sitedemo package."""

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="procergs.sitedemo",
    version="1.0.0a0",
    description="Site Demonstração",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="PROCERGS",
    author_email="sites@procergs.rs.gov.br",
    url="https://github.com/PROCERGS/procergs.sitedemo",
    project_urls={
        "PyPI": "https://pypi.org/project/procergs.sitedemo",
        "Source": "https://github.com/PROCERGS/procergs.sitedemo",
        "Tracker": "https://github.com/PROCERGS/procergs.sitedemo/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["procergs"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "Products.CMFCore",
        "plone.api",
        "plone.restapi",
        "plone.volto",
        "plone.base",
        "plone.dexterity",
        "plone.autoform",
        "z3c.relationfield",
        "plone.app.vocabularies",
        "plone.supermodel",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.testing",
            "plone.restapi[test]",
            "pytest-cov",
            "pytest-plone>=0.5.0",
            "plone.app.contenttypes",
            "plone.app.robotframework",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = procergs.sitedemo.locales.update:update_locale
    """,
)
