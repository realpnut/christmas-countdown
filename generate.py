
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

TARGET = datetime(
    2026, 12, 24, 0, 0, 0,
    tzinfo=ZoneInfo("Europe/Warsaw")
)

now = datetime.now(ZoneInfo("Europe/Warsaw"))
remaining = max(0, int((TARGET - now).total_seconds()))

days, remaining = divmod(remaining, 86400)
hours, remaining = divmod(remaining, 3600)
minutes, seconds = divmod(remaining, 60)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="700" height="190" viewBox="0 0 700 190">

<rect width="700" height="190" rx="18" fill="#0D1117"/>

<text x="350" y="42" text-anchor="middle"
font-family="monospace" font-size="23"
font-weight="bold" fill="#58A6FF">
CHRISTMAS COUNTDOWN
</text>

<g font-family="monospace" text-anchor="middle">
'''

values = [
    (days, "DAYS", 100),
    (hours, "HOURS", 270),
    (minutes, "MINUTES", 440),
    (seconds, "SECONDS", 610)
]

for value, label, x in values:
    svg += f'''
    <text x="{x}" y="112" font-size="39"
    font-weight="bold" fill="#FFFFFF">{value:02d}</text>

    <text x="{x}" y="145" font-size="13"
    fill="#58A6FF">{label}</text>
    '''

svg += '''
</g>

<text x="350" y="177" text-anchor="middle"
font-family="monospace" font-size="10"
fill="#79C0FF">UNTIL CHRISTMAS · 24.12.2026</text>

</svg>
'''

Path("countdown.svg").write_text(svg, encoding="utf-8")
