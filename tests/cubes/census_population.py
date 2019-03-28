#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "census_population"
MEASURES_SUM = ['People']


class SumMeasuresTestCase(unittest.TestCase):
    def test_aboriginalpeople_aboriginalpeople(self):
        level_fullname = "[Aboriginal People].[Aboriginal People]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_aboriginalpeople_aboriginalpeoplegroup(self):
        level_fullname = "[Aboriginal People].[Aboriginal People Group]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_aboriginalpeople_aboriginalpeoplesubgroup(self):
        level_fullname = "[Aboriginal People].[Aboriginal People Subgroup]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_arrivaltochile_yearofarrivaltochile(self):
        level_fullname = "[Arrival To Chile].[Year Of Arrival To Chile]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_arrivaltochile_yearrange(self):
        level_fullname = "[Arrival To Chile].[Year Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_birthcomuna_birthcomuna(self):
        level_fullname = "[Birth Comuna].[Birth Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 9465051.0)

    def test_birthcountry_birthcountry(self):
        level_fullname = "[Birth Country].[Birth Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_birthplace_birthplace(self):
        level_fullname = "[Birth Place].[Birth Place]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_calculatedagerange_age(self):
        level_fullname = "[Calculated Age Range].[Age]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_calculatedagerange_agerange(self):
        level_fullname = "[Calculated Age Range].[Age Range]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_childrenbornalive_childrenbornalive(self):
        level_fullname = "[Children Born Alive].[Children Born Alive]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_childrencurrentlyalive_childrencurrentlyalive(self):
        level_fullname = "[Children Currently Alive].[Children Currently Alive]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_economicactivity_economicactivity(self):
        level_fullname = "[Economic Activity].[Economic Activity]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_formaleducation_formaleducation(self):
        level_fullname = "[Formal Education].[Formal Education]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_habitualresidence_habitualresidence(self):
        level_fullname = "[Habitual Residence].[Habitual Residence]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_highestcourseapproved_highestcourseapproved(self):
        level_fullname = "[Highest Course Approved].[Highest Course Approved]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_highestlevelapproved_highestlevelapproved(self):
        level_fullname = "[Highest Level Approved].[Highest Level Approved]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_nativepeople_nativepeople(self):
        level_fullname = "[Native People].[Native People]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_residence5yearsago_residence5yearsago(self):
        level_fullname = "[Residence 5 Years Ago].[Residence 5 Years Ago]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_residencecomuna5yearsago_residencecomuna5yearsago(self):
        level_fullname = "[Residence Comuna 5 Years Ago].[Residence Comuna 5 Years Ago]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 14859124.0)

    def test_residencecomuna_residencecomuna(self):
        level_fullname = "[Residence Comuna].[Residence Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17107732.0)

    def test_residencecountry5yearsago_residencecountry5yearsago(self):
        level_fullname = "[Residence Country 5 Years Ago].[Residence Country 5 Years Ago]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_residencecountry_residencecountry(self):
        level_fullname = "[Residence Country].[Residence Country]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_sex_sex(self):
        level_fullname = "[Sex].[Sex]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)

    def test_zone_zone(self):
        level_fullname = "[Zone].[Zone]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "People"
        measure_sum = sum(item["People"] for item in result)
        self.assertEqual(measure_sum, 17574003.0)
