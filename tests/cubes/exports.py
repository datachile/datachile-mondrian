#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "exports"
MEASURES_SUM = ['FOB US']


class SumMeasuresTestCase(unittest.TestCase):
    def test_country_continent(self):
        level_fullname = "[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414297706496.0)

    def test_country_country(self):
        level_fullname = "[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414316305677.0713)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414308814848.0)

    def test_destinationcountry_country_continent(self):
        level_fullname = "[Destination Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414297706496.0)

    def test_destinationcountry_country_country(self):
        level_fullname = "[Destination Country].[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414316305677.0713)

    def test_exporths_hs_hs0(self):
        level_fullname = "[Export HS].[HS].[HS0]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414314223389.0)

    def test_exporths_hs_hs2(self):
        level_fullname = "[Export HS].[HS].[HS2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414317603497.34467)

    def test_exporths_hs_hs4(self):
        level_fullname = "[Export HS].[HS].[HS4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414317607608.5573)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414314489632.53516)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414313367696.0)
