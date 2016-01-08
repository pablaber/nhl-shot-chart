from Tkinter import *

gui = Tk()

gui.title("test")

SCALE = 4;
OFFSET = 20;
HEIGHT = 85 * SCALE + OFFSET * 2
WIDTH = 200 * SCALE + OFFSET * 2

# COLORS
WHITE = "#FFFFFF"
RED = "#ED1B25"
BLUE = "#3F47CC"
LIGHT_BLUE = "#9AD9EA"

canvas = Canvas(gui, height=HEIGHT, width=WIDTH, bg="#AAAAAA")

# OUTLINE
coords = OFFSET, OFFSET, OFFSET+22*SCALE, OFFSET+22*SCALE
canvas.create_arc(coords, start=90, extent=90, fill=WHITE, outline=WHITE)
coords = OFFSET, HEIGHT-OFFSET-22*SCALE, OFFSET+22*SCALE, HEIGHT-OFFSET
canvas.create_arc(coords, start=180, extent=90, fill=WHITE, outline=WHITE)
coords = WIDTH-OFFSET-22*SCALE, HEIGHT-OFFSET-22*SCALE, WIDTH-OFFSET, HEIGHT-OFFSET
canvas.create_arc(coords, start=270, extent=90, fill=WHITE, outline=WHITE)
coords = WIDTH-OFFSET-22*SCALE, OFFSET, WIDTH-OFFSET, OFFSET+22*SCALE
canvas.create_arc(coords, start=0, extent=90, fill=WHITE, outline=WHITE)
coords = OFFSET+11*SCALE, OFFSET, WIDTH-OFFSET-11*SCALE, OFFSET, WIDTH-OFFSET-11*SCALE, HEIGHT-OFFSET, OFFSET+11*SCALE, HEIGHT-OFFSET
canvas.create_polygon(coords, fill=WHITE, outline=WHITE)
coords = OFFSET, OFFSET+11*SCALE, WIDTH-OFFSET, OFFSET+11*SCALE, WIDTH-OFFSET, HEIGHT-OFFSET-11*SCALE, OFFSET, HEIGHT-OFFSET-11*SCALE
canvas.create_polygon(coords, fill=WHITE, outline=WHITE)

# CENTER CIRCLE
coords = WIDTH/2-15*SCALE, HEIGHT/2-15*SCALE, WIDTH/2+15*SCALE, HEIGHT/2+15*SCALE
canvas.create_oval(coords, outline=BLUE, width=1.5, fill=WHITE)

# LINES
# - Left Baseline
coords = OFFSET+11*SCALE, OFFSET, OFFSET+11*SCALE, HEIGHT-OFFSET
canvas.create_line(coords, fill=RED, width=1.5)
# - Right Baseline
coords = WIDTH-OFFSET-11*SCALE, OFFSET, WIDTH-OFFSET-11*SCALE, HEIGHT-OFFSET
canvas.create_line(coords, fill=RED, width=1.5)
# - Left Blueline
coords = OFFSET+70*SCALE, OFFSET, OFFSET+70*SCALE, HEIGHT-OFFSET
canvas.create_line(coords, fill=BLUE, width=5)
# - Right Blueline
coords = WIDTH-(OFFSET+70*SCALE), OFFSET, WIDTH-(OFFSET+70*SCALE), HEIGHT-OFFSET
canvas.create_line(coords, fill=BLUE, width=5)
# - Redline
coords = WIDTH/2, OFFSET, WIDTH/2, HEIGHT-OFFSET
canvas.create_line(coords, fill=RED, width=5)
coords = WIDTH/2, OFFSET, WIDTH/2, HEIGHT-OFFSET
canvas.create_line(coords, fill=WHITE, width=3, dash=(9,9))

# CENTER DOT
coords = WIDTH/2-1*SCALE-1, HEIGHT/2-1*SCALE-1, WIDTH/2+1*SCALE+1, HEIGHT/2+1*SCALE+1
canvas.create_oval(coords, outline=WHITE, fill=BLUE)

# FACEOFF
# - Top Left
coords = OFFSET+16*SCALE, HEIGHT/2-37*SCALE, OFFSET+46*SCALE, HEIGHT/2-7*SCALE
canvas.create_oval(coords, outline=RED, width=1.5)
coords = OFFSET+30*SCALE, HEIGHT/2-23*SCALE, OFFSET+32*SCALE, HEIGHT/2-21*SCALE
canvas.create_oval(coords, fill=RED, outline="")
# - Bottom Left
coords = OFFSET+16*SCALE, HEIGHT/2+37*SCALE, OFFSET+46*SCALE, HEIGHT/2+7*SCALE
canvas.create_oval(coords, outline=RED, width=1.5)
coords = OFFSET+30*SCALE, HEIGHT/2+23*SCALE, OFFSET+32*SCALE, HEIGHT/2+21*SCALE
canvas.create_oval(coords, fill=RED, outline="")
# - Top Right
coords = WIDTH-(OFFSET+16*SCALE), HEIGHT/2-37*SCALE, WIDTH-(OFFSET+46*SCALE), HEIGHT/2-7*SCALE
canvas.create_oval(coords, outline=RED, width=1.5)
coords = WIDTH-(OFFSET+30*SCALE), HEIGHT/2-23*SCALE, WIDTH-(OFFSET+32*SCALE), HEIGHT/2-21*SCALE
canvas.create_oval(coords, fill=RED, outline="")
# - Bottom Right
coords = WIDTH-(OFFSET+16*SCALE), HEIGHT/2+37*SCALE, WIDTH-(OFFSET+46*SCALE), HEIGHT/2+7*SCALE
canvas.create_oval(coords, outline=RED, width=1.5)
coords = WIDTH-(OFFSET+30*SCALE), HEIGHT/2+23*SCALE, WIDTH-(OFFSET+32*SCALE), HEIGHT/2+21*SCALE
canvas.create_oval(coords, fill=RED, outline="")

# GOALIE CREASE
# - Left
coords = OFFSET+5*SCALE, HEIGHT/2-6*SCALE, OFFSET+17*SCALE, HEIGHT/2+6*SCALE
canvas.create_arc(coords, fill=BLUE, start=315, extent=90, outline="")
coords = OFFSET+11*SCALE, HEIGHT/2-4*SCALE, OFFSET+15*SCALE, HEIGHT/2-4*SCALE, OFFSET+15*SCALE, HEIGHT/2+4*SCALE, OFFSET+11*SCALE, HEIGHT/2+4*SCALE
canvas.create_polygon(coords, fill=BLUE, outline="")
# - Right

canvas.pack()

gui.mainloop()
