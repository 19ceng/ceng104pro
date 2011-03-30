from gasp import *

def bug(kx, ky):
	Circle((kx, ky),      50, filled=True, color=(255,0,0))
	Circle((kx, ky-150), 100, filled=True, color=(255,255,0))

# main
begin_graphics()

bug(250, 250)
bug(450, 350)

#end_graphics()
