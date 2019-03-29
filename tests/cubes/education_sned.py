#!/usr/bin/env python3

import unittest

from tests.api import query

CUBE = "education_sned"
MEASURES_COUNT = ['Number of records']
MEASURES_AVG = ['Avg efectiveness', 'Avg overcoming', 'Avg initiative', 'Avg integration', 'Avg improvement', 'Avg fairness', 'Avg sned_score']


class CountMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66155.0)

    def test_cluster_stage1a(self):
        level_fullname = "[Cluster].[Stage 1a]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_cluster_stage1b(self):
        level_fullname = "[Cluster].[Stage 1b]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_cluster_stage2(self):
        level_fullname = "[Cluster].[Stage 2]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_institutions_institution_administration(self):
        level_fullname = "[Institutions].[Institution].[Administration]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_institutions_institution_institution(self):
        level_fullname = "[Institutions].[Institution].[Institution]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_subsidized100_subsidized100(self):
        level_fullname = "[Subsidized 100%].[Subsidized 100%]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)

    def test_subsidized60_subsidized60(self):
        level_fullname = "[Subsidized 60%].[Subsidized 60%]"
        result = query(CUBE, MEASURES_COUNT, level_fullname)

        # Check sum for measure "Number of records"
        measure_sum = sum(item["Number of records"] for item in result)
        self.assertEqual(measure_sum, 66225.0)


class AvgMeasuresTestCase(unittest.TestCase):
    def test_administration_administration(self):
        level_fullname = "[Administration].[Administration]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 147.06829851699285
        average_count = 3
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 152.71758191907566
        average_count = 3
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 205.68708553981668
        average_count = 3
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 181.6101000051509
        average_count = 3
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 266.1210554167892
        average_count = 3
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 276.5640558066955
        average_count = 3
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 189.50527314173607
        average_count = 3
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_cluster_stage1a(self):
        level_fullname = "[Cluster].[Stage 1a]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 141.69332633476762
        average_count = 3
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 154.1049494026062
        average_count = 3
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 188.61216511936226
        average_count = 3
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 165.4868677547808
        average_count = 3
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 257.99827131793165
        average_count = 3
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 280.05372166780774
        average_count = 3
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 201.6007899169059
        average_count = 3
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_cluster_stage1b(self):
        level_fullname = "[Cluster].[Stage 1b]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 236.6324182543381
        average_count = 5
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 255.39481218788598
        average_count = 5
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 327.7431442471417
        average_count = 5
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 284.1931894696529
        average_count = 5
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 426.1634198952415
        average_count = 5
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 460.60322119445954
        average_count = 5
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 322.45678304960086
        average_count = 5
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_cluster_stage2(self):
        level_fullname = "[Cluster].[Stage 2]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 537.2583454976855
        average_count = 11
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 560.1039856113064
        average_count = 11
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 720.3318866418197
        average_count = 11
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 625.2679091633315
        average_count = 11
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 934.4600029873919
        average_count = 11
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 1012.2942357477286
        average_count = 11
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 691.1539599218821
        average_count = 11
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_date_year(self):
        level_fullname = "[Date].[Year]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 288.1546574608035
        average_count = 6
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 305.7078263669612
        average_count = 6
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 386.914420695887
        average_count = 6
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 335.8671753621696
        average_count = 6
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 509.1751199946004
        average_count = 6
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 555.5059441517725
        average_count = 6
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 378.72657149554806
        average_count = 6
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_comuna(self):
        level_fullname = "[Geography].[Comuna]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 16415.930310448806
        average_count = 346
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 17629.4481620694
        average_count = 346
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 22908.08646639044
        average_count = 346
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 19639.914984763553
        average_count = 346
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 29295.863782145323
        average_count = 346
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 32264.71176893759
        average_count = 346
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 21675.77502637095
        average_count = 346
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_geography_region(self):
        level_fullname = "[Geography].[Region]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 719.8517652140877
        average_count = 15
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 758.9576763113088
        average_count = 15
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 974.5104636605527
        average_count = 15
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 840.9571201038256
        average_count = 15
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 1276.234220377252
        average_count = 15
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 1390.8210470602398
        average_count = 15
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 945.4599759346318
        average_count = 15
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_institutions_institution_administration(self):
        level_fullname = "[Institutions].[Institution].[Administration]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 206.64132015621306
        average_count = 4
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 202.9393911448277
        average_count = 4
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 250.00809737133827
        average_count = 4
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 222.5703021208978
        average_count = 4
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 354.0060560559724
        average_count = 4
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 365.94907052422127
        average_count = 4
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 251.7633956763496
        average_count = 4
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_institutions_institution_institution(self):
        level_fullname = "[Institutions].[Institution].[Institution]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 572270.0130655643
        average_count = 13095
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 609743.7144192345
        average_count = 13095
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 804783.8124059608
        average_count = 13095
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 700825.1209103158
        average_count = 13095
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 1111255.6024566412
        average_count = 13095
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 1211082.3651767035
        average_count = 13095
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 830515.5056501933
        average_count = 13095
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_subsidized100_subsidized100(self):
        level_fullname = "[Subsidized 100%].[Subsidized 100%]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 105.00007960341522
        average_count = 2
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 105.80203361658756
        average_count = 2
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 148.02528473961183
        average_count = 2
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 132.58004563640145
        average_count = 2
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 172.01460152014326
        average_count = 2
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 187.08917667247078
        average_count = 2
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 134.17551516992643
        average_count = 2
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

    def test_subsidized60_subsidized60(self):
        level_fullname = "[Subsidized 60%].[Subsidized 60%]"
        result = query(CUBE, MEASURES_AVG, level_fullname)

        # Check values for measure "Avg efectiveness"
        average_sum = 101.09616264895503
        average_count = 2
        retrieved_values = [item["Avg efectiveness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg overcoming"
        average_sum = 104.41262307304972
        average_count = 2
        retrieved_values = [item["Avg overcoming"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg initiative"
        average_sum = 148.73520599621193
        average_count = 2
        retrieved_values = [item["Avg initiative"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg integration"
        average_sum = 130.88042977066382
        average_count = 2
        retrieved_values = [item["Avg integration"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg improvement"
        average_sum = 168.32405469257597
        average_count = 2
        retrieved_values = [item["Avg improvement"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg fairness"
        average_sum = 186.29853440745148
        average_count = 2
        retrieved_values = [item["Avg fairness"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

        # Check values for measure "Avg sned_score"
        average_sum = 131.57270991097803
        average_count = 2
        retrieved_values = [item["Avg sned_score"] or 0 for item in result]
        self.assertEqual(average_sum, sum(retrieved_values))
        self.assertEqual(average_count, len(retrieved_values))

