#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-25 17:13:48
# Project: qunaer

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://travel.qunar.com/travelbook/list.htm?order=hot_heat', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('li > .tit > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, fecth_type='js')
            next = response.doc('.next').attr.href
            self.crawl(next, callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
