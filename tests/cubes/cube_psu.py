#!/usr/bin/env python3

import unittest
from api import query


CUBE = "psu"
MEASURES = ['PSU AVG individual']


class SumMeasuresTestCase(unittest.TestCase):
    def test_calculatedpsubucket_bucket(self):
        level_fullname = "[Calculated PSU Bucket].[Bucket]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803)

