# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileipother
from genie.libs.parser.bigip.get_ltm_profileipother import LtmProfileIpother

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/ipother'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:ipother:ipothercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipother?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:ipother:ipotherstate",
                    "name": "ipother",
                    "partition": "Common",
                    "fullPath": "/Common/ipother",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipother/~Common~ipother?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "idleTimeout": "60",
                }
            ],
        }


class test_get_ltm_profileipother(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/ipother",
                "generation": 1,
                "idleTimeout": "60",
                "kind": "tm:ltm:profile:ipother:ipotherstate",
                "name": "ipother",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipother/~Common~ipother?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:ipother:ipothercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipother?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileIpother(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileIpother(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()