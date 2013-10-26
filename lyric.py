#!/usr/bin/env python
#coding=utf-8

import re
import time
import gecimi

__version__ = '0.0.1'

timematch = re.compile(r'(?P<minute>\d+):(?P<second>\d+(.\d+)?)')
lyricmatch = re.compile(r'](?P<content>[^][]*)')


class Lyric(object):

    artist = 'Beyond'
    song = '不再犹豫'

    def __init__(self, song, artist=None, album=None):
        self.song = song
        if artist:
            self.artist = artist
            lrc = gecimi.Lyric(self.song, self.artist)
        else:
            lrc = gecimi.Lyric(self.song)
        self.lyric = lrc.get()

    def play(self):
        print 'playing...'
        lyriclist = []
        for i in self.lyric.split('\n'):
            ltime = timematch.findall(i)
            content = lyricmatch.findall(i)
            for j in ltime:
                sectime = int(j[0])*60+float(j[1])
                lrc = content[len(content) - 1]
                lyriclist.append((sectime, lrc))
        lyriclist.sort()
        lasttime = 0
        for l in lyriclist:
            breaktime = l[0]-lasttime
            time.sleep(breaktime)
            print l[1]
            lasttime = l[0]


if __name__ == '__main__':
    lyric = Lyric('不再犹豫', 'Beyond')
    lyric.play()
