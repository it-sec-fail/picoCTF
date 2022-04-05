#!/usr/bin/env python

charset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pre_numbers = ["16","9","3","15","3","20","6"]
suf_numbers = ["20","8","5","14","21","13","2","5","18","19","13","1","19","15","14"]

pre=""
suf=""

for number in pre_numbers:
    pre = pre + charset[int(number)-1]

if pre == "picoctf":
    pre = "picoCTF"

for number in suf_numbers:
    suf = suf + charset[int(number)-1]

print(pre+"{"+suf+"}")
