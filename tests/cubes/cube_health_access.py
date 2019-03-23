#!/usr/bin/env python3

import unittest
from api import query


CUBE = "health_access"
MEASURES = ['Primary Healthcare SUM', 'Specialized Healthcare SUM', 'Urgency Healthcare SUM']


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Primary Healthcare SUM"
        measure_sum = sum(item["Primary Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 79535259)

        # Check sum for measure "Specialized Healthcare SUM"
        measure_sum = sum(item["Specialized Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 36196737)

        # Check sum for measure "Urgency Healthcare SUM"
        measure_sum = sum(item["Urgency Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 96332494)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Primary Healthcare SUM"
        measure_sum = sum(item["Primary Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 79535259)

        # Check sum for measure "Specialized Healthcare SUM"
        measure_sum = sum(item["Specialized Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 36196737)

        # Check sum for measure "Urgency Healthcare SUM"
        measure_sum = sum(item["Urgency Healthcare SUM"] for item in result)
        self.assertEqual(measure_sum, 96332494)

