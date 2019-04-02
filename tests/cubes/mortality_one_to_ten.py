#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "mortality_one_to_ten"
MEASURES_SUM = ['Number of deaths']
MEASURES_AVG = ['Rate Comuna', 'Rate Region', 'Rate Country']


class SumMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerangedeis_agegroup(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 1815.0)

    def test_agerange_agerangedeis_agerange(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 1815.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 1815.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 1815.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 1815.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Number of deaths"
        measure_sum = sum(item["Number of deaths"] for item in result)
        self.assertEqual(measure_sum, 1815.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_agerange_agerangedeis_agegroup(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Group]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 7.3029227419810185
        average_count = 1
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 5.817192654262668
        average_count = 1
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 5.990730249322951
        average_count = 1
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_agerange_agerangedeis_agerange(self):
        level_fullname = "[Age Range].[Age Range DEIS].[Age Range]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 14.605845483962035
        average_count = 2
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 11.634385308525337
        average_count = 2
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 11.981460498645902
        average_count = 2
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 29.211690967924074
        average_count = 4
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 23.268770617050674
        average_count = 4
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 23.962920997291803
        average_count = 4
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 2526.8112687254325
        average_count = 346
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 2012.7486583748832
        average_count = 346
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 2072.792666265741
        average_count = 346
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 101.81823384314104
        average_count = 15
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 93.19269652757794
        average_count = 15
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 89.86095373984426
        average_count = 15
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Rate Comuna"
        average_sum = 14.605845483962039
        average_count = 2
        retrieved_values = [item["Rate Comuna"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Region"
        average_sum = 11.634385308525337
        average_count = 2
        retrieved_values = [item["Rate Region"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Rate Country"
        average_sum = 11.981460498645902
        average_count = 2
        retrieved_values = [item["Rate Country"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

