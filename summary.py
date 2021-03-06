#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

DAY = 24 * 60 * 60 # in seconds
SUMMARY = "summary"
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
margin_top = "------------------------------------------------------------\n"
no_write = "  这一天没有写总结\n"

def gen_monday_ts() -> 'int':
    now_time_second = int(time.time())
    while True:
        if time.localtime(now_time_second).tm_wday == 0:
            break
        now_time_second -= DAY
    return now_time_second

def gen_floder_name() -> 'string':
    monday = time.strftime("%Y%m%d", time.localtime(gen_monday_ts()))
    firday = time.strftime("%Y%m%d", time.localtime(gen_monday_ts() + 4 * DAY))
    return "{}--{}".format(monday, firday)

def summary():
    floder_name = gen_floder_name()
    line = os.popen('ls {}'.format(floder_name)).readlines()
    with open(SUMMARY, "w") as fpw:
        fpw.write("         Weiming Liu weekly summary\n")
        idx = -1
        for file_name in line:
            idx += 1
            with open(os.path.join(floder_name, file_name[:-1]), "r") as fp:
                fpw.write(margin_top + "\n")
                fpw.write(week[idx] + ":\n")
                text = fp.read()
                if len(text) == 0:
                    text = no_write
                fpw.write(text + "\n")

if __name__ == '__main__':
    summary()
