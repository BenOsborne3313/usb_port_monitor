import json
import os
import sys
from PySide6.QtGui import QPalette, QColor 

#simple class for storing rgba values
class Color:
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __init__(self, color):
        self.r = color.red()
        self.g = color.green()
        self.b = color.blue()
        self.a = color.alpha()

    def __str__(self):
        return f"rgba({self.r}, {self.g}, {self.b}, {self.a})"

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b}, {self.a})"

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a

    def to_qcolor(self):
        return QColor(self.r, self.g, self.b, self.a)
    
    #make it json serializable
    def to_json(self):
        return {"r": self.r, "g": self.g, "b": self.b, "a": self.a}
    

#some functions to get the theme as a palette
def load_theme_from_json(path_to_theme):
    with open(path_to_theme, "r") as f:
        theme = json.load(f)

    theme_palette = QPalette()
    for key, value in theme.items():
        color = QColor(value["r"], value["g"], value["b"], value["a"])
        theme_palette.setColor(getattr(QPalette, key), color)
    return theme_palette

#make an empty file in ./assets/ called theme.json
if __name__ == "__main__":
    print("Creating theme.json")
    theme_fields = [
        "Window",
        "WindowText",
        "Base",
        "AlternateBase",
        "ToolTipBase",
        "ToolTipText",
        "Text",
        "Button",
        "ButtonText",
        "BrightText",
        "Link",
        "Highlight",
        "HighlightedText",
    ]

    #now we set our colors
    grey = QColor(16, 16, 16)
    white = QColor(255, 255, 255)
    visua_blue = QColor(0, 117, 183)
    black = QColor(0, 0, 0)
    visua_dark_blue = QColor(0, 80, 125)

    grey = Color(grey).to_json()
    white = Color(white).to_json()
    visua_blue = Color(visua_blue).to_json()
    visua_dark_blue = Color(visua_dark_blue).to_json()
    black = Color(black).to_json()

    theme_dict = {
        "Window": grey,
        "WindowText": visua_blue,
        "Base": grey,
        "AlternateBase": white,
        "ToolTipBase": black,
        "ToolTipText": visua_blue,
        "Text": visua_blue,
        "Button": grey,
        "ButtonText": visua_blue,
        "BrightText": visua_blue,
        "Link": visua_blue,
        "Highlight": visua_dark_blue,
        "HighlightedText": black,
    }
    dir = os.path.abspath(__file__)
    path_to_theme = os.path.join(os.path.dirname(dir), r"../assets/theme.json")
    with open(path_to_theme, "w") as f:
        json.dump(theme_dict, f, indent=4)
    
    print("theme.json created")