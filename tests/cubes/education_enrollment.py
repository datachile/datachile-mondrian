#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "education_enrollment"
MEASURES_COUNT = ['Number of records']
MEASURES_AVG = ['Average Age']


class CountMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_institutions_institution_institution(self):
        level_fullname = "[Institutions].[Institution].[Institution]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_teachings_teaching_teaching(self):
        level_fullname = "[Teachings].[Teaching].[Teaching]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 43757282.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 61.29708272672498
        average_count = 5
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 136.75473951749635
        average_count = 12
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 136.75473951749635
        average_count = 12
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 136.75473951749635
        average_count = 12
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 3826.7312559545862
        average_count = 346
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 171.2655138197366
        average_count = 15
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_institutions_institution_institution(self):
        level_fullname = "[Institutions].[Institution].[Institution]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 140627.88827818815
        average_count = 14331
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 30.298412043903674
        average_count = 3
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_teachings_teaching_teaching(self):
        level_fullname = "[Teachings].[Teaching].[Teaching]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 839.0521911684449
        average_count = 40
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 21.9235061896972
        average_count = 2
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

