#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "mds_abandonment_rate"
MEASURES_SUM = ['Number of Students']


class SumMeasuresTestCase(unittest.TestCase):
    def test_educationlevel_educationlevel(self):
        level_fullname = "[Education Level].[Education Level]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of Students"
        measure_sum = sum(item["Number of Students"] for item in result)
        self.assertEqual(measure_sum, 22769555.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of Students"
        measure_sum = sum(item["Number of Students"] for item in result)
        self.assertEqual(measure_sum, 22769555.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of Students"
        measure_sum = sum(item["Number of Students"] for item in result)
        self.assertEqual(measure_sum, 22769555.0)

    def test_promotionstatus_promotionstatus(self):
        level_fullname = "[Promotion Status].[Promotion Status]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of Students"
        measure_sum = sum(item["Number of Students"] for item in result)
        self.assertEqual(measure_sum, 22769555.0)

    def test_year_year(self):
        level_fullname = "[Year].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of Students"
        measure_sum = sum(item["Number of Students"] for item in result)
        self.assertEqual(measure_sum, 22769555.0)
