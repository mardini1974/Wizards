# Wizards
Linuxcnc Wizards for common operation
This is my approch for things i didn't find in Linuxcnc.
Btw I'm not a real programmer, so my code will look buggy .  
# Installation
copy both files : 
  1. Wizards.py
  2. Wizards.glade
  
To a directory of your choice 
    
    chmod +x Wizards.py 
To make it executable or run from any editor with run cabablity.
make sure Linuxcnc is running and your machine is homed and ready for normmal operation.
start Wizards.py :
    
    in Terminal : ./Wizards.py
    or Double click from file manager.
    or from (for example open Geany and press F5 to run program ).
    
# Circle Center:

  This wizards is used to find center of a circle in manual mode ( if you don' have a touch probe). of course it can be used for other shapes.
  
  Just move the tool ( or visual touch probe) until you get a touch on one side ( for example on X axe to the right) then press ("+X" button) to save X value, then move to the opposit direction till you get a touch then press ("-X" button).

Go back to middle ( eye sight ) then repat on the Y axe.

**Important!! _click on "Calc. Center"_ to display the center coordinates.**

You can click on ("Goto Center X" button) to move to the center then repeat for Y  axe ("Goto Center Y" button)or you can move directly to the center ("Goto Center" button).

You can use  the arrow buttons on the wizards for movement or your manual buttons on Linuxcnc program.
speed of movement can be changed through a speed slider [0% .. 100%] of your max velcity (linuxcnc ini file)
increments can be selected for movement ( no Continous movement!! ) be carefull not to use it in linuxcnc screen.

You can use key board keys for movement. 

To quit click stop or press Esc on you keyboard.
```
  Tip:  if you don't have a visual touch probe you can use any tool at very low speed ( 10-30 rpm)  that fits in the  circle's pocket and and use a strip of paper between the tool and the material move until the paper is scratched by the tool.  
```
   
The program will be in fornt of other screens till you finish the operation.
