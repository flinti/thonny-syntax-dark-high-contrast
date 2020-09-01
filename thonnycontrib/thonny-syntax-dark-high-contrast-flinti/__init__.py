'''Thonny dark syntax plugin for better contrast than default'''

from thonny import get_workbench
from thonny.workbench import SyntaxThemeSettings




def dark_high_contrast() -> SyntaxThemeSettings:
    default_fg = "#FFFFFF"
    default_bg = "#101010"
    string_fg = "#ADE06F"
    open_string_bg = "#224533"
    gutter_foreground = "#A0A0A0"
    gutter_background = "#222222"

    return {
        "TEXT": {
            "foreground": default_fg,
            "insertbackground": default_fg,
            "background": default_bg,
        },
        "GUTTER": {"foreground": gutter_foreground, "background": gutter_background},
        "breakpoint": {"foreground": "pink"},
        "current_line": {"background": "#363636"},
        "sel": {"background": "#6E6E6E"},#{"foreground": "#eeeeee", "background": "#6E6E6E"},
        "definition": {"foreground": default_fg},
        "string": {"foreground": string_fg},
        "string3": {"foreground": string_fg, "background": None, "font": "EditorFont"},
        "open_string": {"foreground": string_fg, "background": open_string_bg},
        "open_string3": {
            "foreground": string_fg,
            "background": open_string_bg,
            "font": "EditorFont",
        },
        "builtin": {"foreground": "#B9C1FF"},
        "keyword": {"foreground": "#B9C1FF", "font": "BoldEditorFont"},
        "number": {"foreground": "#FFAA1F"},
        "comment": {"foreground": "#BBBB4E", "font": "BoldEditorFont"},
        "welcome": {"foreground": "pink"},
        "magic": {"foreground": "pink"},
        # paren matcher
        "surrounding_parens": {"foreground": "#FF0000", "background": "#000000", "font": "BoldEditorFont", "underline": True},
        "unclosed_expression": {"background": "#250000"},
        # find/replace
        "found": {"underline": True},
        "current_found": {"foreground": "white", "background": "C00000"},
        "matched_name": {"background": "#272727"},
        "local_name": {"font": "ItalicEditorFont"},
    }



def load_plugin() -> None:
    get_workbench().add_syntax_theme("Dark High Contrast", "Default Dark", dark_high_contrast)


