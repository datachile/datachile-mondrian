#!/usr/bin/env python3

import unittest
from api import query


CUBE = "election_results_update"
MEASURES = ['Votes']


class SumMeasuresTestCase(unittest.TestCase):
    def test_candidates_candidate(self):
        level_fullname = "[Candidates].[Candidate]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_coalition_coalition(self):
        level_fullname = "[Coalition].[Coalition]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_elected_elected(self):
        level_fullname = "[Elected].[Elected]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_electiontype_electiontype(self):
        level_fullname = "[Election Type].[Election Type]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

    def test_party_partido(self):
        level_fullname = "[Party].[Partido]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Votes"
        measure_sum = sum(item["Votes"] for item in result)
        self.assertEqual(measure_sum, 53111242)

