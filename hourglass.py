###############################################################################
#  Title:         hourglass.py                                                #
#  Author:        Paul Lack                                                   #
#  Date Created:  4/2/21                                                      #
#                                                                             #
#  Purpose:  The purpose of this program is to graphically simulate an hour-  #
#            glass on a terminal screen.  The user can enter a number of      #  
#            minutes from 1-60.  Falling 'sand' shows it is working.  The sand#
#            levels change at quarterly invervals of the time selected.       #
############################################################################### 



#  import system from os which allows the ability to clear the screen.
from os import system, name
# import sleep to allow 'frames' to persist for a specified time interval.
from time import sleep
# import datetime to allow storing necessary systme time variables.
from datetime import datetime
###############################################################################
#  Define the top of a full hourglass.
top_full=        ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X     ....                              .......X      ',
                  '        X .........        ........    ............X        ',
                  '          X .....................................X          ',
                  '            X .................................X            ',
                  '               X ...........................X               ',
                  '                  X .....................X                  ',
                  '                     X ...............X                     ',
                  '                       X ...........X                       ',
                  '                         X .......X                         ',
                  '                           X ...X                           ',
                  '                            X .X                            ']
#################################################################################
# Define the top of an almost full hourglass.
top_3Q_full=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X      ..                             .....X        ',
                  '          X .....................................X          ',
                  '            X .................................X            ',
                  '               X ...........................X               ',
                  '                  X .....................X                  ',
                  '                     X ...............X                     ',
                  '                       X ...........X                       ',
                  '                         X .......X                         ',
                  '                           X ...X                           ',
                  '                            X .X                            ']
#################################################################################
# Define the top of a half full hourglass.
top_2Q_full=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                     .....  X               ',
                  '                  X .....................X                  ',
                  '                     X ...............X                     ',
                  '                       X ...........X                       ',
                  '                         X .......X                         ',
                  '                           X ...X                           ',
                  '                            X .X                            ']
#################################################################################
# Define the top of a mostly empty hourglass.
top_1Q_full=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X ...........X                       ',
                  '                         X .......X                         ',
                  '                           X ...X                           ',
                  '                            X .X                            ']
#################################################################################
# Define the top of a completly empty hourglass.
top_finished=    ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  ' X                                                        X ',
                  '  X                                                      X  ',
                  '  X                      FINISHED!                       X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            ']
#################################################################################
#  Define the bottom of a mostly empty hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to 'draw' it 
#  correctly using a list.  Shows the first of three falling sand 'animations'.
bottom_empty_1=  ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                   ..................                   X ',
                  ' X                      ............                      X ',
                  ' X                          ....                          X ',
                  ' X                           .                            X ',
                  '  X                           .                          X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                           .                        X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                  .                   X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X      .     X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a mostly empty hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to 'draw' it 
#  correctly using a list.  Shows the second of three falling sand 'animations'. 
bottom_empty_2=  ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                   ..................                   X ',
                  ' X                      ............                      X ',
                  ' X                          ....                          X ',
                  ' X                           .                            X ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                           .                          X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                        .                     X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X           .          X                  ',
                  '                     X                X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a mostly empty hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to 'draw' it 
#  correctly using a list.  Shows the last of three falling sand 'animations'. 
bottom_empty_3=  ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X                   ..................                   X ',
                  ' X                      ............                      X ',
                  ' X                          ....                          X ',
                  ' X                           .                            X ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                          .                         X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                     .                    X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X        .       X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################   
#  Define the bottom of a mostly one quarter full hourglass in an inverted 
#  format with falling sand.  It is easier to flip it programatically than to 
#  draw it correctly.  Shows the first of three falling sand 'animations'. 
bottom_1Q_1=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X              ..........................                X ',
                  ' X                   .................                    X ',
                  ' X                      ...........                       X ',
                  ' X                         .....                          X ',
                  '  X                         ...                          X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                                                    X   ',
                  '   X                           .                        X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                  .                   X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X      .     X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a mostly one quarter full hourglass in an inverted 
#  format with falling sand.  It is easier to flip it programatically than to 
#  draw it correctly.  Shows the second of three falling sand 'animations'. 
bottom_1Q_2=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X              ..........................                X ',
                  ' X                   .................                    X ',
                  ' X                      ...........                       X ',
                  ' X                         .....                          X ',
                  '  X                         ...                          X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                           .                          X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                        .                     X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X           .          X                  ',
                  '                     X                X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a mostly one quarter full hourglass in an inverted 
