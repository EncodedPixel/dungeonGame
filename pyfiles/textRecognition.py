#! /usr/bin/python2
#coding=utf-8

"""
Yet to be named dungeonGame
by EncodedPixel
coded by タダノデーモン(tadanodaemon)

This program will contain all the class used for Text Recognition
"""

class TextRecognition(object):

    def __init__(self):
        self.modes = []
        self.function = None

    def inputHandler(self, **kwargs):
        kwargs['screen'].refocus()
        string = kwargs['string']
        inputs = string.lower().split()
        kwargs['string'] = inputs
        screenName = kwargs['screen'].name
        screenName = kwargs['screen'].name
        self.function = kwargs['screen'].responce
        if 'gamescreen' == screenName:
            self.gameScreenInputHandler(kwargs)
        elif 'battlescreen' == screenName:
            self.battleScreenInputHandler(kwargs)
        else:
            self.function(kwargs)

    def gameScreenInputHandler(self, kwargs):
        if 'upStat' in self.modes:
            kwargs['screen'].usr.confirmUpgradeStat(kwargs['string'])
        elif 'story' in self.modes:
            pass
        elif 'dungeon' in self.modes:
            pass
        else:
            self.function(kwargs)

    def battleScreenInputHandler(self, kwargs):
        if kwargs['screen'].pressEnter.y == 410:
            kwargs['screen'].arena.enterPressed = True
            kwargs['screen'].pressEnter.slideOut.start(kwargs['screen'].pressEnter)
            kwargs['screen'].pressEnter.fadeOut.start(kwargs['screen'].pressEnter)
            kwargs['screen'].textinput.text = ''
        else:
            if kwargs['string']:
                kwargs['screen'].goCheckEm(kwargs['string'])
