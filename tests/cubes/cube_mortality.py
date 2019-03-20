#!/usr/bin/env python3

import unittest
from api import query


CUBE = "mortality"
MEASURES = ['Number of deaths']


class SumMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerangedeis_agegroup(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Group]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 0)

    def test_agerange_agerangedeis_agerange(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Range]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 0)

