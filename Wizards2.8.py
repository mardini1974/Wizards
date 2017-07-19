#!/usr/bin/python

import sys
import linuxcnc
import gtk, gobject
import numpy as np
import ConfigParser


class WizardsApp(gtk.Window):
    class axis(object):
        X = 0
        Y = 1
        Z = 2

    class Direction(object):
        Pos = 1
        Neg = -1

    # XVal_label = gtk.Label()
    # YVal_label = gtk.Label()
    # ValPosX = gtk.Label()
    # ValPosY = gtk.Label()
    # ValNegX = gtk.Label()
    # ValNegY = gtk.Label()
    # Centerresult = gtk.Label()
    # comboincrement = gtk.ComboBox()
    # Feedrate_scale = gtk.HScale()
    # C3PX1 = C3PY1 = C3PZ1 = gtk.Label()
    # C3PX2 = C3PY2 = C3PZ2 = gtk.Label()
    # C3PX3 = C3PY3 = C3PZ3 = gtk.Label()

    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("Wizards.glade")
        builder.connect_signals(self)
        global XVal_label, YVal_label
        global ValPosX, ValPosY, ValNegX, ValNegY, Centerresult, feedrate, comboincrement, Feedrate_scale
        global C3PX1, C3PY1, C3PZ1
        global C3PX2, C3PY2, C3PZ2
        global C3PX3, C3PY3, C3PZ3
        global C3PCenter,C3PRadius

        XVal_label = builder.get_object('XVal')
        YVal_label = builder.get_object('YVal')
        ValPosX = builder.get_object('ValPosX')
        ValPosY = builder.get_object('ValPosY')
        ValNegX = builder.get_object('ValNegX')
        ValNegY = builder.get_object('ValNegY')
        Centerresult = builder.get_object('Centerresult')
        Feedrate_scale = builder.get_object('hscale1')
        feedrate = getattr(s, 'max_velocity')
        C3PX1 = builder.get_object('C3PX1')
        C3PY1 = builder.get_object('C3PY1')
        C3PZ1 = builder.get_object('C3PZ1')
        C3PX2 = builder.get_object('C3PX2')
        C3PY2 = builder.get_object('C3PY2')
        C3PZ2 = builder.get_object('C3PZ2')
        C3PX3 = builder.get_object('C3PX3')
        C3PY3 = builder.get_object('C3PY3')
        C3PZ3 = builder.get_object('C3PZ3')
        C3PCenter = builder.get_object('C3PCenter')
        C3PRadius = builder.get_object('C3PRadius')

        window = builder.get_object("window1")
        comboincrement = builder.get_object('Increments')
        gobject.timeout_add(100, self.updateValues)
        comboincrement.set_active(2)
        try:
            config = ConfigParser.ConfigParser()
            config.read('Wizards.ini')
            Centerresult.set_text(config.get('ManualCenter', 'Centerresult'))
            ValPosX.set_text(config.get('ManualCenter', 'ValPosX'))
            ValPosY.set_text(config.get('ManualCenter', 'ValPosY'))
            ValNegX.set_text(config.get('ManualCenter', 'ValNegX'))
            ValNegY.set_text(config.get('ManualCenter', 'ValNegY'))
            C3PCenter.set_text (config.get('Center3P', 'Center'))
            C3PRadius.set_text (config.get('Center3P', 'Radius'))
        except IOError:
            Centerresult.set_text('')
            ValPosX.set_text('')
            ValPosY.set_text('')
            ValNegX.set_text('')
            ValNegY.set_text('')

        window.set_keep_above(True)
        window.show_all()

    def on_GetP1_clicked(self, *args):
        s.poll()
        C3PX1.set_text("{:6.3f}".format(s.position[0] - s.g5x_offset[0]))
        C3PY1.set_text("{:6.3f}".format(s.position[1] - s.g5x_offset[1]))
        C3PZ1.set_text("{:6.3f}".format(s.position[2] - s.g5x_offset[2]))

    def on_GetP2_clicked(self, *args):
        s.poll()
        C3PX2.set_text("{:6.3f}".format(s.position[0] - s.g5x_offset[0]))
        C3PY2.set_text("{:6.3f}".format(s.position[1] - s.g5x_offset[1]))
        C3PZ2.set_text("{:6.3f}".format(s.position[2] - s.g5x_offset[2]))

    def on_GetP3_clicked(self, *args):
        s.poll()
        C3PX3.set_text("{:6.3f}".format(s.position[0] - s.g5x_offset[0]))
        C3PY3.set_text("{:6.3f}".format(s.position[1] - s.g5x_offset[1]))
        C3PZ3.set_text("{:6.3f}".format(s.position[2] - s.g5x_offset[2]))

    def on_C3PCalc_clicked(self,*args):
        A = np.array([float(C3PX1.get_text()), float(C3PY1.get_text()), float(C3PZ1.get_text())])
        B = np.array([float(C3PX2.get_text()), float(C3PY2.get_text()), float(C3PZ2.get_text())])
        C = np.array([float(C3PX3.get_text()), float(C3PY3.get_text()), float(C3PZ3.get_text())])
        a = np.linalg.norm(C - B)
        b = np.linalg.norm(C - A)
        c = np.linalg.norm(B - A)
        s = (a + b + c) / 2
        R = a*b*c / 4 / np.sqrt(s * (s - a) * (s - b) * (s - c))
        b1 = a*a * (b*b + c*c - a*a)
        b2 = b*b * (a*a + c*c - b*b)
        b3 = c*c * (a*a + b*b - c*c)
        P = np.column_stack((A, B, C)).dot(np.hstack((b1, b2, b3)))
        P /= b1 + b2 + b3
        C3PCenter.set_text("[X%s Y%s Z%s]"%("{:6.3f}".format(P[0]),"{:6.3f}".format(P[1]),"{:6.3f}".format(P[2])))
        C3PRadius.set_text("{:6.3f}".format(R))
    def on_C3PGotoCenter_clicked(self,*args):
        c.mode(linuxcnc.MODE_MDI)
        c.wait_complete()
        c.mdi("G0 %s" % (C3PCenter.get_text().split("[")[1].split("]")[0]))


    def updateValues(self):
        s.poll()
        XVal_label.set_text("{:6.3f}".format(s.position[0] - s.g5x_offset[0]))
        YVal_label.set_text("{:6.3f}".format(s.position[1] - s.g5x_offset[1]))
        return True

    def gtk_main_quit(self, *args):
        gtk.main_quit(*args)

    def on_PosX_clicked(self, *args):
        self.Jogaxis(self.axis.X, self.Direction.Pos)

    def on_NegX_clicked(self, *args):
        self.Jogaxis(self.axis.X, self.Direction.Neg)

    def on_PosY_clicked(self, *args):
        self.Jogaxis(self.axis.Y, self.Direction.Pos)

    def on_NegY_clicked(self, *args):
        self.Jogaxis(self.axis.Y, self.Direction.Neg)

    def Jogaxis(self, axis, direction):

        c.jog(linuxcnc.JOG_INCREMENT, False, axis, float(Feedrate_scale.get_value()),
              direction * float(comboincrement.get_active_text()))


    def on_button1_clicked(self, *args):
        s.poll()
        ValPosX.set_text("{:6.3f}".format(s.position[0] - s.g5x_offset[0]))

    def on_button2_clicked(self, *args):
        s.poll()
        ValNegX.set_text("{:6.3f}".format(s.position[0] - s.g5x_offset[0]))

    def on_button3_clicked(self, *args):
        s.poll()
        ValPosY.set_text("{:6.3f}".format(s.position[1] - s.g5x_offset[1]))

    def on_button4_clicked(self, *args):
        s.poll()
        ValNegY.set_text("{:6.3f}".format(s.position[1] - s.g5x_offset[1]))

    def on_window1_key_press_event(self, widget, ev, data=None):
        if ev.keyval == 65363:
            self.on_PosX_clicked()
        elif ev.keyval == 65361:
            self.on_NegX_clicked()
        elif ev.keyval == 65362:
            self.on_PosY_clicked()
        elif ev.keyval == 65364:
            self.on_NegY_clicked()
        elif ev.keyval == 65307:
            self.gtk_main_quit()
        else:
            None
            # print ev.keyval

    def on_Manual_clicked(self, *args):
        c.mode(linuxcnc.MODE_MANUAL)
        c.wait_complete()

    def on_center_clicked(sef, *args):
        ValueposX = 0.0 if ValPosX.get_text() == '' else float(ValPosX.get_text())
        ValueposY = 0.0 if ValPosY.get_text() == '' else float(ValPosY.get_text())
        ValueNegX = 0.0 if ValNegX.get_text() == '' else float(ValNegX.get_text())
        ValueNegY = 0.0 if ValNegY.get_text() == '' else float(ValNegY.get_text())
        CenterX = np.median([ValueposX, ValueNegX])
        CenterY = np.median([ValueposY, ValueNegY])
        Centerresult.set_text("[X%s Y%s]" % ("{:6.3f}".format(CenterX), "{:6.3f}".format(CenterY)))

    def on_GoCenter_clicked(self, *args):
        c.mode(linuxcnc.MODE_MDI)
        c.wait_complete()
        c.mdi("G0 %s" % (Centerresult.get_text().split("[")[1].split("]")[0]))

    def on_hscale1_change_value(self, *args):

        """ Function doc """

    def on_GoCenterX_clicked(self, *args):
        c.mode(linuxcnc.MODE_MDI)
        c.wait_complete()
        c.mdi("G0%s" % (Centerresult.get_text().split("[")[1].split(" Y")[0]))

    def on_GoCenterY_clicked(self, *args):
        c.mode(linuxcnc.MODE_MDI)
        c.wait_complete()
        c.mdi("G0Y%s" % (Centerresult.get_text().split("Y")[1].split("]")[0]))


try:
    s = linuxcnc.stat()  # create a connection to the status channel
    s.poll()  # get current values
    c = linuxcnc.command()
    WizardsApp()
    gtk.main()
except linuxcnc.error, detail:
    print "error", detail
    sys.exit(1)


def savedata():
    config = ConfigParser.RawConfigParser()
    config.add_section('ManualCenter')
    config.set('ManualCenter', 'Centerresult', Centerresult.get_text())
    config.set('ManualCenter', 'ValPosX', ValPosX.get_text())
    config.set('ManualCenter', 'ValPosY', ValPosY.get_text())
    config.set('ManualCenter', 'ValNegX', ValNegX.get_text())
    config.set('ManualCenter', 'ValNegY', ValNegY.get_text())
    config.add_section('Center3P')
    config.set('Center3P', 'Center', C3PCenter.get_text())
    config.set('Center3P', 'Radius', C3PRadius.get_text())
    with open("Wizards.ini", "w") as outfile:
        config.write(outfile)


import atexit

atexit.register(savedata)
