#!/usr/bin/env python3

import unittest
from api import query


CUBE = "population_estimate"
MEASURES = ['Population']


class SumMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerange(self):
        level_fullname = "[Age Range].[Age Range]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Population"
        measure_sum = sum(item["Population"] for item in result)
        self.assertEqual(measure_sum, 279246382)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Population"
        measure_sum = sum(item["Population"] for item in result)
        self.assertEqual(measure_sum, 279246382)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Population"
        measure_sum = sum(item["Population"] for item in result)
        self.assertEqual(measure_sum, 279246382)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Population"
        measure_sum = sum(item["Population"] for item in result)
        self.assertEqual(measure_sum, 279246382)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Population"
        measure_sum = sum(item["Population"] for item in result)
        self.assertEqual(measure_sum, 279246382)

