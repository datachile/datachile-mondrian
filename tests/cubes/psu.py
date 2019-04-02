#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "psu"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['PSU AVG individual']
MEASURES_AVG = ['Avg language test', 'Avg math test']


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


class AvgMeasuresTestCase(unittest.TestCase):
    def test_calculatedpsubucket_bucket(self):
        level_fullname = "[Calculated PSU Bucket].[Bucket]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg language test"
        average_sum = 6972.069219505334
        average_count = 14
        retrieved_values = [item["Avg language test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg math test"
        average_sum = 7029.197232998107
        average_count = 14
        retrieved_values = [item["Avg math test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg language test"
        average_sum = 6512.922502452165
        average_count = 13
        retrieved_values = [item["Avg language test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg math test"
        average_sum = 6509.105132152321
        average_count = 13
        retrieved_values = [item["Avg math test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg language test"
        average_sum = 163462.22619767458
        average_count = 346
        retrieved_values = [item["Avg language test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg math test"
        average_sum = 164504.72164398775
        average_count = 346
        retrieved_values = [item["Avg math test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg language test"
        average_sum = 7368.334355690237
        average_count = 15
        retrieved_values = [item["Avg language test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg math test"
        average_sum = 7390.37801082364
        average_count = 15
        retrieved_values = [item["Avg math test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg language test"
        average_sum = 1002.2797516578079
        average_count = 2
        retrieved_values = [item["Avg language test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg math test"
        average_sum = 1003.2250519107647
        average_count = 2
        retrieved_values = [item["Avg math test"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

