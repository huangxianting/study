__author__ = 'sherry'
#coding:utf-8

import datetime

def this_week(fmt = '%Y-%m-%d'):
    now = datetime.datetime.now()
    this_week_start_dt = (now - datetime.timedelta(days = now.weekday())).strftime(fmt)
    this_week_end_dt = (now + datetime.timedelta(days = 6 - now.weekday())).strftime(fmt)
    return [this_week_start_dt, this_week_end_dt]

def last_week(fmt = '%Y-%m-%d'):
    now = datetime.datetime.now()
    last_week_start_dt = (now - datetime.timedelta(days = now.weekday() + 7)).strftime(fmt)
    last_week_end_dt = (now - datetime.timedelta(days = now.weekday() + 1)).strftime(fmt)
    return [last_week_start_dt, last_week_end_dt]

def this_week_kpi(fmt = '%Y-%m-%d'):
    now = datetime.datetime.now()
    start_dt_kpi = (now - datetime.timedelta(days = now.weekday() + 1)).strftime(fmt)
    end_dt_kpi = (now + datetime.timedelta(days = 5 - now.weekday())).strftime(fmt)
    this_week_start_dt_kpi = start_dt_kpi + 'T16:00:00.000Z'
    this_week_end_dt_kpi = end_dt_kpi + 'T16:00:00.000Z'
    return this_week_start_dt_kpi, this_week_end_dt_kpi

def last_week_kpi(fmt = '%Y-%m-%d'):
    now = datetime.datetime.now()
    start_dt_kpi = (now - datetime.timedelta(days = now.weekday() + 8)).strftime(fmt)
    end_dt_kpi =  (now - datetime.timedelta(days = now.weekday() + 2)).strftime(fmt)
    last_week_start_dt_kpi = start_dt_kpi + 'T16:00:00.000Z'
    last_week_end_dt_kpi = end_dt_kpi + 'T16:00:00.000Z'
    return last_week_start_dt_kpi, last_week_end_dt_kpi
