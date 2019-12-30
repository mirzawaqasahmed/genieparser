# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_sflowvlan
from genie.libs.parser.bigip.get_sys_sflowvlan import SysSflowVlan

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/sflow/global-settings/vlan'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:sflow:global-settings:vlan:vlanstate",
            "selfLink": "https://localhost/mgmt/tm/sys/sflow/global-settings/vlan?ver=14.1.2.1",
            "pollInterval": 10,
            "samplingRate": 2048,
        }


class test_get_sys_sflowvlan(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:sys:sflow:global-settings:vlan:vlanstate",
        "pollInterval": 10,
        "samplingRate": 2048,
        "selfLink": "https://localhost/mgmt/tm/sys/sflow/global-settings/vlan?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSflowVlan(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSflowVlan(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()