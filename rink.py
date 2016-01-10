from Tkinter import *
import urllib, json

# CONSTANTS
SCALE = 4;
OFFSET = 20;
HEIGHT = 85 * SCALE + OFFSET * 2
WIDTH = 200 * SCALE + OFFSET * 2
WHITE = "#FFFFFF"
RED = "#ED1B25"
BLUE = "#3F47CC"
LIGHT_BLUE = "#9AD9EA"
GRAY = "#CCCCCC"
BLACK = "#000000"

events = []

def create_rink():
    """Creates a blank hockey rink."""

    # RINK
    coords = OFFSET, OFFSET, OFFSET+22*SCALE, OFFSET+22*SCALE
    canvas.create_arc(coords, start=90, extent=90, fill=WHITE, outline="")   
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

    # RINK OUTLINE
    coords = OFFSET, OFFSET, OFFSET+22*SCALE, OFFSET+22*SCALE
    canvas.create_arc(coords, start=90, extent=90, outline=BLACK, style=ARC, width=2)
    coords = OFFSET, HEIGHT-OFFSET-22*SCALE, OFFSET+22*SCALE, HEIGHT-OFFSET
    canvas.create_arc(coords, start=180, extent=90, outline=BLACK, style=ARC, width=2)
    coords = WIDTH-OFFSET-22*SCALE, HEIGHT-OFFSET-22*SCALE, WIDTH-OFFSET, HEIGHT-OFFSET
    canvas.create_arc(coords, start=270, extent=90, outline=BLACK, style=ARC, width=2)
    coords = WIDTH-OFFSET-22*SCALE, OFFSET, WIDTH-OFFSET, OFFSET+22*SCALE
    canvas.create_arc(coords, start=0, extent=90, outline=BLACK, style=ARC, width=2)
    coords = OFFSET+11*SCALE, OFFSET, WIDTH-OFFSET-11*SCALE, OFFSET
    canvas.create_line(coords, fill=BLACK, width=2)
    coords = WIDTH-OFFSET, OFFSET+11*SCALE, WIDTH-OFFSET, HEIGHT-OFFSET-11*SCALE
    canvas.create_line(coords, fill=BLACK, width=2)
    coords = WIDTH-OFFSET-11*SCALE, HEIGHT-OFFSET, OFFSET+11*SCALE, HEIGHT-OFFSET
    canvas.create_line(coords, fill=BLACK, width=2)
    coords = OFFSET, OFFSET+11*SCALE, OFFSET, HEIGHT-OFFSET-11*SCALE
    canvas.create_line(coords, fill=BLACK, width=2)
    

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
    """Returns the PlayByPlay.json fil for the game given by the season and game_id."""
    url = "http://live.nhl.com/GameData/" + str(season) + "/" + str(game_id) + "/PlayByPlay.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def click_event(event):
    """The event handler that sets the description when an event is clicked."""
    desc_tuple = canvas.gettags(event.widget.find_closest(event.x, event.y)[0])
    desc = [x for x in desc_tuple if x != "current"]
    desc = ' '.join(map(str,desc))
    description.set(desc)

def add_event(play, color, label, x, y):
    """Adds a single event to the canvas."""
    coords = WIDTH/2+x*SCALE-6, HEIGHT/2+y*SCALE-6, WIDTH/2+x*SCALE+6, HEIGHT/2+y*SCALE+6
    style = ("Arial", 10, "bold")
    event = canvas.create_oval(coords, outline="black", fill=color, tags=play["desc"])
    events.append(event)
    canvas.tag_bind(event, "<ButtonPress-1>", click_event)
    event = canvas.create_text(WIDTH/2+x*SCALE, HEIGHT/2+y*SCALE, text=label, font=style, tags=play["desc"])
    events.append(event)
    canvas.tag_bind(event, "<ButtonPress-1>", click_event)
    canvas.pack()
    
