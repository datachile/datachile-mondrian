#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "casen_health_system"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Expansion Factor Region', 'Expansion Factor Comuna']


class CountMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1746044.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1746044.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1746044.0)

    def test_healthsystem_healthsystem(self):
        level_fullname = "[Health System].[Health System]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1746044.0)

    def test_healthsystem_healthsystemgroup(self):
        level_fullname = "[Health System].[Health System Group]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1746044.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897.0)

    def test_healthsystem_healthsystem(self):
        level_fullname = "[Health System].[Health System]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897.0)

    def test_healthsystem_healthsystemgroup(self):
        level_fullname = "[Health System].[Health System Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 110671513.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 110860897.0)
