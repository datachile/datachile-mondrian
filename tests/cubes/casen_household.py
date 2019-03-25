#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "casen_household"
MEASURES_COUNT = ['Number of records']
MEASURES_SUM = ['Expansion Factor Region', 'Expansion Factor Comuna']


class CountMeasuresTestCase(unittest.TestCase):
    def test_affectedbyaccumulationoftrashpublicareas_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Accumulation Of Trash Public Areas].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214178.0)

    def test_affectedbyacousticcontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Acoustic Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214178.0)

    def test_affectedbyaircontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Air Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214178.0)

    def test_affectedbyanimalorinsectplague_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Animal Or Insect Plague].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214178.0)

    def test_affectedbygraffitisoradvertising_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Graffitis Or Advertising].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214178.0)

    def test_affectedbypublicwatersourcecontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Public Water Source Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214178.0)

    def test_affectedbyriverorlakecontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By River Or Lake Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214175.0)

    def test_bathrooms_bathrooms(self):
        level_fullname = "[Bathrooms].[Bathrooms]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 154670.0)

    def test_ceilingmaterial_ceilingmaterial(self):
        level_fullname = "[Ceiling Material].[Ceiling Material]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_cookingenergysource_energysourcesurveyresponse_energysourcesurveyresponse(self):
        level_fullname = "[Cooking Energy Source].[Energy Source Survey Response].[Energy Source Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_credit_credit(self):
        level_fullname = "[Credit].[Credit]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 88943.0)

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_electricity_electricity(self):
        level_fullname = "[Electricity].[Electricity]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_familiesinhousehold_familiesinhousehold(self):
        level_fullname = "[Families In Household].[Families In Household]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 205086.0)

    def test_familymemberowner2_familymemberowner2(self):
        level_fullname = "[Family Member Owner 2].[Family Member Owner 2]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 139403.0)

    def test_familymemberowner_familymemberowner(self):
        level_fullname = "[Family Member Owner].[Family Member Owner]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 140395.0)

    def test_floormaterial_floormaterial(self):
        level_fullname = "[Floor Material].[Floor Material]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_heatingenergysource_energysourcesurveyresponse_energysourcesurveyresponse(self):
        level_fullname = "[Heating Energy Source].[Energy Source Survey Response].[Energy Source Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_hotwaterenergysource_energysourcesurveyresponse_energysourcesurveyresponse(self):
        level_fullname = "[Hot Water Energy Source].[Energy Source Survey Response].[Energy Source Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_householdsinland_householdsinland(self):
        level_fullname = "[Households In Land].[Households In Land]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 166812.0)

    def test_householdsqmeters_householdsqmeters(self):
        level_fullname = "[Household Sq Meters].[Household Sq Meters]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214193.0)

    def test_householdtype_householdtype(self):
        level_fullname = "[Household Type].[Household Type]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_householdusing_householdusing(self):
        level_fullname = "[Household Using].[Household Using]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_landusing_landusing(self):
        level_fullname = "[Land Using].[Land Using]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blocksatm_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Atm].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blockscommunityequipment_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Community Equipment].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blockseducationalcenter_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Educational Center].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blocksgreenareas_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Green Areas].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blockshealthcenter_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Health Center].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blocksmarket_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Market].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blockspharmacy_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Pharmacy].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan20blockssportscenter_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Sports Center].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_lessthan8blockspublictransport_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 8 Blocks Public Transport].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_payingcredit_payingcredit(self):
        level_fullname = "[Paying Credit].[Paying Credit]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 44836.0)

    def test_reasontoshare_reasontoshare(self):
        level_fullname = "[Reason To Share].[Reason To Share]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 9112.0)

    def test_rooms_rooms(self):
        level_fullname = "[Rooms].[Rooms]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 9896.0)

    def test_subsidyorprogram_subsidyorprogram(self):
        level_fullname = "[Subsidy Or Program].[Subsidy or Program]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 139394.0)

    def test_wallsmaterial_wallsmaterial(self):
        level_fullname = "[Walls Material].[Walls Material]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_wastedisposal_wastedisposal(self):
        level_fullname = "[Waste Disposal].[Waste Disposal]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_waterdistribution_waterdistribution(self):
        level_fullname = "[Water Distribution].[Water Distribution]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_watersource_watersource(self):
        level_fullname = "[Water Source].[Water Source]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)

    def test_zoneid_zoneid(self):
        level_fullname = "[Zone Id].[Zone Id]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 214198.0)


