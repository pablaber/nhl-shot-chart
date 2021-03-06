from Tkinter import *
from PIL import Image, ImageTk
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
    canvas.create_oval(coords, outline=BLUE, width=2, fill=WHITE)

    # HALF CENTER CIRCLE
    coords = WIDTH/2-10*SCALE, HEIGHT-OFFSET-10*SCALE, WIDTH/2+10*SCALE, HEIGHT-OFFSET+10*SCALE
    canvas.create_arc(coords, outline=RED, width=2, start=0, extent=180)

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
    # - - Ticks
    coords = OFFSET+29.5*SCALE, HEIGHT/2-39*SCALE, OFFSET+29.5*SCALE, HEIGHT/2-5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+32.5*SCALE, HEIGHT/2-39*SCALE, OFFSET+32.5*SCALE, HEIGHT/2-5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - - Circles
    coords = OFFSET+16*SCALE, HEIGHT/2-37*SCALE, OFFSET+46*SCALE, HEIGHT/2-7*SCALE
    canvas.create_oval(coords, outline=RED, width=2, fill=WHITE)
    coords = OFFSET+30*SCALE, HEIGHT/2-23*SCALE, OFFSET+32*SCALE, HEIGHT/2-21*SCALE
    canvas.create_oval(coords, fill=RED, outline="")
    # - - Cross
    coords = OFFSET+25*SCALE, HEIGHT/2-22.8*SCALE, OFFSET+29*SCALE, HEIGHT/2-22.8*SCALE, OFFSET+29*SCALE, HEIGHT/2-25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+25*SCALE, HEIGHT/2-21.2*SCALE, OFFSET+29*SCALE, HEIGHT/2-21.2*SCALE, OFFSET+29*SCALE, HEIGHT/2-18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+37*SCALE, HEIGHT/2-22.8*SCALE, OFFSET+33*SCALE, HEIGHT/2-22.8*SCALE, OFFSET+33*SCALE, HEIGHT/2-25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+37*SCALE, HEIGHT/2-21.2*SCALE, OFFSET+33*SCALE, HEIGHT/2-21.2*SCALE, OFFSET+33*SCALE, HEIGHT/2-18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - Bottom Left
    # - - Ticks
    coords = OFFSET+29.5*SCALE, HEIGHT/2+39*SCALE, OFFSET+29.5*SCALE, HEIGHT/2+5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+32.5*SCALE, HEIGHT/2+39*SCALE, OFFSET+32.5*SCALE, HEIGHT/2+5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - - Circles
    coords = OFFSET+16*SCALE, HEIGHT/2+37*SCALE, OFFSET+46*SCALE, HEIGHT/2+7*SCALE
    canvas.create_oval(coords, outline=RED, width=2, fill=WHITE)
    coords = OFFSET+30*SCALE, HEIGHT/2+23*SCALE, OFFSET+32*SCALE, HEIGHT/2+21*SCALE
    canvas.create_oval(coords, fill=RED, outline="")
    # - - Cross
    coords = OFFSET+25*SCALE, HEIGHT/2+22.8*SCALE, OFFSET+29*SCALE, HEIGHT/2+22.8*SCALE, OFFSET+29*SCALE, HEIGHT/2+25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+25*SCALE, HEIGHT/2+21.2*SCALE, OFFSET+29*SCALE, HEIGHT/2+21.2*SCALE, OFFSET+29*SCALE, HEIGHT/2+18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+37*SCALE, HEIGHT/2+22.8*SCALE, OFFSET+33*SCALE, HEIGHT/2+22.8*SCALE, OFFSET+33*SCALE, HEIGHT/2+25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = OFFSET+37*SCALE, HEIGHT/2+21.2*SCALE, OFFSET+33*SCALE, HEIGHT/2+21.2*SCALE, OFFSET+33*SCALE, HEIGHT/2+18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - Top Right
    # - - Ticks
    coords = WIDTH-(OFFSET+29.5*SCALE), HEIGHT/2-39*SCALE, WIDTH-(OFFSET+29.5*SCALE), HEIGHT/2-5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+32.5*SCALE), HEIGHT/2-39*SCALE, WIDTH-(OFFSET+32.5*SCALE), HEIGHT/2-5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - - Circles
    coords = WIDTH-(OFFSET+16*SCALE), HEIGHT/2-37*SCALE, WIDTH-(OFFSET+46*SCALE), HEIGHT/2-7*SCALE
    canvas.create_oval(coords, outline=RED, width=2, fill=WHITE)
    coords = WIDTH-(OFFSET+30*SCALE), HEIGHT/2-23*SCALE, WIDTH-(OFFSET+32*SCALE), HEIGHT/2-21*SCALE
    canvas.create_oval(coords, fill=RED, outline="")
    # - - Cross
    coords = WIDTH-(OFFSET+25*SCALE), HEIGHT/2-22.8*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2-22.8*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2-25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+25*SCALE), HEIGHT/2-21.2*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2-21.2*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2-18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+37*SCALE), HEIGHT/2-22.8*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2-22.8*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2-25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+37*SCALE), HEIGHT/2-21.2*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2-21.2*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2-18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - Bottom Right
    # - - Ticks
    coords = WIDTH-(OFFSET+29.5*SCALE), HEIGHT/2+39*SCALE, WIDTH-(OFFSET+29.5*SCALE), HEIGHT/2+5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+32.5*SCALE), HEIGHT/2+39*SCALE, WIDTH-(OFFSET+32.5*SCALE), HEIGHT/2+5*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    # - - Circles
    coords = WIDTH-(OFFSET+16*SCALE), HEIGHT/2+37*SCALE, WIDTH-(OFFSET+46*SCALE), HEIGHT/2+7*SCALE
    canvas.create_oval(coords, outline=RED, width=2, fill=WHITE)
    coords = WIDTH-(OFFSET+30*SCALE), HEIGHT/2+23*SCALE, WIDTH-(OFFSET+32*SCALE), HEIGHT/2+21*SCALE
    canvas.create_oval(coords, fill=RED, outline="")
    # - - Cross
    coords = WIDTH-(OFFSET+25*SCALE), HEIGHT/2+22.8*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2+22.8*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2+25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+25*SCALE), HEIGHT/2+21.2*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2+21.2*SCALE, WIDTH-(OFFSET+29*SCALE), HEIGHT/2+18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+37*SCALE), HEIGHT/2+22.8*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2+22.8*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2+25.8*SCALE
    canvas.create_line(coords, fill=RED, width=2)
    coords = WIDTH-(OFFSET+37*SCALE), HEIGHT/2+21.2*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2+21.2*SCALE, WIDTH-(OFFSET+33*SCALE), HEIGHT/2+18.2*SCALE
    canvas.create_line(coords, fill=RED, width=2)

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


    canvas.grid(row=1, columnspan=5)

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
    x = x*-1
    coords = WIDTH/2+x*SCALE-6, HEIGHT/2+y*SCALE-6, WIDTH/2+x*SCALE+6, HEIGHT/2+y*SCALE+6
    style = ("Arial", 10, "bold")
    tag = play["desc"] + ". Period: " + str(play["period"]) + ". Time: " + str(play["time"])
    event = canvas.create_oval(coords, outline="black", fill=color, tags=tag)
    events.append(event)
    canvas.tag_bind(event, "<ButtonPress-1>", click_event)
    event = canvas.create_text(WIDTH/2+x*SCALE, HEIGHT/2+y*SCALE, text=label, font=style, tags=tag)
    events.append(event)
    canvas.tag_bind(event, "<ButtonPress-1>", click_event)
    canvas.grid(row=1, columnspan=5)

