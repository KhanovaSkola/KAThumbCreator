#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from PIL import Image
from transforms import RGBTransform
import urllib, cStringIO
from PIL import ImageFont
from PIL import ImageDraw
import json
import textwrap
import argparse

#######################
# get YT id from command line argument
#######################

parser = argparse.ArgumentParser(description='Get YouTube id.')
parser.add_argument('YTid', type=str)

args = parser.parse_args()
YTid = args.YTid

print('YouTube id: {}'.format(YTid))
print

#######################
# get title and wrap it
#######################

video_detail = json.loads(urllib.urlopen("https://noembed.com/embed?url=https://www.youtube.com/watch?v={}".format(YTid)).read())
full_title = video_detail["title"].split(' | ')

title = full_title[0].upper()
subject = full_title[-2]

# unbreakable space did not work, so there is this mess
unbreakable_title = ''
for word in title.split(' '):
    unbreakable_title += word
    if len(word) <= 2:
        unbreakable_title += '{}'
    else:
        unbreakable_title += ' '

line_length = min(len(title)/2 + 2, 25)

wrapped_title = textwrap.wrap(unbreakable_title, line_length, break_long_words=False)
wrapped_title = [line.format(*(' '*100)) for line in wrapped_title]

print(title)
print(subject)
print
for line in wrapped_title:
    print(line)

#######################
# get thumbnail
#######################

file = cStringIO.StringIO(urllib.urlopen("http://img.youtube.com/vi/{}/maxresdefault.jpg".format(YTid)).read())

#######################
# color thumbnail
#######################

ver1 = RGBTransform().desaturate(factor=0.5).applied_to(Image.open(file))
ver2 = RGBTransform().multiply_with((90, 201, 235)).applied_to(ver1)
ver3 = RGBTransform().mix_with((90, 201, 235),factor=0.5).applied_to(ver2) 

ver3.paste(Image.open("Khan_Academy_Logo.png"), (42,622), Image.open("Khan_Academy_Logo.png"))

draw = ImageDraw.Draw(ver3)

#######################
# write title
#######################

font = ImageFont.truetype("LiberationSansNarrow-Bold.ttf", 112)

y = 103
for line in wrapped_title:
    x = (1280 - font.getsize(line)[0])/2
    draw.text((x, y),line,(255,255,255),font=font)
    y += 155


ver3.save(YTid + ".png")
