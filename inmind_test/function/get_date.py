__author__ = 'sherry'
#coding:utf-8

import datetime


def this_week(fmt='%Y-%m-%d'):
    now = datetime.datetime.now()
    this_week_start_dt = (now - datetime.timedelta(days = now.weekday())).strftime(fmt)
    this_week_end_dt = (now + datetime.timedelta(days = 6 - now.weekday())).strftime(fmt)
    return this_week_start_dt,this_week_end_dt
