#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

from snaut import app_factory

conf = ConfigParser()

conf.read(['config.ini', 'config_local.ini'])

app = app_factory(conf)
