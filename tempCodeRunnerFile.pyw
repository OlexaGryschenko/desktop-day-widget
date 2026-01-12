import tkinter as tk
from time import strftime

# --- CONFIGURATION ---
WIDTH = 100
HEIGHT = 65
BACKGROUND_COLOR = "#400303"  # Dark modern grey
TEXT_COLOR = "#91AAEE"        # White
FONT_STYLE = ("Segoe UI", 14, "bold") # Large, clear font
SMALL_FONT_STYLE = ("Segoe UI", 9) # Smaller font for date and month

def update_day():
    """ Updates the labels with the current day, date, and month. """
    day_string = strftime('%A')
    # %d is day of month, %B is full month name
    date_string = strftime('%d %B') 
    
    day_label.config(text=day_string)
    date_label.config(text=date_string)
    
    root.after(1000, update_day)

def start_move(event):
    """ Record the initial mouse position when clicking. """
    root.x = event.x
    root.y = event.y

def stop_move(event):
    """ Reset on release. """
    root.x = None
    root.y = None

def do_move(event):
    """ Calculate new position as mouse moves. """
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

def close_app(event):
    """ Close the app on right-click. """
    root.destroy()

# --- MAIN WINDOW SETUP ---
root = tk.Tk()
root.title("Day Widget")

# Remove the title bar and borders
root.overrideredirect(True)

# Set size and initial position (Top-Left default)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Center it initially? Or use +50+50 for top left.
# Let's put it slightly offset from the top left corner.
root.geometry(f"{WIDTH}x{HEIGHT}+100+100")
root.configure(bg=BACKGROUND_COLOR)

# --- WIDGETS ---
day_label = tk.Label(
    root, 
    font=FONT_STYLE, 
    bg=BACKGROUND_COLOR, 
    fg=TEXT_COLOR
)
day_label.pack(expand=True, fill='x')

date_label = tk.Label(
    root,
    font=SMALL_FONT_STYLE,
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR
)
date_label.pack(expand=True, fill='x')

# --- BINDINGS (Interactivity) ---
# Right-click to close
root.bind('<Button-3>', close_app) 

# Left-click and drag to move
root.bind('<Button-1>', start_move)
root.bind('<ButtonRelease-1>', stop_move)
root.bind('<B1-Motion>', do_move)

# --- START ---
update_day()
root.mainloop()