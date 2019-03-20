#!/usr/bin/env python3

import unittest
from api import query


CUBE = "education_employability"
MEASURES = ['Sum anual payment 2016']


class SumMeasuresTestCase(unittest.TestCase):
    def test_accreditations_accreditation(self):
        level_fullname = "[Accreditations].[Accreditation]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

    def test_avgincome4thyear_avgincome4thyear(self):
        level_fullname = "[Avg Income 4th year].[Avg Income 4th year]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

    def test_careers_career(self):
        level_fullname = "[Careers].[Career]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

    def test_careers_careergroup(self):
        level_fullname = "[Careers].[Career Group]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

    def test_higherinstitutions_higherinstitution(self):
        level_fullname = "[Higher Institutions].[Higher Institution]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

    def test_higherinstitutions_higherinstitutiongroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Group]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

    def test_higherinstitutions_higherinstitutionsubgroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Subgroup]"
        result = query(CUBE, MEASURES, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743)

