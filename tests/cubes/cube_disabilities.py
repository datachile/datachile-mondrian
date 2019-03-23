#!/usr/bin/env python3

import unittest
from api import query


CUBE = "disabilities"
MEASURES = ['Expansion Factor Region']


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13028152)

    def test_disabilitygrade_disabilitygrade(self):
        level_fullname = "[Disability Grade].[Disability Grade]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13028152)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13028152)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13028152)

