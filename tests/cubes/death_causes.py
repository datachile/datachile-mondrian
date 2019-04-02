#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "death_causes"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Casualities Count SUM']
MEASURES_AVG = ['Casualities Count AVG', 'Casualities rate per 100 inhabitants']


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


class AvgMeasuresTestCase(unittest.TestCase):
    def test_cie10_cie10(self):
        level_fullname = "[CIE 10].[CIE 10]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Casualities Count AVG"
        average_sum = 2889.5733333333333
        average_count = 9
        retrieved_values = [item["Casualities Count AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Casualities rate per 100 inhabitants"
        average_sum = 4.9725926628801975
        average_count = 9
        retrieved_values = [item["Casualities rate per 100 inhabitants"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Casualities Count AVG"
        average_sum = 1605.3185185185184
        average_count = 5
        retrieved_values = [item["Casualities Count AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Casualities rate per 100 inhabitants"
        average_sum = 2.762551479377887
        average_count = 5
        retrieved_values = [item["Casualities rate per 100 inhabitants"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Casualities Count AVG"
        average_sum = 4815.955555555555
        average_count = 15
        retrieved_values = [item["Casualities Count AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Casualities rate per 100 inhabitants"
        average_sum = 8.287654438133663
        average_count = 15
        retrieved_values = [item["Casualities rate per 100 inhabitants"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Casualities Count AVG"
        average_sum = 642.1274074074074
        average_count = 2
        retrieved_values = [item["Casualities Count AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Casualities rate per 100 inhabitants"
        average_sum = 1.1050205917511549
        average_count = 2
        retrieved_values = [item["Casualities rate per 100 inhabitants"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

