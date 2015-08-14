#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
##
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## (copyleft) CELLS / ALBA Synchrotron, Bellaterra, Spain
##
## This is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This software is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
###########################################################################

"""
configuration file for an example of how to construct a GUI based on TaurusGUI

This configuration file determines the default, permanent, pre-defined
contents of the GUI. While the user may add/remove more elements at run
time and those customizations will also be stored, this file defines what a
user will find when launching the GUI for the first time.
"""

# =============================================================================
# Import section. You probably want to keep this line. Don't edit this block
# unless you know what you are doing
from taurus.qt.qtgui.taurusgui.utils import PanelDescription, Qt_Qt
import PyTango
# (end of import section)
# =============================================================================


# ==============================================================================
# General info.
# ==============================================================================
GUI_NAME = 'LiberaSinglePassE'
ORGANIZATION = 'MAXIV'
CUSTOM_LOGO = 'images/maxivlogo.png'

# ==============================================================================
# If you want to have a main synoptic panel, set the SYNOPTIC variable
# to the file name of a jdraw file. If a relative path is given, the directory
# containing this configuration file will be used as root
# (comment out or make SYNOPTIC=None to skip creating a synoptic panel)
# ==============================================================================
# SYNOPTIC = ['images/delaygen.jdw']

# ==============================================================================
# Set INSTRUMENTS_FROM_POOL to True for enabling auto-creation of
# instrument panels based on the Pool Instrument info
# ==============================================================================
# INSTRUMENTS_FROM_POOL = False

# ==============================================================================
# Define panels to be shown.
# To define a panel, instantiate a PanelDescription object (see documentation
# for the gblgui_utils module)
# ==============================================================================

# Build libera models

libera_models = {'Libera-001': ['I-S01B/DIA/BPL-01/'],
                 'Libera-002': ['I-MS1/DIA/BPL-01/'],
                 'Libera-003': ['I-MS1/DIA/BPL-02/'],
                 'Libera-004': ['I-BC1/DIA/BPL-01/'],
                 'Libera-005': ['I-BC1/DIA/BPL-02/'],
                 'Libera-006': ['I-MS2/DIA/BPL-01/'],
                 'Libera-007': ['I-S04B/DIA/BPL-01/'],
                 'Libera-008': ['I-EX1/DIA/BPL-01/'],
                 'Libera-009': ['I-EX1/DIA/BPL-02/'],
                 'Libera-010': ['I-TR1/DIA/BPL-01/'],
                 'Libera-011': ['I-TR1/DIA/BPL-02/'],
                 'Libera-012': ['I-S12A/DIA/BPL-01/'],
                 'Libera-013': ['I-S14B/DIA/BPL-01/'],
                 'Libera-014': ['I-S16B/DIA/BPL-01/'],
                 'Libera-015': ['I-S19B/DIA/BPL-01/'],
                 'Libera-016': ['I-EX3/DIA/BPL-01/'],
                 'Libera-017': ['I-BC2/DIA/BPL-01/'],
                 'Libera-018': ['I-KTR3/DIA/BPL-01/'],
                 'Libera-019': ['I-TR3/DIA/BPL-02/'],
                 'Libera-020': ['I-TR3/DIA/BPL-04/'],
                    }

libera_attributes = ['X', 'Y', 'Q', 'Sum']
libera_models_attr = {}

# Build panels

for key, models in libera_models.iteritems():
    device = models[0].upper()
    index = device.rfind("-")
    l_model = []
    for attr in libera_attributes:
        l_model.append(device + attr)

    locals()[key] = PanelDescription(
        device[:index] + device[index + 1:],
        classname='LiberaSinglePassEMini',
        modulename='tgconf_libera_single_pass_e.panels',
        model=l_model
    )

# Build alarm panel

# PanicGuiWidget = PanelDescription('Panic Taurus Widget',
#                                   classname = 'TaurusAlarmGUI',
#                                   modulename= "PanicGUI.gui",
#                                   model="I/PSS/Watchdog",
#                                   )

# ==============================================================================
# Define which External Applications are to be inserted.
# To define an external application, instantiate an ExternalApp object
# See TauMainWindow.addExternalAppLauncher for valid values of ExternalApp
# ==============================================================================
# xterm = ExternalApp(cmdargs=['xterm','spock'], text="Spock",
#                     icon='utilities-terminal')
# hdfview = ExternalApp(["hdfview"])
# pymca = ExternalApp(['pymca'])

# ==============================================================================
# Macro execution configuration
# (comment out or make MACRO_SERVER=None to skip creating a macro execution
# infrastructure)
# ==============================================================================
# MACROSERVER_NAME =''
# DOOR_NAME = ''
# MACROEDITORS_PATH = ''

# ==============================================================================
# Monitor widget
# ==============================================================================
# MONITOR = ['sys/tg_test/1/double_scalar_rww']
