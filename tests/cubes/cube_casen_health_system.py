#!/usr/bin/env python3

import unittest
from api import query


CUBE = "casen_health_system"
MEASURES = ['Expansion Factor Region', 'Expansion Factor Comuna']


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897)

    def test_healthsystem_healthsystem(self):
        level_fullname = "[Health System].[Health System]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897)

    def test_healthsystem_healthsystemgroup(self):
        level_fullname = "[Health System].[Health System Group]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897)

