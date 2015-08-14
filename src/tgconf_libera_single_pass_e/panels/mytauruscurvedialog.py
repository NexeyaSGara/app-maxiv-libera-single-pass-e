
from PyQt4 import QtCore, QtGui
from taurus.qt.qtgui.extra_guiqwt import TaurusCurveDialog

class myTaurusCurveDialog(TaurusCurveDialog):
    def __init__(self, parent=None):
        TaurusCurveDialog.__init__(self, parent=parent)
        self.setModifiableByUser(False)
        self.toolbar.setVisible(False)

    def contextMenuEvent(self, event):
        pass

