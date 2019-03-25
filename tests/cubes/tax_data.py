#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "tax_data"
MEASURES_SUM = ['Output', 'Labour', 'Labour Cost', 'Investment', 'Intermediates']


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3508528652786706.5)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 104540839.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 395439072414092.3)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84788575128236.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1709668478798595.0)

    def test_isicrev4_level1(self):
        level_fullname = "[ISICrev4].[Level 1]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3469991258094876.5)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 98299698.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 368932870435224.75)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84776429442333.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1705135284466563.0)

    def test_isicrev4_level2(self):
        level_fullname = "[ISICrev4].[Level 2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3469991258094875.5)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 98299698.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 368932870435224.9)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84776429442333.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1705135284466563.0)

    def test_isicrev4_level3(self):
        level_fullname = "[ISICrev4].[Level 3]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3469991258094874.5)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 98299698.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 368932870435224.9)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84776429442333.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1705135284466563.0)

    def test_isicrev4_level4(self):
        level_fullname = "[ISICrev4].[Level 4]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3469991258094874.0)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 98299698.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 368932870435224.9)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84776429442333.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1705135284466563.0)

    def test_taxgeography_geography_comuna(self):
        level_fullname = "[Tax Geography].[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3472042265599834.0)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 102817535.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 392439765682961.6)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84080962548951.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1691250556091695.0)

    def test_taxgeography_geography_region(self):
        level_fullname = "[Tax Geography].[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Output"
        measure_sum = sum(item["Output"] for item in result)
        self.assertEqual(measure_sum, 3472042265599835.5)

        # Check sum for measure "Labour"
        measure_sum = sum(item["Labour"] for item in result)
        self.assertEqual(measure_sum, 102817535.0)

        # Check sum for measure "Labour Cost"
        measure_sum = sum(item["Labour Cost"] for item in result)
        self.assertEqual(measure_sum, 392439765682961.6)

        # Check sum for measure "Investment"
        measure_sum = sum(item["Investment"] for item in result)
        self.assertEqual(measure_sum, 84080962548951.0)

        # Check sum for measure "Intermediates"
        measure_sum = sum(item["Intermediates"] for item in result)
        self.assertEqual(measure_sum, 1691250556091695.0)
