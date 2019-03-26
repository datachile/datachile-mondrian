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
        self.assertEqual(measure_sum, 366129726088.0)

    def test_country_country(self):
        level_fullname = "[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161686831.0505)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366155603968.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366164795033.0154)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366065260808.0)

    def test_imporths_hs_hs0(self):
        level_fullname = "[Import HS].[HS].[HS0]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161109196.0)

    def test_imporths_hs_hs2(self):
        level_fullname = "[Import HS].[HS].[HS2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167726630.7906)

    def test_imporths_hs_hs4(self):
        level_fullname = "[Import HS].[HS].[HS4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167741560.6806)

    def test_origincountry_country_continent(self):
        level_fullname = "[Origin Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366129726088.0)

    def test_origincountry_country_country(self):
        level_fullname = "[Origin Country].[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161686831.0505)
