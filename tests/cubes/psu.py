#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "psu"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['PSU AVG individual']


class CountMeasuresTestCase(unittest.TestCase):
    def test_calculatedpsubucket_bucket(self):
        level_fullname = "[Calculated PSU Bucket].[Bucket]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 5421885.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 5421885.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 5421885.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 5421885.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 5421885.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_calculatedpsubucket_bucket(self):
        level_fullname = "[Calculated PSU Bucket].[Bucket]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "PSU AVG individual"
        measure_sum = sum(item["PSU AVG individual"] for item in result)
        self.assertEqual(measure_sum, 2714363803.0)
