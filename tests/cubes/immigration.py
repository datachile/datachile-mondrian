#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "immigration"
MEASURES_COUNT = ['Number of visas']


class CountMeasuresTestCase(unittest.TestCase):
    def test_activity_activity(self):
        level_fullname = "[Activity].[Activity]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1556618.0)

    def test_calculatedagerange_agerange(self):
        level_fullname = "[Calculated Age Range].[Age Range]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_education_education(self):
        level_fullname = "[Education].[Education]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_origincountry_country_continent(self):
        level_fullname = "[Origin Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_origincountry_country_country(self):
        level_fullname = "[Origin Country].[Country].[Country]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_visatype_visatype(self):
        level_fullname = "[Visa Type].[Visa Type]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)
