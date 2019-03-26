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
        self.assertEqual(measure_sum, 414297263872.0)

    def test_country_country(self):
        level_fullname = "[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414316697995.66504)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414309818368.0)

    def test_destinationcountry_country_continent(self):
        level_fullname = "[Destination Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414297263872.0)

    def test_destinationcountry_country_country(self):
        level_fullname = "[Destination Country].[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414316697995.66504)

    def test_exporths_hs_hs0(self):
        level_fullname = "[Export HS].[HS].[HS0]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414314320214.0)

    def test_exporths_hs_hs2(self):
        level_fullname = "[Export HS].[HS].[HS2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414317588077.1788)

    def test_exporths_hs_hs4(self):
        level_fullname = "[Export HS].[HS].[HS4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414317619056.1784)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414314566226.5039)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414266380096.0)
