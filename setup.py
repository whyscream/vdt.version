# coding: utf-8
from setuptools import find_packages, setup

pkgname = "vdt.version"

setup(name=pkgname,
      version="0.0.2",
      description="Version Increment Tool for GIT",
      author="Cosmin Luță",
      author_email="cosmin.luta@avira.com",
      maintainer="Cosmin Luță",
      maintainer_email="cosmin.luta@avira.com",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['vdt'],
      zip_safe=True,
      install_requires=[
          "setuptools",
          "straight.plugin",
          "vdt.versionplugin.default",
      ],
      entry_points={
          'console_scripts':[
              'version = vdt.version.main:main'
          ]
      },
)
