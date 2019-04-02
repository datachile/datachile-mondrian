#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "education_employability"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Sum anual payment 2016']
MEASURES_AVG = ['Avg subsidized', 'Avg Retention 1st year', 'Avg Duration in semesters', 'Avg employability 1st year', 'Avg anual payment 2016']


class CountMeasuresTestCase(unittest.TestCase):
    def test_accreditations_accreditation(self):
        level_fullname = "[Accreditations].[Accreditation]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)

    def test_avgincome4thyear_avgincome4thyear(self):
        level_fullname = "[Avg Income 4th year].[Avg Income 4th year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)

    def test_careers_career(self):
        level_fullname = "[Careers].[Career]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)

    def test_careers_careergroup(self):
        level_fullname = "[Careers].[Career Group]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)

    def test_higherinstitutions_higherinstitution(self):
        level_fullname = "[Higher Institutions].[Higher Institution]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)

    def test_higherinstitutions_higherinstitutiongroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Group]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)

    def test_higherinstitutions_higherinstitutionsubgroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Subgroup]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 1641.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_accreditations_accreditation(self):
        level_fullname = "[Accreditations].[Accreditation]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)

    def test_avgincome4thyear_avgincome4thyear(self):
        level_fullname = "[Avg Income 4th year].[Avg Income 4th year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)

    def test_careers_career(self):
        level_fullname = "[Careers].[Career]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)

    def test_careers_careergroup(self):
        level_fullname = "[Careers].[Career Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)

    def test_higherinstitutions_higherinstitution(self):
        level_fullname = "[Higher Institutions].[Higher Institution]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)

    def test_higherinstitutions_higherinstitutiongroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)

    def test_higherinstitutions_higherinstitutionsubgroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Subgroup]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Sum anual payment 2016"
        measure_sum = sum(item["Sum anual payment 2016"] for item in result)
        self.assertEqual(measure_sum, 3784407743.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_accreditations_accreditation(self):
        level_fullname = "[Accreditations].[Accreditation]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 6.209844753996062
        average_count = 7
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 5.058715402304616
        average_count = 7
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 77.59432239668745
        average_count = 7
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 5.416174654052235
        average_count = 7
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 16136716.468365189
        average_count = 7
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_avgincome4thyear_avgincome4thyear(self):
        level_fullname = "[Avg Income 4th year].[Avg Income 4th year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 18.62406099635095
        average_count = 24
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 18.948662542638854
        average_count = 24
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 314.428235299632
        average_count = 24
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 20.20471564544752
        average_count = 24
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 77983951.25281197
        average_count = 24
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_careers_career(self):
        level_fullname = "[Careers].[Career]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 498.21271275678225
        average_count = 577
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 334.41940667186725
        average_count = 577
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 4110.836419317359
        average_count = 577
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 427.77373735884834
        average_count = 577
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 1144389055.8031945
        average_count = 577
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_careers_careergroup(self):
        level_fullname = "[Careers].[Career Group]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 5.190751108196083
        average_count = 6
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 4.445964759084694
        average_count = 6
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 74.07972689877101
        average_count = 6
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 4.570797954397048
        average_count = 6
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 15716212.727196923
        average_count = 6
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_higherinstitutions_higherinstitution(self):
        level_fullname = "[Higher Institutions].[Higher Institution]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 114.96220987460572
        average_count = 130
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 78.9634102010748
        average_count = 130
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 1173.3633305282776
        average_count = 130
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 97.7679496363987
        average_count = 130
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 245983442.97848535
        average_count = 130
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_higherinstitutions_higherinstitutiongroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Group]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 2.7869858257068763
        average_count = 3
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 2.085204854432699
        average_count = 3
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 28.791349967966354
        average_count = 3
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 2.2035001697877323
        average_count = 3
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 5503902.104070172
        average_count = 3
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_higherinstitutions_higherinstitutionsubgroup(self):
        level_fullname = "[Higher Institutions].[Higher Institution Subgroup]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg subsidized"
        average_sum = 4.490076652153261
        average_count = 5
        retrieved_values = [item["Avg subsidized"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Retention 1st year"
        average_sum = 3.6741005694203057
        average_count = 5
        retrieved_values = [item["Avg Retention 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg Duration in semesters"
        average_sum = 55.58841595298772
        average_count = 5
        retrieved_values = [item["Avg Duration in semesters"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg employability 1st year"
        average_sum = 3.8674669402665307
        average_count = 5
        retrieved_values = [item["Avg employability 1st year"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg anual payment 2016"
        average_sum = 11300392.32588777
        average_count = 5
        retrieved_values = [item["Avg anual payment 2016"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

