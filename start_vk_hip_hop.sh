#!/bin/sh

VK_URL=""
VK_KEY=""

while true
do
  ffmpeg -re -f concat -safe 0 -i hip_hop.txt \
	-preset fast \
	-f flv -copyts $VK_URL$VK_KEY
	done