# Adds play to the shot chart
# Types of plays: Goal, Shot, Hit, Penalty
def add_to_chart(play, options={}):
    """Add's an event to the chart by setting colors and labels then calling add_event."""
    x = play["xcoord"]
    y = play["ycoord"]
    color = LIGHT_BLUE
    label = ""
    if play["type"] == "Shot":
        color = "red"
        label = "S"
    elif play["type"] == "Hit":
        color = "yellow"
        label = "H"
    elif play["type"] == "Goal":
        color = "green"
        label = "G"
    elif play["type"] == "Penalty":
        color = "blue"
        label = "P"
    if options == {}:
        add_event(play, color, label, x, y)
    else:
        adding = True
        for option in options:
            if str(play[option]) != str(options[option]) and options[option] != -1:
                adding = False
                break
        if adding:  
            add_event(play, color, label, x, y)

def clear_events():
    """Clears all events off of the canvas."""
    while len(events) > 0:
        canvas.delete(events.pop())

def determine_periods(obj):
    """Returns the number of periods in the json 'play' array obj"""
    return obj[len(obj)-1]["period"]
    

tk = Tk()
tk.geometry(str(WIDTH)+"x"+str(HEIGHT+150))
tk.resizable(width=FALSE, height=FALSE)
tk.title("NHL Shot Chart")

title_frame = Frame(tk)
title_frame.grid(row=0)
top_frame = Frame(tk)
top_frame.grid(row=1)
bottom_frame = Frame(tk)
bottom_frame.grid(row=3)
description_frame = Frame(tk)
description_frame.grid(row=2)

canvas = Canvas(top_frame, height=HEIGHT, width=WIDTH)
create_rink()

data = get_pbp_json(20152016, 2015020614)
# data = get_pbp_json(20152016, 2015020590)
# data = get_pbp_json(20152016, 2015020613)
plays = data["data"]["game"]["plays"]["play"]
home_team = data["data"]["game"]["hometeamname"]
away_team = data["data"]["game"]["awayteamname"]

for i in range(0, len(plays)):
    add_to_chart(plays[i])

variable = StringVar(bottom_frame)
variable.set("Both") # default value
description = StringVar(bottom_frame)
description.set("None selected")

# Updates the shot chart
def update_chart():
    """Updates the shot chart based off of what team is selected."""
    selected_team = variable.get()
    selected_period = period_variable.get()
    if selected_period == "All":
        selected_period = -1
    elif selected_period == "OT":
        selected_period = 4
    selected_id = -1
    if selected_team == home_team:
        selected_id = data["data"]["game"]["hometeamid"]
    elif selected_team == away_team:
        selected_id = data["data"]["game"]["awayteamid"]
    clear_events()
    for i in range(0, len(plays)):
        add_to_chart(plays[i], {"teamid":selected_id, "period":selected_period})
    
# Title
title_text = away_team + " at " + home_team
title_font = ("TkDefaultFont", 16, "bold")
title = Label(title_frame, text=title_text, font=title_font)
title.grid(row=0)

# Team Select
team_label = Label(bottom_frame, text="Select Team")
team_label.grid(row=0, sticky=E)
team_menu = OptionMenu(bottom_frame, variable, "Both", home_team, away_team)
team_menu.config(width=20)
team_menu.grid(row=0, column=1, columnspan=2, sticky=E+W)

# Period Select
period_label = Label(bottom_frame, text="Select Period")
period_label.grid(row=1, sticky=E)
period_variable = StringVar(bottom_frame)
period_variable.set("All")
periods = determine_periods(plays)
period_menu = OptionMenu(bottom_frame, period_variable, "All", "1", "2", "3")
if periods == 4:
    period_menu = OptionMenu(bottom_frame, period_variable, "All", "1", "2", "3", "OT")
elif periods == 5:
    period_menu = OptionMenu(bottom_frame, period_variable, "All", "1", "2", "3", "OT", "SO")
period_menu.grid(row=1, column = 1, columnspan=2, sticky=E+W)

# Buttons
# - Update
update = Button(bottom_frame, text="Update", command=update_chart)
update.grid(row=3, column=1)

# Description
desc = Label(description_frame, textvariable=description)
desc.grid(row=0, sticky=E+W+N+S)

tk.mainloop()
