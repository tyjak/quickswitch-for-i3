# quickswitch for i3 - quickly change to and locate windows in i3.
#
# Maintainer: OliverUv <OliverUv@Github, oliver.uvman+quickswitch@gmail.com>
# Original author: slowpoke <mail+python at slowpoke dot io>
#
# This program is Free Software under the terms of the
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# version must use semver 2.0.0

from setuptools import setup

setup(name="quickswitch-i3",
      description="Quickly change to and locate windows in i3",
      long_description=open("README.rst").read(),
      version="2.7.0",
      author="OliverUv",
      author_email="oliver.uvman+quickswitch@gmail.com",
      url="https://github.com/OliverUv/quickswitch-for-i3",
      scripts=["quickswitch.py"],
      requires=["i3_py"],
      entry_points={"console_scripts": ["quickswitch=quickswitch:main"]},
      classifiers=["Intended Audience :: End Users/Desktop",
                   "Programming Language :: Python :: 3"],
      license="DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE")
