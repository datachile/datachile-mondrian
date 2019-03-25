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
        self.assertEqual(measure_sum, 414297322496.0)

    def test_country_country(self):
        level_fullname = "[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414316543563.16895)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414309351424.0)

    def test_destinationcountry_country_continent(self):
        level_fullname = "[Destination Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414297322496.0)

    def test_destinationcountry_country_country(self):
        level_fullname = "[Destination Country].[Country].[Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414316543563.16895)

    def test_exporths_hs_hs0(self):
        level_fullname = "[Export HS].[HS].[HS0]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414313985821.0)

    def test_exporths_hs_hs2(self):
        level_fullname = "[Export HS].[HS].[HS2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414317589287.3282)

    def test_exporths_hs_hs4(self):
        level_fullname = "[Export HS].[HS].[HS4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414317608787.2448)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414314559439.9258)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "FOB US"
        measure_sum = sum(item["FOB US"] for item in result)
        self.assertEqual(measure_sum, 414263362176.0)
