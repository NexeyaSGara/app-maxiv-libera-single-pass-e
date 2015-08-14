#!/usr/bin/env python

# Code implementation generated from reading ui file 'libera_single_pass_e_mini.ui'
#
# Created: Tue Aug 11 16:29:36 2015 
#      by: Taurus UI code generator 3.3.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from PyQt4 import QtGui, QtCore
from ui_libera_single_pass_e_mini import Ui_LiberaSinglePassEMini
from taurus.qt.qtgui.panel import TaurusWidget
from PyQt4.Qwt5 import QwtPlot, QwtSymbol, QwtPlotMarker, QwtText
import PyTango
from mytauruscurvedialog import myTaurusCurveDialog

class LiberaSinglePassEMini(TaurusWidget):
    l_plot = None
    trigger = QtCore.pyqtSignal()
    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_LiberaSinglePassEMini()
        self._ui.setupUi(self)
        self._ui.taurusCurveDialog = myTaurusCurveDialog(self)
        self._ui.taurusCurveDialog.setObjectName("taurusCurveDialog")
        self._ui.gridLayout.addWidget(self._ui.taurusCurveDialog, 0, 0, 1, 1)
        self.l_plot = self._ui.taurusCurveDialog.get_active_plot()
        self.sym = QwtSymbol(QwtSymbol.Ellipse, QtGui.QBrush(QtCore.Qt.blue), QtGui.QPen(QtCore.Qt.blue), QtCore.QSize(10, 10))
        self.sym_old = QwtSymbol(QwtSymbol.Ellipse, QtGui.QBrush(QtCore.Qt.gray), QtGui.QPen(QtCore.Qt.gray), QtCore.QSize(4, 4))
        self.l_plot.set_axis_limits('left', -0.003, 0.003)
        self.l_plot.set_axis_title('left', "Y")
        self.l_plot.set_axis_unit('left', "mm")
        self.l_plot.set_axis_limits('bottom', -0.003, 0.003)
        self.l_plot.set_axis_title('bottom', "X")
        self.l_plot.set_axis_unit('bottom', "mm") 
        self.x = 0
        self.y = 0
        self.list_mark = []
        self.trigger.connect(self.update_plot)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'liberasinglepassemini'
        ret['group'] = 'Taurus Display'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret

    def setModel(self, models):
        self._ui.taurusTrend.setModel(models[:3])
        index = models[0].rfind("/")
        self.dev = PyTango.DeviceProxy(models[0][:index])
        self.id1 = self.dev.subscribe_event('X', PyTango.EventType.CHANGE_EVENT, self.handle_x)
        self.id2 = self.dev.subscribe_event('Y', PyTango.EventType.CHANGE_EVENT, self.handle_y)
        self._ui.taurusTrend_2.setModel(models[3])

    def handle_x(self, evt):
        if evt.attr_value is not None:
            if evt.attr_value.value != self.x:
	        self.x = evt.attr_value.value / 1e9

    def handle_y(self, evt):
        if evt.attr_value is not None:
            if evt.attr_value.value != self.y:
	        self.y = evt.attr_value.value / 1e9
                self.mark = QwtPlotMarker()
                self.mark.setSymbol(self.sym)
                self.mark.attach(self.l_plot)
	        self.mark.setValue(self.x, self.y)
                if len(self.list_mark) > 10:
                    self.list_mark[0].setVisible(False)
                    l_mark = self.list_mark[0]
                    self.list_mark.pop(0)
                for mark in self.list_mark:
                    mark.setSymbol(self.sym_old)
                self.list_mark.append(self.mark)
                self.trigger.emit()
   
    def update_plot(self):
        if self.l_plot is not None:
            self.l_plot.replot()

def main():
    app = Qt.QApplication(sys.argv)
    w = LiberaSinglePassMini()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
