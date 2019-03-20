#!/usr/bin/env python3

import unittest
from api import query


CUBE = "election_participation"
MEASURES = ['Electors', 'Votes']


class SumMeasuresTestCase(unittest.TestCase):
    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Electors"
        measure_sum = sum(item["Electors"] for item in result)
        self.assertEqual(measure_sum, 42737618)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 18615900)

    def test_electiontype_electiontype(self):
        level_fullname = "[Election Type].[Election Type]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Electors"
        measure_sum = sum(item["Electors"] for item in result)
        self.assertEqual(measure_sum, 42737618)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 18615900)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Electors"
        measure_sum = sum(item["Electors"] for item in result)
        self.assertEqual(measure_sum, 42737618)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 18615900)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Electors"
        measure_sum = sum(item["Electors"] for item in result)
        self.assertEqual(measure_sum, 42737618)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 18615900)

