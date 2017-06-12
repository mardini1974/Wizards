#!/usr/bin/python

import sys
import linuxcnc
import time
import gtk,gtk.gdk
import numpy as np


	
		
		
class WizardsApp (gtk.Window):
	class axis (object):
		X=0
		Y=1
		Z=2
	class Direction (object):
		Pos = 1
		Neg = -1	
	XVal_label = gtk.Label()
	YVal_label = gtk.Label()
	ValPosX = gtk.Label()
	ValPosY = gtk.Label()
	ValNegX = gtk.Label()
	ValNegY = gtk.Label()
	Centerresult = gtk.Label()
	comboincrement = gtk.ComboBox()
	Feedrate_scale = gtk.HScale()
	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("Wizards.glade")
		builder.connect_signals(self)
		global XVal_label 
		global YVal_label
		global ValPosX 
		global ValPosY 
		global ValNegX 
		global ValNegY
 		global Centerresult 
		global feedrate
		global comboincrement
		global Feedrate_scale
		XVal_label = builder.get_object('XVal')
		YVal_label = builder.get_object('YVal')
		ValPosX = builder.get_object('ValPosX')
		ValPosY = builder.get_object('ValPosY')
		ValNegX = builder.get_object('ValNegX')
		ValNegY = builder.get_object('ValNegY')
		Centerresult = builder.get_object('Centerresult')
		Feedrate_scale = builder.get_object('hscale1')
		feedrate = getattr(s,'max_velocity')
		window = builder.get_object("window1")
		comboincrement = builder.get_object( 'Increments')
		comboincrement.set_active(2)
		window.set_keep_above (True)
		window.show_all()
	

			
	def gtk_main_quit(self, *args):
		gtk.main_quit(*args)
	
	def on_PosX_clicked (self,*args):
		self.Jogaxis(self.axis.X,self.Direction.Pos)
		
	def on_NegX_clicked (self,*args):
		self.Jogaxis(self.axis.X,self.Direction.Neg)
		
	def on_PosY_clicked (self,*args):
		self.Jogaxis(self.axis.Y,self.Direction.Pos)
		
	def on_NegY_clicked (self,*args):
		self.Jogaxis(self.axis.Y,self.Direction.Neg)
		
	def Jogaxis (self,axis,direction):
		print int(Feedrate_scale.get_value())
		c.jog(linuxcnc.JOG_INCREMENT,axis,int(Feedrate_scale.get_value()),direction*float(comboincrement.get_active_text()))
		c.wait_complete()
		s.poll()
		XVal_label.set_text ("{:6.3f}".format(s.axis[0]['output']))
		YVal_label.set_text ("{:6.3f}".format(s.axis[1]['output']))
	def on_button1_clicked (self,*args):
		s.poll()
		ValPosX.set_text ("{:6.3f}".format(s.axis[0]['output']))
	def on_button2_clicked (self,*args):
		s.poll()
		ValNegX.set_text ("{:6.3f}".format(s.axis[0]['output']))	
		
	def on_button3_clicked (self,*args):
		s.poll()
		ValPosY.set_text ("{:6.3f}".format(s.axis[1]['output']))
	def on_button4_clicked (self,*args):
		s.poll()
		ValNegY.set_text ("{:6.3f}".format(s.axis[1]['output']))	
	def on_window1_key_press_event (self,widget,ev, data=None):
		if  ev.keyval==65363:
			self.on_PosX_clicked()
		elif ev.keyval == 65361:
			self.on_NegX_clicked ()
		elif ev.keyval == 65362:
			self.on_PosY_clicked()
		elif ev.keyval == 65364:
			self.on_NegY_clicked ()
		elif ev.keyval == 65307:
			self.gtk_main_quit()
		else :
			None
			#print ev.keyval
	def on_Manual_clicked (self,*args):
		c.mode(linuxcnc.MODE_MANUAL)
		c.wait_complete()
	def on_center_clicked (sef,*args):
		ValueposX= 0.0 if ValPosX.get_text() == '' else float(ValPosX.get_text())
		ValueposY= 0.0 if ValPosY.get_text() == '' else float(ValPosY.get_text())
		ValueNegX= 0.0 if ValNegX.get_text() == '' else float(ValNegX.get_text())
		ValueNegY= 0.0 if ValNegY.get_text() == '' else float(ValNegY.get_text())
		CenterX= np.median([ValueposX,ValueNegX])
		CenterY = np.median ([ValueposY,ValueNegY])
		Centerresult.set_text("[X%s Y%s]"%("{:6.3f}".format(CenterX),"{:6.3f}".format(CenterY)))
	def on_GoCenter_clicked (self,*args):
		c.mode(linuxcnc.MODE_MDI)
		c.wait_complete()
		c.mdi("F%s G1 %s"%("{:3.0f}".format(Feedrate_scale.get_value()),Centerresult.get_text().split("[")[1].split("]")[0]))
	def on_hscale1_change_value (self,*args):
		
		""" Function doc """
	def on_GoCenterX_clicked (self,*args):
		c.mode(linuxcnc.MODE_MDI)
		c.wait_complete()
		c.mdi("F%sG1%s"%("{:3.0f}".format(Feedrate_scale.get_value()),Centerresult.get_text().split("[")[1].split(" Y")[0]))
		
	def on_GoCenterY_clicked (self,*args):
		c.mode(linuxcnc.MODE_MDI)
		c.wait_complete()
		c.mdi("F%sG1Y%s"%("{:3.0f}".format(Feedrate_scale.get_value()),Centerresult.get_text().split("Y")[1].split("]")[0]))
		
			
			
	
		

			
		
try:		
	s = linuxcnc.stat() # create a connection to the status channel
	s.poll() # get current values
	c = linuxcnc.command()
	WizardsApp()
	gtk.main()
except linuxcnc.error, detail:
	print "error", detail
	sys.exit(1)

