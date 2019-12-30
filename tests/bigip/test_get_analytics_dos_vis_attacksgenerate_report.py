# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_analytics_dos_vis_attacksgenerate_report
from genie.libs.parser.bigip.get_analytics_dos_vis_attacksgenerate_report import (
    AnalyticsDosvisattacksGeneratereport,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/analytics/dos-vis-attacks/generate-report'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [],
            "generation": 0,
            "kind": "tm:analytics:dos-vis-attacks:generate-report:avrreporttaskcollectionstate",
            "lastUpdateMicros": 0,
            "selfLink": "https://localhost/mgmt/tm/analytics/dos-vis-attacks/generate-report",
        }


class test_get_analytics_dos_vis_attacksgenerate_report(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [],
        "kind": "tm:analytics:dos-vis-attacks:generate-report:avrreporttaskcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/analytics/dos-vis-attacks/generate-report",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AnalyticsDosvisattacksGeneratereport(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AnalyticsDosvisattacksGeneratereport(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()