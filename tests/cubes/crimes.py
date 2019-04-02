#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "crimes"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Cases']


class CountMeasuresTestCase(unittest.TestCase):
    def test_crime_crime(self):
        level_fullname = "[Crime].[Crime]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 58128.0)

    def test_crime_crimegroup(self):
        level_fullname = "[Crime].[Crime Group]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 58128.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 58128.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 58128.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 58128.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_crime_crime(self):
        level_fullname = "[Crime].[Crime]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Cases"
        measure_sum = sum(item["Cases"] for item in result)
        self.assertEqual(measure_sum, 10537426.0)

    def test_crime_crimegroup(self):
        level_fullname = "[Crime].[Crime Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Cases"
        measure_sum = sum(item["Cases"] for item in result)
        self.assertEqual(measure_sum, 10537426.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Cases"
        measure_sum = sum(item["Cases"] for item in result)
        self.assertEqual(measure_sum, 10537426.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Cases"
        measure_sum = sum(item["Cases"] for item in result)
        self.assertEqual(measure_sum, 10537426.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Cases"
        measure_sum = sum(item["Cases"] for item in result)
        self.assertEqual(measure_sum, 10537426.0)
