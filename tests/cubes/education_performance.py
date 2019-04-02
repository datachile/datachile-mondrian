#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "education_performance"
MEASURES_COUNT = ['Number of records']
MEASURES_AVG = ['Average Score Average (?)']


class CountMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_institutions_institution_institution(self):
        level_fullname = "[Institutions].[Institution].[Institution]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_teachings_teaching_teaching(self):
        level_fullname = "[Teachings].[Teaching].[Teaching]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 37369703.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 31.759553410810305
        average_count = 6
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 61.50450325540738
        average_count = 12
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 61.50450325540738
        average_count = 12
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 61.50450325540738
        average_count = 12
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 1781.4860440825134
        average_count = 346
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 77.23613915287028
        average_count = 15
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_institutions_institution_institution(self):
        level_fullname = "[Institutions].[Institution].[Institution]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 59123.11714292705
        average_count = 11511
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 14.954073472827549
        average_count = 3
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_teachings_teaching_teaching(self):
        level_fullname = "[Teachings].[Teaching].[Teaching]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 140.01092038446794
        average_count = 30
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Score Average (?)"
        average_sum = 16.446702136747685
        average_count = 3
        retrieved_values = [item["Average Score Average (?)"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

