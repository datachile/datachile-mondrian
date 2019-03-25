#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "death_causes"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Casualities Count SUM']


class CountMeasuresTestCase(unittest.TestCase):
    def test_cie10_cie10(self):
        level_fullname = "[CIE 10].[CIE 10]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1350.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1350.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1350.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1350.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_cie10_cie10(self):
        level_fullname = "[CIE 10].[CIE 10]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Casualities Count SUM"
        measure_sum = sum(item["Casualities Count SUM"] for item in result)
        self.assertEqual(measure_sum, 433436.0)
