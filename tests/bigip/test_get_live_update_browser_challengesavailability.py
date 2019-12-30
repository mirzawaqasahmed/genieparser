# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_browser_challengesavailability
from genie.libs.parser.bigip.get_live_update_browser_challengesavailability import (
    Live_updateBrowserchallengesAvailability,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/browser-challenges/availability'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "lastCheckDateTime": "1970-01-01T00:00:00Z",
            "status": "no-update-available",
            "kind": "tm:live-update:browser-challenges:availabilitystate",
            "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/availability",
        }


class test_get_live_update_browser_challengesavailability(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:live-update:browser-challenges:availabilitystate",
        "lastCheckDateTime": "1970-01-01T00:00:00Z",
        "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/availability",
        "status": "no-update-available",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBrowserchallengesAvailability(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBrowserchallengesAvailability(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()