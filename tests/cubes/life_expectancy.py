#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "life_expectancy"
MEASURES_COUNT = ['Number of records']
MEASURES_AVG = ['Life Expectancy AVG', 'Mortality rate per 100 inhabitants AVG']


class CountMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 150.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 150.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 150.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Life Expectancy AVG"
        average_sum = 387.65832901000977
        average_count = 5
        retrieved_values = [item["Life Expectancy AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Mortality rate per 100 inhabitants AVG"
        average_sum = 2.8296666642030077
        average_count = 5
        retrieved_values = [item["Mortality rate per 100 inhabitants AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Life Expectancy AVG"
        average_sum = 1162.9749870300293
        average_count = 15
        retrieved_values = [item["Life Expectancy AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Mortality rate per 100 inhabitants AVG"
        average_sum = 8.488999992609024
        average_count = 15
        retrieved_values = [item["Mortality rate per 100 inhabitants AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Life Expectancy AVG"
        average_sum = 155.0633316040039
        average_count = 2
        retrieved_values = [item["Life Expectancy AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Mortality rate per 100 inhabitants AVG"
        average_sum = 1.131866665681203
        average_count = 2
        retrieved_values = [item["Mortality rate per 100 inhabitants AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

