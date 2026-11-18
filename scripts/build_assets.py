#!/usr/bin/env python3
"""Compose the studio profile SVGs from existing DreamX artwork."""
from pathlib import Path
import base64
import html
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
LETTERS = json.loads((OUT / "brand/lettering.json").read_text())
SYMBOL = base64.b64encode((OUT / "brand/symbol.png").read_bytes()).decode()
FONT = "Inter, 'Segoe UI', Arial, sans-serif"
PALETTES = {
    "light": {"bg": "#f7f9fc", "ink": "#192536", "muted": "#5d6c80", "border": "#dce3ed", "line": "#bac9dd", "fill": "#e9f0fa", "accent": "#426cba"},
    "dark": {"bg": "#101722", "ink": "#edf2f8", "muted": "#9cacbf", "border": "#293548", "line": "#3e5472", "fill": "#172638", "accent": "#83adf0"},
}

def text(value, x, y, size, color, spacing=0, weight=500):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{html.escape(value)}</text>'

def wordmark(x, y, scale, ink):
    paths = "".join(f'<path transform="translate({letter["x"]} 0)" d="{letter["path"]}"/>' for letter in LETTERS["letters"])
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{ink}" stroke-width="{LETTERS["stroke_width"]}" stroke-linecap="round" stroke-linejoin="round">{paths}</g>'

def hero(theme):
    p = PALETTES[theme]
    width, height = 1000, 320
    elements = [f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="18" fill="{p["bg"]}" stroke="{p["border"]}"/>']
    elements += [f'<image x="28" y="43" width="235" height="235" href="data:image/png;base64,{SYMBOL}"/>',
                 wordmark(265, 85, 4.15, p["ink"]), text("STUDIO", 274, 249, 34, p["muted"], 10)]
    elements.append(f'''<g transform="translate(800 84) scale(.77)" stroke-linejoin="round">
  <path d="M0 52 86 3 172 52 86 101Z" fill="{p["fill"]}" stroke="{p["line"]}" stroke-width="1.5"/>
  <path d="M0 52V139L86 188 172 139V52M86 101V188M0 96 86 145 172 96" fill="none" stroke="{p["line"]}" stroke-width="1.5"/>
  <path d="M86 3V57L0 106M86 57 172 106" fill="none" stroke="{p["line"]}" stroke-width="1" stroke-dasharray="3 5"/>
  <path d="M86 101 172 52V139" fill="none" stroke="{p["accent"]}" stroke-width="2.5"/>
  <circle cx="86" cy="101" r="4" fill="{p["accent"]}"/>
  <circle cx="172" cy="139" r="3" fill="{p["accent"]}"/>
</g>''')
    content = chr(10).join(elements)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">DreamX Studio</title>
<desc id="desc">Games, tools and agent systems. A development studio in Vietnam.</desc>
{content}
</svg>
'''

for theme in PALETTES:
    (OUT / ("studio-" + theme + ".svg")).write_text(hero(theme))

icons = {
    "game": '<path d="m32 10 20 11v23L32 56 12 44V21Z"/><path d="m12 21 20 12 20-12M32 33v23M22 16l20 12"/><circle cx="12" cy="44" r="3"/><circle cx="52" cy="21" r="3"/>',
    "mop": '<path d="M32 17v11M32 28 15 42M32 28l17 14"/><rect x="24" y="5" width="16" height="13" rx="4"/><rect x="6" y="42" width="18" height="16" rx="4"/><rect x="40" y="42" width="18" height="16" rx="4"/><circle cx="32" cy="29" r="3"/>',
    "relay": '<rect x="12" y="12" width="40" height="40" rx="9"/><path d="m32 21 11 11-11 11-11-11Z"/><circle cx="32" cy="32" r="2"/>',
}
for name, geometry in icons.items():
    (OUT / (name + ".svg")).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64"><g fill="none" stroke="#7298d8" stroke-width="2.3" stroke-linejoin="round" stroke-linecap="round">{geometry}</g></svg>' + chr(10))
print("Built two theme banners and three project-category illustrations.")
