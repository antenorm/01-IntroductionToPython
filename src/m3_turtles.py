"""
Demonstrates using OBJECTS via Turtle Graphics.

Concepts include:
  -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
  -- Make an object   ** DO **   something by using a METHOD.
  -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.

Also:
  -- ASSIGNING a VALUE to a NAME (VARIABLE).

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ryan Antenore.
"""
###############################################################################
#
# Done: 1.
#   Yes, that means for YOU to DO things per the following instructions:
#
#   On Line 13 above, replace  PUT_YOUR_OWN_NAME_HERE  with your OWN name.
#
#   BTW, the top block of text above forms what is called a DOC-STRING.
#   It documents what this module does, in a way that exterior programs
#   can make sense of.  It has no other effect on this program.
#
###############################################################################

import rosegraphics as rg

###############################################################################
#
# Done: 2.
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
#
#   You will see that  rosegraphics  in the  import  statement above (line 28)
#   is no longer marked as an error.  You will do this
#      Select the  src  folder, then  Mark Directory As ~ Sources Root
#   in all projects that use rosegraphics, so get used to it. :)
#
#   Once  rosegraphics  in the  import  statement is no longer marked
#   as an error, change the above TO-DO to DONE and coninue to the next TO-DO.
#
###############################################################################

###############################################################################
#
# Done: 3.
#   Run this module.  A window will pop up and Turtles will move around.
#   After the Turtles stop moving, *click anywhere in the window to close it*.
#
#   Then look at the code below.  Raise your hand when you have questions about
#   what the code is doing.  Be sure that you understand the notations for:
#     -- CONSTRUCTING an instance of a CLASS, e.g.
#           rg.SimpleTurtle()
#     -- ASSIGNING the resulting OBJECT (instance of a class) a NAME, e.g.
#           natasha = rg.SimpleTurtle()
#     -- Applying a METHOD to an object to make the object DO something, e.g.
#           natasha.forward(100)
#     -- Accessing an INSTANCE VARIABLE of an object, e.g.
#           natasha.speed = 10
#           print(boris.speed)
#
#   After you are confident that you understand all the code below,
#   change this TO-DO to DONE and  ** continue to the next TOD-DO (below). **
#
###############################################################################

# -----------------------------------------------------------------------------
# CONSTRUCT (make) a   TurtleWindow   object and set it up for animation.
# The definition of a  TurtleWindow  is in the   rg  (shorthand for
# rosegraphics) module.
# -----------------------------------------------------------------------------
window = rg.TurtleWindow()
window.delay(20)  # Bigger numbers mean slower animation.

# -----------------------------------------------------------------------------
# CONSTRUCT (make) a  SimpleTurtle  object and ASSIGN a NAME to the object.
# -----------------------------------------------------------------------------
boris = rg.SimpleTurtle()

# -----------------------------------------------------------------------------
# Ask the SimpleTurtle object to do things by applying METHODs to it:
# -----------------------------------------------------------------------------
boris.forward(100)
boris.left(90)
boris.forward(200)

# -----------------------------------------------------------------------------
# Construct a second SimpleTurtle,
# set its  pen  and  speed  INSTANCE VARIABLES, and ask it to do things.
# -----------------------------------------------------------------------------
natasha = rg.SimpleTurtle('turtle')
natasha.pen = rg.Pen('red', 30)  # Second argument is the Pen's thickness
natasha.speed = 10  # Faster

natasha.backward(50)
natasha.right(90)
natasha.forward(50)
natasha.right(45)
natasha.forward(75)
natasha.right(45)
natasha.forward(200)
###############################################################################
#
# Done: 4.
#   Add a few more line of your own code to make one of the
#   existing SimpleTurtles move some more and/or have different
#   characteristics.
#
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
###############################################################################
ryan = rg.SimpleTurtle()
ryan.pen = rg.Pen('blue', '20')
ryan.forward(200)
ryan.left(90)
ryan.backward(200)

###############################################################################
#
# Done: 5.
#   The above code  CONSTRUCTS  two SimpleTurtle objects
#   and gives those objects NAMES:
#       boris    natasha
#
#   Add code of your own that constructs another SimpleTurtle object,
#   naming it whatever you want.  Names cannot have spaces or special
#   characters, but they can have digits and underscores, e.g.
#      this_1_has
#
#   STYLE RULE: Your names should always begin with a LOWER_CASE letter.
#   So   mary   is OK but   Mary   is NOT OK.
#
#   Then add a few more lines that:
#     -- Constructs a Pen object,
#     -- assigns your SimpleTurtle's  pen  to the constructed Pen object, and
#     -- makes your SimpleTurtle move around a bit.
#
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
###############################################################################

###############################################################################
#
# Done: 6.
#   Run one more time to be sure that all is still OK.
#   Ensure that no blue bars on the scrollbar-thing to the right remain.
#
#   Then COMMIT-and-PUSH your work as before:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up:
#          - HOVER over the  Commit  button
#              (in the lower-right corner of the window)
#          - CLICK on  Commit and Push.
#
#   You can COMMIT-and-PUSH as often as you like.  DO IT FREQUENTLY.
#
###############################################################################

# -----------------------------------------------------------------------------
# The next line keeps the window open until the user clicks in the window.
# Throughout this exercise, this  close_on_mouse_click   line should be the
# LAST line in the file.  DO NOT ADD CODE BELOW THIS LINE!
# -----------------------------------------------------------------------------
window.close_on_mouse_click()
