#!/usr/bin/env python3
# encoding: UTF-8


from distutils.core import setup

desc = """\
ZingChart Ipython plugin
==============
This pakcge will enhase ipython to use ZingChart Javascript liberarry.
ZingChart website:
http://www.zingchart.com/
More inforamtion about this package:
https://github.com/hamidre13/IPython-Kepler-Magic-Function
This package is property of ZingChart:
http://www.zingchart.com/
"""
setup(name='ZingChartIpython',
      version='1.0',
      author  ='Hamid Tavakoli',
      author_email= 'stavakol@ucsd.edu',
      url='https://github.com/hamidre13/ZingChartIpython',
      long_description=desc,
      py_modules=['ZingChart'],
      )