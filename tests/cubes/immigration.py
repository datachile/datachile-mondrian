#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "immigration"
MEASURES_COUNT = ['Number of visas']
MEASURES_AVG = ['Average Age']


class CountMeasuresTestCase(unittest.TestCase):
    def test_activity_activity(self):
        level_fullname = "[Activity].[Activity]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1556618.0)

    def test_calculatedagerange_agerange(self):
        level_fullname = "[Calculated Age Range].[Age Range]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_education_education(self):
        level_fullname = "[Education].[Education]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_origincountry_country_continent(self):
        level_fullname = "[Origin Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_origincountry_country_country(self):
        level_fullname = "[Origin Country].[Country].[Country]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)

    def test_visatype_visatype(self):
        level_fullname = "[Visa Type].[Visa Type]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of visas"
        measure_sum = sum(item["Number of visas"] for item in result)
        self.assertEqual(measure_sum, 1494873.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_activity_activity(self):
        level_fullname = "[Activity].[Activity]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 520.235997567966
        average_count = 15
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_calculatedagerange_agerange(self):
        level_fullname = "[Calculated Age Range].[Age Range]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 185.33658011528536
        average_count = 6
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 366.2546662690842
        average_count = 12
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_education_education(self):
        level_fullname = "[Education].[Education]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 175.8925787000318
        average_count = 7
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 10815.382889937166
        average_count = 339
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 462.81666780953645
        average_count = 15
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_origincountry_country_continent(self):
        level_fullname = "[Origin Country].[Country].[Continent]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 200.4540214724419
        average_count = 6
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_origincountry_country_country(self):
        level_fullname = "[Origin Country].[Country].[Country]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 5907.043148597167
        average_count = 177
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 61.027888096477604
        average_count = 2
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_visatype_visatype(self):
        level_fullname = "[Visa Type].[Visa Type]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Average Age"
        average_sum = 225.44069832628546
        average_count = 7
        retrieved_values = [item["Average Age"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

