#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "nesi_income"
MEASURES_SUM = ['Income', 'Expansion Factor', 'Weighted Income']


class SumMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerange(self):
        level_fullname = "[Age Range].[Age Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752480.5)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.566)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752507.5)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.7)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752510.45629883)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.668)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752601.90625)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.68)

    def test_icse_icse(self):
        level_fullname = "[ICSE].[ICSE]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752665.15625)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.633)

    def test_incomerange_incomerange(self):
        level_fullname = "[Income Range].[Income Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752386.46875)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.7)

    def test_isced_isced(self):
        level_fullname = "[ISCED].[ISCED]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752459.5)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.69)

    def test_isco_isco(self):
        level_fullname = "[ISCO].[ISCO]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752437.1875)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.652)

    def test_occupationlength_occupationlength(self):
        level_fullname = "[Occupation Length].[Occupation Length]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752024.0)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.676)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752474.0)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.492)

    def test_workday_workday(self):
        level_fullname = "[Workday].[Workday]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752718.0)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.684)
