#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "education_performance_new"
MEASURES_COUNT = ['Number of records']
MEASURES_AVG = ['Average PSU', 'Average NEM']


class CountMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3209428.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3171731.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3171731.0)

    def test_institution_administration(self):
        level_fullname = "[Institution].[Administration]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3152985.0)

    def test_institution_institution(self):
        level_fullname = "[Institution].[Institution]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3152985.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3209428.0)

    def test_year_year(self):
        level_fullname = "[Year].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 3209428.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 2993.24101599792
        average_count = 6
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 33.39913363895076
        average_count = 6
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 150366.83216184567
        average_count = 329
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 1848.1219732527504
        average_count = 329
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 7407.986916426141
        average_count = 15
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 84.37975067422066
        average_count = 15
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_institution_administration(self):
        level_fullname = "[Institution].[Administration]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 2045.408793910675
        average_count = 4
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 22.53893398789396
        average_count = 4
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_institution_institution(self):
        level_fullname = "[Institution].[Institution]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 1881318.0042927386
        average_count = 3973
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 22117.96708175497
        average_count = 3973
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 1004.1852414664304
        average_count = 2
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 11.20098826804954
        average_count = 2
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_year_year(self):
        level_fullname = "[Year].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average PSU"
        average_sum = 6519.621124297931
        average_count = 13
        retrieved_values = [item["Average PSU"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Average NEM"
        average_sum = 72.97593846994914
        average_count = 13
        retrieved_values = [item["Average NEM"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

