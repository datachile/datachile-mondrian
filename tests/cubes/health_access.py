#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "health_access"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Primary Healthcare SUM', 'Specialized Healthcare SUM', 'Urgency Healthcare SUM']
MEASURES_AVG = ['Primary Healthcare AVG', 'Specialized Healthcare AVG', 'Urgency Healthcare AVG', 'Dental Discharges Per 100 inhabitants AVG']


class CountMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 78.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 78.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Primary Healthcare SUM"
        measure_sum = sum(item["Primary Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 79535259.0)

        # Check sum for measure "Specialized Healthcare SUM"
        measure_sum = sum(item["Specialized Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 36196737.0)

        # Check sum for measure "Urgency Healthcare SUM"
        measure_sum = sum(item["Urgency Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 96332494.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Primary Healthcare SUM"
        measure_sum = sum(item["Primary Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 79535259.0)

        # Check sum for measure "Specialized Healthcare SUM"
        measure_sum = sum(item["Specialized Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 36196737.0)

        # Check sum for measure "Urgency Healthcare SUM"
        measure_sum = sum(item["Urgency Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 96332494.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Primary Healthcare AVG"
        average_sum = 5129687.411111111
        average_count = 5
        retrieved_values = [item["Primary Healthcare AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Specialized Healthcare AVG"
        average_sum = 2327705.588888889
        average_count = 5
        retrieved_values = [item["Specialized Healthcare AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Urgency Healthcare AVG"
        average_sum = 6200857.08888889
        average_count = 5
        retrieved_values = [item["Urgency Healthcare AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Dental Discharges Per 100 inhabitants AVG"
        average_sum = 39.81082196765476
        average_count = 5
        retrieved_values = [item["Dental Discharges Per 100 inhabitants AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Primary Healthcare AVG"
        average_sum = 15839270.433333334
        average_count = 15
        retrieved_values = [item["Primary Healthcare AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Specialized Healthcare AVG"
        average_sum = 7168714.966666666
        average_count = 15
        retrieved_values = [item["Specialized Healthcare AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Urgency Healthcare AVG"
        average_sum = 19107283.183333334
        average_count = 15
        retrieved_values = [item["Urgency Healthcare AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Dental Discharges Per 100 inhabitants AVG"
        average_sum = 120.67514924208322
        average_count = 15
        retrieved_values = [item["Dental Discharges Per 100 inhabitants AVG"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

