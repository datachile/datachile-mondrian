#!/usr/bin/env python3

import unittest
from api import query


CUBE = "casen_banking"
MEASURES = ['Expansion Factor Region', 'Expansion Factor Comuna']


class SumMeasuresTestCase(unittest.TestCase):
    def test_bankcreditcard_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Bank Credit Card].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_checks_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Checks].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_creditline_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Credit Line].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_debitcard_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Debit Card].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

    def test_storecreditcard_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Store Credit Card].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 41178411)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 41520081)

