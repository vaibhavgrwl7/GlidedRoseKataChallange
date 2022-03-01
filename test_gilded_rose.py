# -*- coding: utf-8 -*-
import unittest
from approvaltests.approvals import verify
import approvaltests

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def updateQualityTest(self):
        name = "foo"
        sellIn = 0
        quality = 0
        ret = self.updateQuality(name, sellIn, quality)
        verify(ret)
        #CombinationApprovals.verifyAllCombinations(ret)

    def updateQuality(self, name, sellIn, qaulity):
        items = [Item(name, sellIn, qaulity)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items[0].name
        

        
if __name__ == '__main__':
    unittest.main()
