
import re

with open("SquidGame.srt", "r") as file:
    content = file.read()
    content = re.sub("\[.*?\]","", content)     # regex for replacing everything inside of [] with nothing("")
with open("SquidGame_clean.srt", "w") as file:
    file.write(content)