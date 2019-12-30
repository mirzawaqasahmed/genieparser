# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorftp
from genie.libs.parser.bigip.get_gtm_monitorftp import GtmMonitorFtp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/ftp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:ftp:ftpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/ftp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:ftp:ftpstate",
                    "name": "ftp",
                    "partition": "Common",
                    "fullPath": "/Common/ftp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/ftp/~Common~ftp?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 10,
                    "mode": "passive",
                    "probeTimeout": 5,
                    "timeout": 31,
                }
            ],
        }


class test_get_gtm_monitorftp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/ftp",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 10,
                "kind": "tm:gtm:monitor:ftp:ftpstate",
                "mode": "passive",
                "name": "ftp",
                "partition": "Common",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/ftp/~Common~ftp?ver=14.1.2.1",
                "timeout": 31,
            }
        ],
        "kind": "tm:gtm:monitor:ftp:ftpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/ftp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorFtp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorFtp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()