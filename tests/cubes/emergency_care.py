#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "emergency_care"
MEASURES_SUM = ['Total']


class SumMeasuresTestCase(unittest.TestCase):
    def test_age_age(self):
        level_fullname = "[Age].[Age]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_date_quarter(self):
        level_fullname = "[Date].[Quarter]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_date_week(self):
        level_fullname = "[Date].[Week]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_emergency_actionl1(self):
        level_fullname = "[Emergency].[Action-L1]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_emergency_causel2(self):
        level_fullname = "[Emergency].[Cause-L2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_emergency_namel3(self):
        level_fullname = "[Emergency].[Name-L3]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Total"
        measure_sum = sum(item["Total"] for item in result)
        self.assertEqual(measure_sum, 491940846.0)
