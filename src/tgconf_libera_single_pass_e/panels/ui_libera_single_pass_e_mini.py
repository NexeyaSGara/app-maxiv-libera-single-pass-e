# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'libera_single_pass_e_mini.ui'
#
# Created: Wed Aug 12 11:21:23 2015
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LiberaSinglePassEMini(object):
    def setupUi(self, LiberaSinglePassEMini):
        LiberaSinglePassEMini.setObjectName(_fromUtf8("LiberaSinglePassEMini"))
        LiberaSinglePassEMini.resize(338, 670)
        self.gridLayout = QtGui.QGridLayout(LiberaSinglePassEMini)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.taurusTrend_2 = TaurusTrend(LiberaSinglePassEMini)
        self.taurusTrend_2.setObjectName(_fromUtf8("taurusTrend_2"))
        self.gridLayout.addWidget(self.taurusTrend_2, 3, 0, 1, 1)
        self.taurusTrend = TaurusTrend(LiberaSinglePassEMini)
        self.taurusTrend.setObjectName(_fromUtf8("taurusTrend"))
        self.gridLayout.addWidget(self.taurusTrend, 1, 0, 2, 1)
        #self.taurusCurveDialog = TaurusCurveDialog(LiberaSinglePassEMini)
        #self.taurusCurveDialog.setModifiableByUser(False)
        #self.taurusCurveDialog.setObjectName(_fromUtf8("taurusCurveDialog"))
        #self.gridLayout.addWidget(self.taurusCurveDialog, 0, 0, 1, 1)

        self.retranslateUi(LiberaSinglePassEMini)
        QtCore.QMetaObject.connectSlotsByName(LiberaSinglePassEMini)

    def retranslateUi(self, LiberaSinglePassEMini):
        LiberaSinglePassEMini.setWindowTitle(_translate("LiberaSinglePassEMini", "Form", None))

from taurus.qt.qtgui.extra_guiqwt import TaurusCurveDialog
from taurus.qt.qtgui.panel import TaurusWidget
from taurus.qt.qtgui.plot import TaurusTrend

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LiberaSinglePassEMini = QtGui.TaurusWidget()
    ui = Ui_LiberaSinglePassEMini()
    ui.setupUi(LiberaSinglePassEMini)
    LiberaSinglePassEMini.show()
    sys.exit(app.exec_())

