from setuptools import setup, find_packages
import os

version = '0.1' 

setup(name='medialog.plotly',
      version=version,
      description="Makes it possible to use plotly with plone.",
      long_description=open("README").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone 5",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone zope plotly',
      author='Grieg Medialog [Espen Moe-Nilssen]',
      author_email='espen@medialog.no',
      url='http://github.com/espemn/medialog.plotly',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'medialog.controlpanel',
          'collective.z3cform.datagridfield',
          'plone.api',
          'plone.directives.form',
          'plone.behavior',
          'plone.api',
          'plotly',
          'pandas',
           'numpy',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
