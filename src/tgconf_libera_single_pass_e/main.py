"""Module to run the taurus GUI."""

# Imports
import os
from PyQt4 import QtGui, QtCore
from functools import partial
from pickle import dump, load
from taurus.qt.qtgui.taurusgui import TaurusGui
from taurus.qt.qtgui.application import TaurusApplication

EXTENSION = "plot"
get_plot_filename = lambda gui: gui.getQSettings().fileName()[:-3] + EXTENSION

class MyTaurusGui(TaurusGui):

    def __init__(self, parent=None, confname=None, confRec=None):
        TaurusGui.__init__(self, None, confname, True)

    def event(self, event):
        if event.type() == 2:
            if event.button() == 2:
                return True
            else:
                return False
        elif event.type() == 3:
            if event.button() == 2:
                return True
            else:
                return False
        elif event.type() == 5:
            if event.button() == 2:
                return True
            else:
                return False
        else:
            return False
        #if event.type() == 2:
         #   event.ignore()
          #  print "Accept"
           # event.setAccepted(False)

# Create application
def create_application():
    """Return an (application, taurusgui) pair."""
    basedir = os.path.dirname(__file__)
    confname = os.path.join(basedir, "config.py")
    app = TaurusApplication()
    #gui = MyTaurusGui(None, confname, False)
    gui = TaurusGui(confname=confname)
    #gui.mousePressEvent = myMousePressEvent
    gui.show()
    return app, gui

def myMousePressEvent(event):
    event.ignore()
    print "event ignored"

# Callback for actions

def save_plot_config(gui):
    """Save the configuration of all the plots."""
    config_dict = {}
    # Build config dictionary
    for child in gui.findChildren(QtGui.QWidget, name="taurusTrend"):
        name = child.parent().parent().objectName()
        config_dict[name] = child.createConfig()
    # Write config file
    try:
        with open(get_plot_filename(gui), "w") as f:
            dump(config_dict, f)
    except IOError:
        msg = 'Plot settings could not be saved in "{0}"'
        gui.warning(msg.format(get_plot_filename(gui)))
    else:
        msg = 'Plot settings saved in "{0}"'
        gui.info(msg.format(get_plot_filename(gui)))


def load_plot_config(gui):
    """Display or hide widgets with a given name."""
    # Load config dictionary
    try:
        with open(get_plot_filename(gui)) as f:
            config_dict = load(f)
    except IOError:
        msg = 'Could not load plot settings from "{0}"'
        gui.warning(msg.format(get_plot_filename(gui)))
        return
    else:
        msg = 'Plot settings loaded from "{0}"'
        gui.info(msg.format(get_plot_filename(gui)))
    # Apply config
    for child in gui.findChildren(QtGui.QWidget, name="taurusTrend"):
        name = child.parent().parent().objectName()
        if name in config_dict:
            child.applyConfig(config_dict[name])

# Setup plot config actions
def setup_plot_config_actions(gui):
    """Setup plot configuration actions."""
    # Save configuration
    callback = partial(save_plot_config, gui)
    action = QtGui.QAction("Save plot configuration", gui, triggered=callback)
    gui.quickAccessToolBar.addAction(action)
    gui.quickAccessToolBar.addSeparator()
    # Load configuration
    callback = partial(load_plot_config, gui)
    action = QtGui.QAction("Load plot configuration", gui, triggered=callback)
    gui.quickAccessToolBar.addAction(action)
    gui.quickAccessToolBar.addSeparator()

# Main function
def main():
    """Run the libera taurus gui."""
    # Create GUI
    app, gui = create_application()
    # Hide toolbars
    gui.jorgsBar.hide()
    gui.statusBar().hide()
    gui.setLockView(True)
    # Setup display buttons
    setup_plot_config_actions(gui)
    # Run
    app.exec_()


# Main execution
if __name__ == "__main__":
    main()