class SumMeasuresTestCase(unittest.TestCase):
    def test_affectedbyaccumulationoftrashpublicareas_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Accumulation Of Trash Public Areas].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847770.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114320.0)

    def test_affectedbyacousticcontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Acoustic Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847770.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114320.0)

    def test_affectedbyaircontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Air Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847770.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114320.0)

    def test_affectedbyanimalorinsectplague_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Animal Or Insect Plague].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847770.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114320.0)

    def test_affectedbygraffitisoradvertising_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Graffitis Or Advertising].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847770.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114320.0)

    def test_affectedbypublicwatersourcecontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By Public Water Source Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847770.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114320.0)

    def test_affectedbyriverorlakecontamination_frequencysurveyresponse_frequencysurveyresponse(self):
        level_fullname = "[Affected By River Or Lake Contamination].[Frequency Survey Response].[Frequency Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13847509.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114062.0)

    def test_bathrooms_bathrooms(self):
        level_fullname = "[Bathrooms].[Bathrooms]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 9873931.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 10025329.0)

    def test_ceilingmaterial_ceilingmaterial(self):
        level_fullname = "[Ceiling Material].[Ceiling Material]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_cookingenergysource_energysourcesurveyresponse_energysourcesurveyresponse(self):
        level_fullname = "[Cooking Energy Source].[Energy Source Survey Response].[Energy Source Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_credit_credit(self):
        level_fullname = "[Credit].[Credit]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 5947355.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 6349831.0)

    def test_date_day(self):
        level_fullname = "[Date].[Day]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_date_month(self):
        level_fullname = "[Date].[Month]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_electricity_electricity(self):
        level_fullname = "[Electricity].[Electricity]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_familiesinhousehold_familiesinhousehold(self):
        level_fullname = "[Families In Household].[Families In Household]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13139214.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 13406618.0)

    def test_familymemberowner2_familymemberowner2(self):
        level_fullname = "[Family Member Owner 2].[Family Member Owner 2]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 8793337.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 9230286.0)

    def test_familymemberowner_familymemberowner(self):
        level_fullname = "[Family Member Owner].[Family Member Owner]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 8871424.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 9310386.0)

    def test_floormaterial_floormaterial(self):
        level_fullname = "[Floor Material].[Floor Material]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_heatingenergysource_energysourcesurveyresponse_energysourcesurveyresponse(self):
        level_fullname = "[Heating Energy Source].[Energy Source Survey Response].[Energy Source Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_hotwaterenergysource_energysourcesurveyresponse_energysourcesurveyresponse(self):
        level_fullname = "[Hot Water Energy Source].[Energy Source Survey Response].[Energy Source Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_householdsinland_householdsinland(self):
        level_fullname = "[Households In Land].[Households In Land]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 10249314.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 10767839.0)

    def test_householdsqmeters_householdsqmeters(self):
        level_fullname = "[Household Sq Meters].[Household Sq Meters]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848392.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14114889.0)

    def test_householdtype_householdtype(self):
        level_fullname = "[Household Type].[Household Type]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_householdusing_householdusing(self):
        level_fullname = "[Household Using].[Household Using]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_landusing_landusing(self):
        level_fullname = "[Land Using].[Land Using]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blocksatm_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Atm].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blockscommunityequipment_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Community Equipment].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blockseducationalcenter_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Educational Center].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blocksgreenareas_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Green Areas].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blockshealthcenter_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Health Center].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blocksmarket_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Market].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blockspharmacy_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Pharmacy].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan20blockssportscenter_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 20 Blocks Sports Center].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_lessthan8blockspublictransport_binarysurveyresponse_binarysurveyresponse(self):
        level_fullname = "[Less Than 8 Blocks Public Transport].[Binary Survey Response].[Binary Survey Response]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_payingcredit_payingcredit(self):
        level_fullname = "[Paying Credit].[Paying Credit]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 3607391.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 3974794.0)

    def test_reasontoshare_reasontoshare(self):
        level_fullname = "[Reason To Share].[Reason To Share]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 709463.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 708631.0)

    def test_rooms_rooms(self):
        level_fullname = "[Rooms].[Rooms]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 711271.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 588451.0)

    def test_subsidyorprogram_subsidyorprogram(self):
        level_fullname = "[Subsidy Or Program].[Subsidy or Program]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 8792898.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 9229760.0)

    def test_wallsmaterial_wallsmaterial(self):
        level_fullname = "[Walls Material].[Walls Material]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_wastedisposal_wastedisposal(self):
        level_fullname = "[Waste Disposal].[Waste Disposal]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_waterdistribution_waterdistribution(self):
        level_fullname = "[Water Distribution].[Water Distribution]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_watersource_watersource(self):
        level_fullname = "[Water Source].[Water Source]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)

    def test_zoneid_zoneid(self):
        level_fullname = "[Zone Id].[Zone Id]"
        result = query(CUBE, MEASURES_SUM, level_fullname)

        # Check sum for measure "Expansion Factor Region"
        measure_sum = sum(item["Expansion Factor Region"] for item in result)
        self.assertEqual(measure_sum, 13848677.0)

        # Check sum for measure "Expansion Factor Comuna"
        measure_sum = sum(item["Expansion Factor Comuna"] for item in result)
        self.assertEqual(measure_sum, 14115249.0)
