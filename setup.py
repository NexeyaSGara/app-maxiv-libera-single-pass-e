#!/usr/bin/env python

from setuptools import setup

setup(name="taurusgui-libera-single-pass-e",
      version="2.2.2",
      description="TaurusGUI for the MAX IV liberas single pass e",
      author="KITS team",
      author_email="kitscontrols@maxlab.lu.se",
      license="GPLv3",
      url="http://www.maxlab.lu.se",
      package_dir={'': 'src'},
      packages=['tgconf_libera_single_pass_e', 'tgconf_libera_single_pass_e.panels'],
      include_package_data=True,
      package_data={'tgconf_libera_single_pass_e': ['images/maxivlogo.png']},
      data_files=[('/usr/share/applications',
                   ['maxiv-libera-single-pass-e.desktop']),
                  ('/home/controlroom/Desktop',
                   ['maxiv-libera-single-pass-e.desktop'])],
      scripts=['scripts/ctLiberaSinglePassE']
      )
