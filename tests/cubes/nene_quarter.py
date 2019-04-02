#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "nene_quarter"
MEASURES_COUNT = ['Number of records']


class CountMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerange(self):
        level_fullname = "[Age Range].[Age Range]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_date_movingquarter(self):
        level_fullname = "[Date].[Moving Quarter]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_generaleconomiccondition_generaleconomiccondition(self):
        level_fullname = "[General Economic Condition].[General Economic Condition]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_icse_icse(self):
        level_fullname = "[ICSE].[ICSE]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_isced_isced(self):
        level_fullname = "[ISCED].[ISCED]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030832.0)

    def test_isco_isco(self):
        level_fullname = "[ISCO].[ISCO]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 4353563.0)

    def test_isiccaenes_isiccaenes(self):
        level_fullname = "[ISIC CAENES].[ISIC CAENES]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 2645603.0)

    def test_occupationalsituation_occupationalsituation(self):
        level_fullname = "[Occupational Situation].[Occupational Situation]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 10030835.0)
