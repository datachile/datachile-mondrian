#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "mortality_under_one"
MEASURES_SUM = ['Number of deaths']
MEASURES_AVG = ['Rate Comuna', 'Rate Region', 'Rate Country']


class SumMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerangedeis_agegroup(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 13751.0)

    def test_agerange_agerangedeis_agerange(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 13751.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 13751.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 13751.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 13751.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerangedeis_agegroup(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Group]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 4.750243108454008
        average_count = 1
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 4.765890681473736
        average_count = 1
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 4.652245452006658
        average_count = 1
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_agerange_agerangedeis_agerange(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Range]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 19.00097243381603
        average_count = 4
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 19.063562725894943
        average_count = 4
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 18.608981808026634
        average_count = 4
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 14.250729325362023
        average_count = 3
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 14.297672044421208
        average_count = 3
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 13.956736356019974
        average_count = 3
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 1643.5841155250855
        average_count = 346
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 1648.998175789912
        average_count = 346
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 1609.6769263942974
        average_count = 346
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 68.11497585070751
        average_count = 15
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 72.55628520250322
        average_count = 15
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 69.78368178009987
        average_count = 15
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

