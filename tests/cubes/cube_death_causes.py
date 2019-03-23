#!/usr/bin/env python3

import unittest
from api import query


CUBE = "death_causes"
MEASURES = ['Casualities Count SUM']


class SumMeasuresTestCase(unittest.TestCase):
    def test_cie10_cie10(self):
        level_fullname = "[CIE 10].[CIE 10]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436)

