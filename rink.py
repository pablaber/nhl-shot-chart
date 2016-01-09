from Tkinter import *
import urllib, json

tk = Tk()
tk.title("NHL Shot Chart")

SCALE = 4;
OFFSET = 20;
HEIGHT = 85 * SCALE + OFFSET * 2
WIDTH = 200 * SCALE + OFFSET * 2

# COLORS
WHITE = "#FFFFFF"
RED = "#ED1B25"
BLUE = "#3F47CC"
LIGHT_BLUE = "#9AD9EA"
GRAY = "#CCCCCC"

def create_rink(canvas):

    # RINK
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

    # GOAL AREA
    # - Left
    # - - Crease
    coords = OFFSET+5*SCALE, HEIGHT/2-6*SCALE, OFFSET+17*SCALE, HEIGHT/2+6*SCALE
    canvas.create_arc(coords, fill=LIGHT_BLUE, start=318, extent=84, outline="")
    canvas.create_arc(coords, outline=RED, start=318, extent=84, style=ARC)
    coords = OFFSET+11*SCALE, HEIGHT/2-4*SCALE, OFFSET+15.5*SCALE, HEIGHT/2-4*SCALE, OFFSET+15.5*SCALE, HEIGHT/2+4*SCALE, OFFSET+11*SCALE, HEIGHT/2+4*SCALE
    canvas.create_polygon(coords, fill=LIGHT_BLUE, outline="")
    coords = OFFSET+11*SCALE, HEIGHT/2-4*SCALE, OFFSET+15.2*SCALE+1, HEIGHT/2-4*SCALE
    canvas.create_line(coords, fill=RED)
    coords = OFFSET+15.2*SCALE+1, HEIGHT/2+4*SCALE, OFFSET+11*SCALE, HEIGHT/2+4*SCALE
    canvas.create_line(coords, fill=RED)
    # - - Restricted Area
    coords = OFFSET, HEIGHT/2-14*SCALE, OFFSET+11*SCALE, HEIGHT/2-9*SCALE
    canvas.create_line(coords, fill=RED)
    coords = OFFSET, HEIGHT/2+14*SCALE, OFFSET+11*SCALE, HEIGHT/2+9*SCALE
    canvas.create_line(coords, fill=RED)
    # - - Goal
    coords = OFFSET+8*SCALE, HEIGHT/2-3*SCALE, OFFSET+11*SCALE, HEIGHT/2-3*SCALE, OFFSET+11*SCALE, HEIGHT/2+3*SCALE, OFFSET+8*SCALE, HEIGHT/2+3*SCALE
    canvas.create_polygon(coords, fill=GRAY, outline=RED)
    # - Right
    # - - Crease
    coords = WIDTH-(OFFSET+5*SCALE), HEIGHT/2-6*SCALE, WIDTH-(OFFSET+17*SCALE), HEIGHT/2+6*SCALE
    canvas.create_arc(coords, fill=LIGHT_BLUE, start=138, extent=84, outline="")
    canvas.create_arc(coords, outline=RED, start=138, extent=84, style=ARC)
    coords = WIDTH-(OFFSET+11*SCALE), HEIGHT/2-4*SCALE, WIDTH-(OFFSET+15.5*SCALE), HEIGHT/2-4*SCALE, WIDTH-(OFFSET+15.5*SCALE), HEIGHT/2+4*SCALE, WIDTH-(OFFSET+11*SCALE), HEIGHT/2+4*SCALE
    canvas.create_polygon(coords, fill=LIGHT_BLUE, outline="")
    coords = WIDTH-(OFFSET+11*SCALE), HEIGHT/2-4*SCALE, WIDTH-(OFFSET+15.2*SCALE+1), HEIGHT/2-4*SCALE
    canvas.create_line(coords, fill=RED)
    coords = WIDTH-(OFFSET+15.2*SCALE+1), HEIGHT/2+4*SCALE, WIDTH-(OFFSET+11*SCALE), HEIGHT/2+4*SCALE
    canvas.create_line(coords, fill=RED)
    # - - Restricted Area
    coords = WIDTH-OFFSET, HEIGHT/2-14*SCALE, WIDTH-OFFSET-11*SCALE, HEIGHT/2-9*SCALE
    canvas.create_line(coords, fill=RED)
    coords = WIDTH-OFFSET, HEIGHT/2+14*SCALE, WIDTH-OFFSET-11*SCALE, HEIGHT/2+9*SCALE
    canvas.create_line(coords, fill=RED)
    # - - Goal
    coords = WIDTH-(OFFSET+8*SCALE), HEIGHT/2-3*SCALE, WIDTH-(OFFSET+11*SCALE), HEIGHT/2-3*SCALE, WIDTH-(OFFSET+11*SCALE), HEIGHT/2+3*SCALE, WIDTH-(OFFSET+8*SCALE), HEIGHT/2+3*SCALE
    canvas.create_polygon(coords, fill=GRAY, outline=RED)

    # LINES
    # - Left Baseline
    coords = OFFSET+11*SCALE, OFFSET, OFFSET+11*SCALE, HEIGHT-OFFSET
    canvas.create_line(coords, fill=RED, width=1.5)
    # - Right Baseline
    coords = WIDTH-OFFSET-11*SCALE, OFFSET, WIDTH-OFFSET-11*SCALE, HEIGHT-OFFSET
    canvas.create_line(coords, fill=RED, width=1.5)
    # - Left Blueline
    coords = OFFSET+70*SCALE, OFFSET, OFFSET+70*SCALE, HEIGHT-OFFSET
    canvas.create_line(coords, fill=BLUE, width=7)
    # - Right Blueline
    coords = WIDTH-(OFFSET+70*SCALE), OFFSET, WIDTH-(OFFSET+70*SCALE), HEIGHT-OFFSET
    canvas.create_line(coords, fill=BLUE, width=7)
    # - Redline
    coords = WIDTH/2, OFFSET, WIDTH/2, HEIGHT-OFFSET
    canvas.create_line(coords, fill=RED, width=7)
    coords = WIDTH/2, OFFSET, WIDTH/2, HEIGHT-OFFSET
    canvas.create_line(coords, fill=WHITE, width=5, dash=(9,9))

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

    # NEUTRAL ZONE FACEOFF
    # - Top Left
    coords = WIDTH/2-21*SCALE, HEIGHT/2-23*SCALE, WIDTH/2-19*SCALE, HEIGHT/2-21*SCALE
    canvas.create_oval(coords, outline="", fill=RED)
    # - Bottom Left
    coords = WIDTH/2-21*SCALE, HEIGHT/2+23*SCALE, WIDTH/2-19*SCALE, HEIGHT/2+21*SCALE
    canvas.create_oval(coords, outline="", fill=RED)
    # - Top Right
    coords = WIDTH/2+21*SCALE, HEIGHT/2-23*SCALE, WIDTH/2+19*SCALE, HEIGHT/2-21*SCALE
    canvas.create_oval(coords, outline="", fill=RED)
    # - Bottom Right
    coords = WIDTH/2+21*SCALE, HEIGHT/2+23*SCALE, WIDTH/2+19*SCALE, HEIGHT/2+21*SCALE
    canvas.create_oval(coords, outline="", fill=RED)


    canvas.pack()

