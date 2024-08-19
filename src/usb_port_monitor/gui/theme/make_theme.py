import json
import os
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
    grey = QColor(53, 53, 53)
    white = QColor(255, 255, 255)
    visua_blue = QColor(0, 117, 183)
    black = QColor(0, 0, 0)

    grey = Color(grey).to_json()
    white = Color(white).to_json()
    visua_blue = Color(visua_blue).to_json()
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
        "Highlight": visua_blue,
        "HighlightedText": black,
    }

    with open(r"../assets/theme.json", "w") as f:
        json.dump(theme_dict, f, indent=4)
    
    print("theme.json created")