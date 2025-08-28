DEBUG = False
THEME = "light"

def toggle_debug():
    globals()["DEBUG"] = not globals()["DEBUG"]

def set_theme(t):
    globals()["THEME"] = t

print("Before:", DEBUG, THEME)
toggle_debug(); set_theme("dark")
print("After:", DEBUG, THEME)
