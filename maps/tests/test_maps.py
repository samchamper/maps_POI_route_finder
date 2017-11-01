"""
Nose tests for acp_times.py

Test five routes with strange edge case controle points against values from:
https://rusa.org/octime_acp.html
"""

import arrow
import nose
import logging

from acp_times import *

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def start_finish(controle, total, start):
    return (open_time(controle, total, start), close_time(controle, total, start))

def test_200():
    start = arrow.get("2018-01-01 00:00", 'YYYY-MM-DD HH:mm')
    assert start_finish(0, 200, start) == ("2018-01-01T00:00:00+00:00" , "2018-01-01T01:00:00+00:00")
    assert start_finish(1, 200, start) == ("2018-01-01T00:02:00+00:00" , "2018-01-01T00:04:00+00:00")
    assert start_finish(199, 200, start) == ("2018-01-01T05:51:00+00:00" , "2018-01-01T13:16:00+00:00")
    assert start_finish(200, 200, start) == ("2018-01-01T05:53:00+00:00" , "2018-01-01T13:30:00+00:00")
    assert start_finish(220, 200, start) == ("2018-01-01T05:53:00+00:00" , "2018-01-01T13:30:00+00:00")

def test_300():
    start = arrow.get("2018-01-01 00:00", 'YYYY-MM-DD HH:mm')
    assert start_finish(0, 300, start) == ("2018-01-01T00:00:00+00:00" , "2018-01-01T01:00:00+00:00")
    assert start_finish(299, 300, start) == ("2018-01-01T08:59:00+00:00" , "2018-01-01T19:56:00+00:00")
    assert start_finish(300, 300, start) == ("2018-01-01T09:00:00+00:00" , "2018-01-01T20:00:00+00:00")
    assert start_finish(350, 300, start) == ("2018-01-01T09:00:00+00:00" , "2018-01-01T20:00:00+00:00")
    assert start_finish(9500, 300, start) == ("2018-01-01T09:00:00+00:00" , "2018-01-01T20:00:00+00:00")

def test_400():
    start = arrow.get("2018-01-01 00:00", 'YYYY-MM-DD HH:mm')
    assert start_finish(0, 400, start) == ("2018-01-01T00:00:00+00:00" , "2018-01-01T01:00:00+00:00")
    assert start_finish(400, 400, start) == ("2018-01-01T12:08:00+00:00" , "2018-01-02T03:00:00+00:00")

def test_600():
    start = arrow.get("2018-01-01 00:00", 'YYYY-MM-DD HH:mm')
    assert start_finish(0, 600, start) == ("2018-01-01T00:00:00+00:00" , "2018-01-01T01:00:00+00:00")
    assert start_finish(1, 600, start) == ("2018-01-01T00:02:00+00:00" , "2018-01-01T00:04:00+00:00")
    assert start_finish(599, 600, start) == ("2018-01-01T18:46:00+00:00" , "2018-01-02T15:56:00+00:00")
    assert start_finish(700, 600, start) == ("2018-01-01T18:48:00+00:00" , "2018-01-02T16:00:00+00:00")


def test_1000():
    start = arrow.get("2017-10-20 13:20", 'YYYY-MM-DD HH:mm')
    assert start_finish(0, 1000, start) == ("2017-10-20T13:20:00+00:00" , "2017-10-20T14:20:00+00:00")
    assert start_finish(1, 1000, start) == ("2017-10-20T13:22:00+00:00" , "2017-10-20T13:24:00+00:00")
    assert start_finish(700, 1000, start) == ("2017-10-21T11:42:00+00:00" , "2017-10-22T14:05:00+00:00")
    assert start_finish(999, 1000, start) == ("2017-10-21T22:23:00+00:00" , "2017-10-23T16:15:00+00:00")
    assert start_finish(1010, 1000, start) == ("2017-10-21T22:25:00+00:00" , "2017-10-23T16:20:00+00:00")