def add_to_chart(play, options={}):
    """Add's an event to the chart by setting colors and labels then calling add_event."""
    if str(play["period"]) != "5":
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

def get_games(season, date):
    """ Returns an array of objects representing the games"""
    url = "http://live.nhl.com/GameData/SeasonSchedule-" + season + ".json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    games = []
    for game in data:
        if game["est"][:8] == date:
            games.append(game)
    return games

def get_game_strings(games):
    """Takes what is returned from get_games and produces an array of strings to display"""
    game_strings = []
    for game in games:
        game_string = game["a"] + " at " + game["h"] + " "
        date = game["est"][4:6] + "/" + game["est"][6:8] + "/" + game["est"][:4] + " " + game["est"][9:]
        game_string = game_string + date
        game_strings.append(game_string)
    return game_strings

tk = Tk()
tk.geometry(str(WIDTH+200)+"x"+str(HEIGHT+200))
tk.resizable(width=FALSE, height=FALSE)
tk.title("NHL Shot Chart")

main_frame = Frame(tk)
main_frame.grid()

canvas = Canvas(main_frame, height=HEIGHT, width=WIDTH)
create_rink()

data = get_pbp_json(20152016, 2015020614)
# data = get_pbp_json(20152016, 2015020590)
# data = get_pbp_json(20152016, 2015020613)
plays = data["data"]["game"]["plays"]["play"]
home_team = data["data"]["game"]["hometeamname"]
away_team = data["data"]["game"]["awayteamname"]