#  format with falling sand.  It is easier to flip it programatically than to 
#  draw it correctly.  Shows the last of three falling sand 'animations'.  
bottom_1Q_3=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X              ..........................                X ',
                  ' X                   .................                    X ',
                  ' X                      ...........                       X ',
                  ' X                         .....                          X ',
                  '  X                         ...                          X  ',
                  '  X                                                      X  ',
                  '  X                                                      X  ',                  
                  '  X                                                      X  ',
                  '   X                          .                         X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                     .                    X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X        .       X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################  
#  Define the bottom of a half empty hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  Shows the first of three falling sand 'animations'.
bottom_2Q_1=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X      ............................................      X ',
                  ' X            ...............................             X ',
                  ' X                  ....................                  X ',
                  '  X                      ...........                     X  ',
                  '  X                         ......                       X  ',
                  '  X                          ...                         X  ',                  
                  '  X                           .                          X  ',
                  '   X                                                    X   ',
                  '   X                           .                        X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                  .                   X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X      .     X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a half empty hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  Shows the second of three falling sand 'animations'. 
bottom_2Q_2=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X      ............................................      X ',
                  ' X            ...............................             X ',
                  ' X                  ....................                  X ',
                  '  X                      ...........                     X  ',
                  '  X                         ......                       X  ',
                  '  X                          ...                         X  ',                  
                  '  X                           .                          X  ',
                  '   X                                                    X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                        .                     X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X           .          X                  ',
                  '                     X                X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a half empty hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  Shows the last of three falling sand 'animations'.   
bottom_2Q_3=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X      ............................................      X ',
                  ' X            ...............................             X ',
                  ' X                  ....................                  X ',
                  '  X                      ...........                     X  ',
                  '  X                         ......                       X  ',
                  '  X                          ...                         X  ',                  
                  '  X                           .                          X  ',
                  '   X                          .                         X   ',
                  '   X                                                    X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                     .                    X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X        .       X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################    
#  Define the bottom of a mostly full hour glass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  Shows the first of three falling sand 'animations'. 
bottom_3Q_1=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X .......................................................X ',
                  ' X    ..................................................  X ',
                  ' X         ......................................         X ',
                  '  X              ..........................              X  ',
                  '  X                   ................                   X  ',
                  '  X                      ..........                      X  ',                  
                  '  X                        ......                        X  ',
                  '   X                         ...                        X   ',
                  '   X                          .                         X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                  .                   X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X      .     X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a mostly full hour glass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  Shows the second of three falling sand 'animations'. 
bottom_3Q_2=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X .......................................................X ',
                  ' X    ..................................................  X ',
                  ' X         ......................................         X ',
                  '  X              ..........................              X  ',
                  '  X                   ................                   X  ',
                  '  X                      ..........                      X  ',                  
                  '  X                        ......                        X  ',
                  '   X                         ...                        X   ',
                  '   X                          .                         X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                        .                     X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X           .          X                  ',
                  '                     X                X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################
#  Define the bottom of a mostly full hour glass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  Shows the last of three falling sand 'animations'. 
bottom_3Q_3=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X .......................................................X ',
                  ' X    ..................................................  X ',
                  ' X         ......................................         X ',
                  '  X              ..........................              X  ',
                  '  X                   ................                   X  ',
                  '  X                      ..........                      X  ',                  
                  '  X                        ......                        X  ',
                  '   X                         ...                        X   ',
                  '   X                          .                         X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                     .                    X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X        .       X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
#################################################################################    
#  Define the bottom of a full hourglass in an inverted format with 
#  falling sand.  It is easier to flip it programatically than to draw it 
#  correctly.  
bottom_full=     ['============================================================',
                  '||                                                        ||',
                  '============================================================',
                  ' X .......................................................X ',
                  ' X .......................................................X ',
                  ' X .......................................................X ',
                  ' X ...................................................... X ',
                  '  X......................................................X  ',
                  '  X     ..........................................       X  ',
                  '  X             ...........................              X  ',                  
                  '  X                    .............                     X  ',
                  '   X                       ......                       X   ',
                  '   X                         ..                         X   ',
                  '    X                                                  X    ',
                  '     X                                                X     ',
                  '      X                                              X      ',
                  '        X                                          X        ',
                  '          X                                      X          ',
                  '            X                                  X            ',
                  '               X                            X               ',
                  '                  X                      X                  ',
                  '                     X                X                     ',
                  '                       X            X                       ',
                  '                         X        X                         ',
                  '                           X    X                           ',
                  '                            X  X                            '] 
