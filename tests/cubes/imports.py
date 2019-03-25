#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "imports"
MEASURES_SUM = ['CIF US']


class SumMeasuresTestCase(unittest.TestCase):
    def test_country_continent(self):
        level_fullname = "[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366129893656.0)

    def test_country_country(self):
        level_fullname = "[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161901291.0761)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366156488704.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366164801685.2473)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366064864812.0)

    def test_imporths_hs_hs0(self):
        level_fullname = "[Import HS].[HS].[HS0]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161411628.0)

    def test_imporths_hs_hs2(self):
        level_fullname = "[Import HS].[HS].[HS2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167740962.75934)

    def test_imporths_hs_hs4(self):
        level_fullname = "[Import HS].[HS].[HS4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167741795.4306)

    def test_origincountry_country_continent(self):
        level_fullname = "[Origin Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366129893656.0)

    def test_origincountry_country_country(self):
        level_fullname = "[Origin Country].[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161901291.0761)