# Returns the PlayByPlay.json file for the game given by the season and game_id
def get_pbp_json(season, game_id):
    url = "http://live.nhl.com/GameData/" + str(season) + "/" + str(game_id) + "/PlayByPlay.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

# Adds play to the shot chart
# Types of plays: Goal, Shot, Hit, Penalty
def add_to_chart(play, canvas):
    x = play["xcoord"]
    y = play["ycoord"]
    coords = WIDTH/2+x*SCALE-4, HEIGHT/2+y*SCALE-4, WIDTH/2+x*SCALE+4, HEIGHT/2+y*SCALE+4
    color = LIGHT_BLUE
    if play["type"] == "Shot":
        color = "red"
    elif play["type"] == "Hit":
        color = "yellow"
    elif play["type"] == "Goal":
        color = "green"
    elif play["type"] == "Penalty":
        color = "blue"
    canvas.create_oval(coords, outline="", fill=color)
    canvas.pack()

canvas = Canvas(tk, height=HEIGHT, width=WIDTH, bg="#AAAAAA")
create_rink(canvas)

data = get_pbp_json(20152016, 2015020590)
plays = data["data"]["game"]["plays"]["play"]

for i in range(0, len(plays)):
    add_to_chart(plays[i], canvas)

tk.mainloop()