################################################################################# 
#  Function Name:  clear()                                                      #
#  Purpose:        Clears the terminal window for Windows, Linux, or Mac users. #                                             
#################################################################################
def clear():
# for windows
    if name == 'nt':
        _ = system('cls')
# for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
################################################################################# 
#  Function Name:  start_frame_1()                                              #
#  Purpose:        Displays the first frame of the first quarter interval.      #                                             
#################################################################################
def start_frame_1():
	#  Print each string in the 'top_full' list to the console.
    for line in top_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_empty_1)
    x=0
    for line in bottom_empty_1:
	    print(bottom_empty_1[length-1-x])
	    x=x+1
################################################################################# 
#  Function Name:  start_frame_2()                                              #
#  Purpose:        Displays the second frame of the first quarter interval.     #                                             
#################################################################################
def start_frame_2():
	#  Print each string in the 'top_full' list to the console.
    for line in top_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_empty_2)
    x=0
    for line in bottom_empty_2:
	    print(bottom_empty_2[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  start_frame_3()                                              #
#  Purpose:        Displays the third frame of the first quarter interval.      #                                             
#################################################################################
def start_frame_3():
	#  Print each string in the 'top_full' list to the console.
    for line in top_full:
        print(line)

#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_empty_3)
    x=0
    for line in bottom_empty_3:
	    print(bottom_empty_3[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  second_frame_1()                                             #
#  Purpose:        Displays the first frame of the first second interval.       #                                             
#################################################################################
def second_frame_1():
	#  Print each string in the 'top_full' list to the console.
    for line in top_3Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_1Q_1)
    x=0
    for line in bottom_1Q_1:
	    print(bottom_1Q_1[length-1-x])
	    x=x+1
################################################################################# 
#  Function Name:  second_frame_2()                                             #
#  Purpose:        Displays the second frame of the second interval.            #                                             
#################################################################################
def second_frame_2():
	#  Print each string in the 'top_full' list to the console.
    for line in top_3Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_1Q_2)
    x=0
    for line in bottom_1Q_2:
	    print(bottom_1Q_2[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  second_frame_3()                                             #
#  Purpose:        Displays the third frame of the second interval.             #                                             
#################################################################################
def second_frame_3():
	#  Print each string in the 'top_full' list to the console.
    for line in top_3Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_1Q_3)
    x=0
    for line in bottom_1Q_3:
	    print(bottom_1Q_3[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  third_frame_1()                                              #
#  Purpose:        Displays the first frame of the third interval.              #                                             
#################################################################################
def third_frame_1():
	#  Print each string in the 'top_full' list to the console.
    for line in top_2Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_2Q_1)
    x=0
    for line in bottom_2Q_1:
	    print(bottom_2Q_1[length-1-x])
	    x=x+1
################################################################################# 
#  Function Name:  third_frame_2()                                              #
#  Purpose:        Displays the second frame of the third interval.             #                                             
#################################################################################
def third_frame_2():
	#  Print each string in the 'top_full' list to the console.
    for line in top_2Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_2Q_2)
    x=0
    for line in bottom_2Q_2:
	    print(bottom_2Q_2[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  third_frame_3()                                              #
#  Purpose:        Displays the third frame of the third interval.              #                                             
#################################################################################
def third_frame_3():
	#  Print each string in the 'top_full' list to the console.
    for line in top_2Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_2Q_3)
    x=0
    for line in bottom_2Q_3:
	    print(bottom_2Q_3[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  fourth_frame_1()                                             #
#  Purpose:        Displays the first frame of the fourth interval.             #                                             
#################################################################################
def fourth_frame_1():
	#  Print each string in the 'top_full' list to the console.
    for line in top_1Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_3Q_1)
    x=0
    for line in bottom_3Q_1:
	    print(bottom_3Q_1[length-1-x])
	    x=x+1
################################################################################# 
#  Function Name:  fourth_frame_2()                                             #
#  Purpose:        Displays the second frame of the fourth interval.            #                                             
#################################################################################
def fourth_frame_2():
	#  Print each string in the 'top_full' list to the console.
    for line in top_1Q_full:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_3Q_2)
    x=0
    for line in bottom_3Q_2:
	    print(bottom_3Q_2[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  fourth_frame_3()                                             #
#  Purpose:        Displays the third frame of the fourth interval.             #                                             
#################################################################################
def fourth_frame_3():
	#  Print each string in the 'top_full' list to the console.
    for line in top_1Q_full:
        print(line)

#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_3Q_3)
    x=0
    for line in bottom_3Q_3:
	    print(bottom_3Q_3[length-1-x])
	    x=x+1	
################################################################################# 
#  Function Name:  finished_frame()                                             #
#  Purpose:        Displays the last frame of the entire sequence               #                                             
#################################################################################
def finished_frame():
	#  Print each string in the 'top_full' list to the console.
    for line in top_finished:
        print(line)
#  Get the length of the list and use it to print each string in the 
#  'bottom_empty' list from the end of the list in reverse order.
    length=len(bottom_full)
    x=0
    for line in bottom_full:
	    print(bottom_full[length-1-x])
	    x=x+1	
###############################################################################
# Set the speed of the falling sand.
speed=.25
# Get time number of minutes from the user (1-60 are valid).  
time_set = input('Enter the number of minutes from 1-60.  ')
# Create variables to hold all the necessary time variable.
# 'interval_time' divides the user input time into four segments for use later.
interval_time=int(time_set)/4
now = datetime.now()
start_hour = int(now.strftime("%H"))
start_minute = int(now.strftime("%M"))
start_second = int(now.strftime("%S"))
first_quarter_end_second = int(now.strftime("%S"))
# Set all the interval end times correctly depending on the value the user
# entered.  When minutes > 60, roll minutes back to 0 and increment the hour.
if start_minute+interval_time<60:
    first_quarter_end_minute=start_minute+interval_time
    first_quarter_end_hour=start_hour
else:
	first_quarter_end_minute=start_minute+interval_time-60
	first_quarter_end_hour=start_hour+1
second_quarter_end_second = int(now.strftime("%S"))
if start_minute+(interval_time*2)<60:
    second_quarter_end_minute=start_minute+(interval_time*2)
    second_quarter_end_hour=start_hour
else:
	second_quarter_end_minute=start_minute+(interval_time*2)-60
	second_quarter_end_hour=start_hour+1
third_quarter_end_second = int(now.strftime("%S"))
if start_minute+(interval_time*3)<60:
    third_quarter_end_minute=start_minute+(interval_time*3)
    third_quarter_end_hour=start_hour
else:
	third_quarter_end_minute=start_minute+(interval_time*3)-60
	third_quarter_end_hour=start_hour+1		
end_second = int(now.strftime("%S"))
if int(time_set)==60:
	end_minute=start_minute
	end_hour=start_hour+1
else: 
	end_minute=start_minute+int(time_set)
	end_hour=start_hour
if int(time_set)>=1 and int(time_set)<=60:
    now_minute = int(now.strftime("%M"))
    now_second = int(now.strftime("%S"))
# Run the appropriate three frame sequence while the current system time is 
# within the first of the four interval segments.    
    while now_minute<=first_quarter_end_minute:
        clear()
        start_frame_1()
        sleep(speed)
        clear()
        start_frame_2()
        sleep(speed)
        clear()
        start_frame_3()
        sleep(speed)
        now_minute=now_minute+(3*.25)/60  
# Run the appropriate three frame sequence while the current system time is 
# within the second of the four interval segments.        
    while now_minute<=second_quarter_end_minute:
        clear()
        second_frame_1()
        sleep(speed)
        clear()
        second_frame_2()
        sleep(speed)
        clear()
        second_frame_3()
        sleep(speed)
        now_minute=now_minute+(3*.25)/60 
# Run the appropriate three frame sequence while the current system time is 
# within the second of the four interval segments.           
    while now_minute<=third_quarter_end_minute:
        clear()
        third_frame_1()
        sleep(speed)
        clear()
        third_frame_2()
        sleep(speed)
        clear()
        third_frame_3()
        sleep(speed)
        now_minute=now_minute+(3*.25)/60 
# Run the appropriate three frame sequence while the current system time is 
# within the last of the four interval segments.     
    while now_minute<=third_quarter_end_minute:
        clear()
        fourth_frame_1()
        sleep(speed)
        clear()
        fourth_frame_2()
        sleep(speed)
        clear()
        fourth_frame_3()
        sleep(speed)
        now_minute=now_minute+(3*.25)/60   
# Displays the final frame.
    finished_frame() 
# Tell the user input was invalid.  Only works for invalid integers.
else:
    time_set = input('Invalid entry.  Goodbye.')	


 
    










   