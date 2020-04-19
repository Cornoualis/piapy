import unittest

from piapy.piapy import PiaVpn


class TestPiaVpn(unittest.TestCase):
    def setUp(self):
        self.vpn = PiaVpn()

    def test_set_server1(self):
        wrong_server_name = "Non a server"
        with self.assertRaises(ConnectionError):
            self.vpn.set_region(wrong_server_name)


if __name__ == "__main__":
    unittest.main()
