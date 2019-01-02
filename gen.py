#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
import time

DAY = 24 * 60 * 60 # in seconds

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

def gen() -> 'void':
    floder_name = gen_floder_name()
    if path.exists(floder_name):
        return
    path.makedirs(floder_name)
    file_name = path.join(floder_name, "summary")
    # with open(file_name, "w") as fp:
    print(file_name)

if __name__ == '__main__':
    gen()
