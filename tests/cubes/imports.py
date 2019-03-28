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
        self.assertEqual(measure_sum, 366130386312.0)

    def test_country_country(self):
        level_fullname = "[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161981424.3737)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366155739136.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167210952.0836)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366107115389.5)

    def test_imporths_hs_hs0(self):
        level_fullname = "[Import HS].[HS].[HS0]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161774216.0)

    def test_imporths_hs_hs2(self):
        level_fullname = "[Import HS].[HS].[HS2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167730773.76154)

    def test_imporths_hs_hs4(self):
        level_fullname = "[Import HS].[HS].[HS4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366167739419.9306)

    def test_origincountry_country_continent(self):
        level_fullname = "[Origin Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366130386312.0)

    def test_origincountry_country_country(self):
        level_fullname = "[Origin Country].[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "CIF US"
        measure_sum = sum(item["CIF US"] for item in result)
        self.assertEqual(measure_sum, 366161981424.3737)
