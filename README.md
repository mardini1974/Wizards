# Wizards
Linuxcnc Wizards for common operation
This is my approch for things i didn't find in Linuxcnc, and i found other options are too hard to install ( modifing the ini, changing and adding Paths) .
Btw I'm not a real programmer, so my code will look buggy .  
# Installation
copy both files : 
  1. Wizards.py or Wizards2.8.py
  2. Wizards.glade
  
To a directory of your choice (Better in your ngc folder for quick access) 
    
    chmod +x Wizards.py(Wizards2.8.py) 
To make it executable or run from any editor with run capability.
Make sure Linuxcnc is running and your machine is homed and ready for normal operation.
# Running Wizards :
    
    in Terminal : ./Wizards.py or ./Wizards2.8.py
    or in Linuxcnc open the file (Wizard.py or Wizard2.8.py ) Yes Linuxcnc by default can open python files.
    or Double click from file manager.
    or from (for example open Geany and press F5 to run program ).
    
# Circle Center:

  This wizards is used to find center of a circle in manual mode ( if you don' have a touch probe). of course it can be used for other shapes.
  
  Just move the tool ( or visual touch probe) until you get a touch on one side ( for example on X axe to the right) then press ("+X" button) to save X value, then move to the opposit direction till you get a touch then press ("-X" button).

Go back to middle ( eye sight ) then repeat on the Y axe.

**Important!! _click on "Calc. Center"_ to display the center coordinates.**

You can click on ("Go to Center X" button) to move to the center then repeat for Y  axe ("Go to Center Y" button)or you can move directly to the center ("Goto Center" button).

You can use  the arrow buttons on the wizards for movement or your manual buttons on Linuxcnc program.
speed of movement can be changed through a speed slider [0% .. 100%] of your max velocity (Linuxcnc ini file)
increments can be selected for movement ( no Continuous movement!! ) be careful not to use it in Linuxcnc screen.

You can use key board keys for movement. 

To quit click stop or press Esc on you keyboard.
```
  Tip:  if you don't have a visual touch probe you can use any tool at very low speed ( 10-30 rpm)  that fits in the  circle's pocket and and use a strip of paper between the tool and the material move until the paper is scratched by the tool.  
```
# Center 3 points
 To find center of circle using 3 point make a touch on three different points, preferably as far as possible to get accurate results.
 this can work on arcs , be careful very near points can give wrong center.

The program will be in front of other screens till you finish the operation.
