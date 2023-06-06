#!/bin/sh

VK_URL=""
VK_KEY=""

while true
do
  ffmpeg -re -f concat -safe 0 -i input.txt \
	-preset fast \
	-f flv -copyts $VK_URL$VK_KEY
	done