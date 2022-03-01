# -*- coding: utf-8 -*-

from asyncio import constants


class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            self.doUpdateQuality(item)

    def decquality(self, item):
        if item.quality > 0 and item.quality < 50:
            if item.sell_in >0:
                item.quality = item.quality - 1
                self.updatesellIn(item)
            else:
                item.quality = item.quality - 2
                self.updatesellIn(item)
        else:
            item.quality = item.quality
            self.updatesellIn(item)

    def decqualitytwice(self, item):
        if item.quality > 0 and item.quality < 50:
            if item.sell_in >0:
                item.quality = item.quality - 2
                self.updatesellIn(item)
            else:
                item.quality = item.quality - 4
                self.updatesellIn(item)
        else:
            item.quality = item.quality
            self.updatesellIn(item)

    def incquality(self, item):
        if item.quality < 50 and item.quality >= 0:
            if item.sell_in > 0:
                item.quality = item.quality + 1
            else:
                item.quality = item.quality + 2
        else:
            item.quality = item.quality

    def updatesellIn(self, item):
        item.sell_in = item.sell_in - 1

    def doUpdateQuality(self, item):
        AgedBrie = "Aged Brie"
        BackstagePasses = "Backstage passes to a TAFKAL80ETC concert"
        sulfuras = "Sulfuras, Hand of Ragnaros"
        conjured = "Conjured Mana Cake"
        if item.name == AgedBrie:
            self.incquality(item)
            self.updatesellIn(item)
        elif item.name == BackstagePasses:
            if item.sell_in < 11 and item.sell_in > 5:
                item.quality = item.quality + 2
                self.updatesellIn(item)
            elif item.sell_in < 6 and item.sell_in > 0:
                item.quality = item.quality + 3
                self.updatesellIn(item)
            elif item.sell_in <= 0:
                item.quality = 0
                self.updatesellIn(item)
            else:
                self.incquality(item)
                self.updatesellIn(item)
        elif item.name == sulfuras:
            item.sell_in = item.sell_in
            item.quality = item.quality

        elif item.name == conjured:
            self.decqualitytwice(item)
        else: 
            self.decquality(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
