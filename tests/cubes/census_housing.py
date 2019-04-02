#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "census_housing"
MEASURES_SUM = ['Housing Units', 'Household', 'People']


class SumMeasuresTestCase(unittest.TestCase):
    def test_ceilingmaterial_ceilingmaterial(self):
        level_fullname = "[Ceiling Material].[Ceiling Material]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_floormaterial_floormaterial(self):
        level_fullname = "[Floor Material].[Floor Material]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_housingoccupation_housingoccupation(self):
        level_fullname = "[Housing Occupation].[Housing Occupation]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_housingtype_housingtype(self):
        level_fullname = "[Housing Type].[Housing Type]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_rooms_rooms(self):
        level_fullname = "[Rooms].[Rooms]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_wallsmaterial_wallsmaterial(self):
        level_fullname = "[Walls Material].[Walls Material]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_watersource_watersource(self):
        level_fullname = "[Water Source].[Water Source]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Housing Units"
        measure_sum = sum(item["Housing Units"] for item in result)
        self.assertEqual(measure_sum, 6338596.0)

        # Check sum for measure "Household"
        measure_sum = sum(item["Household"] for item in result)
        self.assertEqual(measure_sum, 6773962.0)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17130076.0)
