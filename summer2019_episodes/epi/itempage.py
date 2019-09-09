#!/usr/bin/python3
# -*- coding: utf-8 -*-

from m3u8 import m3u8 
import misc 
import re 
# from subitempage import subpage 

class page(object):
    """
    """
    def __init__(self, item):
        self.info = item;
        self.title = self.info['title'];
        self.url = self.info['url'];
        self.id = self.url.strip('/').split('/')[-1];
        self.reqs = [
            f"http://t.mtyee.com/ps/s{self.id}.js",
            f"http://t.mtyee.com/ty/yj/s{self.id}.js",
            f"http://t.mtyee.com/ty/yj/s{self.id}.js"
        ]
    def __str__(self, ):
        return self.title;
    def descend(self, ):
        cont = "";
        for req in self.reqs:
            cont += misc.r_get(req);
        m3u8info = re.findall(r'"(https?.*?m3u8),(.*?),(.*?)"', cont);
        m3u8info = [
                {
                **self.info,
                'hls_url': x[0], 
                'nonsense': x[1], 
                'fname': self.info['title']+'/'+misc.unescape(x[2])+".m3u8"
            }
            for x in m3u8info
        ];
        self.m3u8s = [m3u8(x) for x in m3u8info];

if(__name__ == '__main__'):
    item = {
        'title': "shd",
        'url': "http://www.fjisu.tv/tv/5276/"
    }
    x = page(item);
    x.parse();
    for i in x.subitems:
        print(i)
