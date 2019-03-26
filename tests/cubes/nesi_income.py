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
        self.assertEqual(measure_sum, 42752529.5)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.484)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752349.5)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.69)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752506.23510742)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.67)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752405.3125)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.688)

    def test_icse_icse(self):
        level_fullname = "[ICSE].[ICSE]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752581.6875)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.684)

    def test_incomerange_incomerange(self):
        level_fullname = "[Income Range].[Income Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752425.875)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.695)

    def test_isced_isced(self):
        level_fullname = "[ISCED].[ISCED]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752634.3125)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.74)

    def test_isco_isco(self):
        level_fullname = "[ISCO].[ISCO]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752387.875)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.656)

    def test_occupationlength_occupationlength(self):
        level_fullname = "[Occupation Length].[Occupation Length]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752312.0)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.645)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752384.0)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.5)

    def test_workday_workday(self):
        level_fullname = "[Workday].[Workday]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Income"
        measure_sum = sum(item["Income"] for item in result)
        self.assertEqual(measure_sum, 107243508845.0)

        # Check sum for measure "Expansion Factor"
        measure_sum = sum(item["Expansion Factor"] for item in result)
        self.assertEqual(measure_sum, 42752936.0)

        # Check sum for measure "Weighted Income"
        measure_sum = sum(item["Weighted Income"] for item in result)
        self.assertEqual(measure_sum, 19075900059462.723)
