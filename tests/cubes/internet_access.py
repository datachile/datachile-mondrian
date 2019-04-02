#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "internet_access"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Expansion factor']


class CountMeasuresTestCase(unittest.TestCase):
    def test_cellphoneaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Cellphone Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_desktopaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Desktop Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_gamesorconsolesaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Games or Consoles Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_homeaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Home Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_internetplan_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Internet Plan].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_laptopaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Laptop Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_tabletaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Tablet Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_tvaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[TV Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3600.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_cellphoneaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Cellphone Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662253.75)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662249.5)

    def test_desktopaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Desktop Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662255.75)

    def test_gamesorconsolesaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Games or Consoles Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662250.84375)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662252.046875)

    def test_homeaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Home Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662250.375)

    def test_internetplan_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Internet Plan].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662250.532958984)

    def test_laptopaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Laptop Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662257.125)

    def test_tabletaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Tablet Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662256.5)

    def test_tvaccess_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[TV Access].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662253.0)

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion factor"
        measure_sum = sum(item["Expansion factor"] for item in result)
        self.assertEqual(measure_sum, 4662253.125)
