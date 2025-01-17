import sys
import json
from Constants import *
import draw_functions as drawfunc
import colors

def generate_schedules(file):
    with open(file, 'r', encoding='utf-8') as jsonfile:
        event = json.load(jsonfile)

        color_ids = []
        for day in event['event']['days']:
            for stream in day['streams']:
                for block in stream['blocks']:
                    color = block['color']
                    if type(color) == int:
                        color_ids.append(color)
                    


            color_ids = (list(set(color_ids)))
            color_palette = colors.gen_color_palette(event["event"]["color_palette"], len(color_ids))
            c_map = {}
            for c in color_ids:
                c_map[c] = color_palette[len(c_map)]

        for day in event['event']['days']:
            drawfunc.draw_day(event['event']['name'], day, event['event']['time zone'], event['event']['zone_text'], event['event']['time format'], event['event']['zones'], c_map)
        
        drawfunc.draw_tournament_box(event)


generate_schedules(sys.argv[1])
   