# Add all plays to chart on startup
for i in range(0, len(plays)):
    add_to_chart(plays[i])

variable = StringVar(main_frame)
variable.set("Both") # default value
description = StringVar(main_frame)
description.set("Click an event to see information.")

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
title_font = ("TkDefaultFont", 24, "bold")
title = Label(main_frame, text=title_text, font=title_font)
title.grid(row=0, column=1, columnspan=3, sticky=E+W)
awayteam_filename = "logos/gif_40/" + str(data["data"]["game"]["awayteamid"]) + ".gif"
hometeam_filename = "logos/gif_40/" + str(data["data"]["game"]["hometeamid"]) + ".gif"
awayteam_logo = PhotoImage(file=awayteam_filename)
awayteam_label = Label(main_frame, image=awayteam_logo)
awayteam_label.photo = awayteam_logo
awayteam_label.grid(row=0, column=0, sticky="E")
hometeam_logo = PhotoImage(file=hometeam_filename)
hometeam_label = Label(main_frame, image=hometeam_logo)
hometeam_label.photo = hometeam_logo
hometeam_label.grid(row=0, column=4, sticky="W")


# Team Select
team_label = Label(main_frame, text="Select Team")
team_label.grid(row=3, column=1, sticky=E)
team_menu = OptionMenu(main_frame, variable, "Both", home_team, away_team)
team_menu.config(width=20)
team_menu.grid(row=3, column=2, columnspan=2, sticky=W, ipadx=10)

# Period Select
period_label = Label(main_frame, text="Select Period")
period_label.grid(row=4, column=1, sticky=E)
period_variable = StringVar(main_frame)
period_variable.set("All")
periods = determine_periods(plays)
period_menu = OptionMenu(main_frame, period_variable, "All", "1", "2", "3")
if periods == 4 or periods == 5:
    period_menu = OptionMenu(main_frame, period_variable, "All", "1", "2", "3", "OT")
period_menu.grid(row=4, column = 2, columnspan=2, sticky=W, ipadx=68)

# Buttons
# - Update
update = Button(main_frame, text="Update", command=update_chart)
update.grid(row=5, column=2, sticky=W, padx=40)

# Description
desc = Label(main_frame, textvariable=description)
desc.grid(row=2, columnspan=5, sticky=E+W+N+S)

# Game Info
# game_select_label = Label(side_frame, text="Game Select")
# game_select_label.pack(fill=X)


tk.mainloop()
