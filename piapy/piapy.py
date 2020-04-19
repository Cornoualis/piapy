import random
import subprocess
from itertools import cycle
from time import sleep


class PiaVpn:
    def __init__(self):
        pass

    @staticmethod
    def regions():
        """
        get VPN servers available
        :return:
        """
        process = subprocess.run(
            ["piactl get regions"], shell=True, capture_output=True
        )

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            regions = process.stdout.decode("utf-8").split("\n")
            regions.remove("auto")
            regions.remove("")

            return regions

    @staticmethod
    def region():
        process = subprocess.run(["piactl get region"], shell=True, capture_output=True)
        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return process.stdout.decode("utf-8").replace("\n", "")

    def set_region(self, server=None):

        regions = self.regions()
        if server is None or server.lower() == "auto":
            server = "auto"
        elif server.lower() == "random":
            server = random.choice(regions)
        elif server not in regions:
            raise ConnectionError("Server must be one of: {}".format(regions))

        args = "piactl set region {}".format(server)
        process = subprocess.run([args], shell=True, capture_output=True)

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return server

    @staticmethod
    def status():
        process = subprocess.run(
            ["piactl get connectionstate"], shell=True, capture_output=True
        )

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return process.stdout.decode("utf-8").replace("\n", "")

    @staticmethod
    def ip():
        process = subprocess.run(["piactl get vpnip"], shell=True, capture_output=True)

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return process.stdout.decode("utf-8").replace("\n", "")

    def connect(self, timeout=20, verbose=False):
        """

        :param timeout: int
        :param verbose: bool
        :return:
        """
        if not isinstance(timeout, int) and not isinstance(verbose, bool):
            raise SystemError(
                'Args have some problems, check them. "timeout" must be integer and "verbose" must be boolean.'
            )

        process = subprocess.run(["piactl connect"], shell=True, capture_output=True)
        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            wait_animation = self._wait_iterator()
            elapsed_time = 0.0
            while self.status().lower() != "connected":
                if int(elapsed_time) == timeout:
                    self.disconnect()
                    raise ConnectionError(
                        "\nConnectionError: Unable to connect to server. Check your internet connection."
                    )
                if verbose:
                    print("\rVPN connecting [{}]".format(next(wait_animation)), end="")
                sleep_time = 0.2
                sleep(sleep_time)
                elapsed_time += sleep_time
            region = self.region()

            if verbose:
                print('\rVPN connected to: "{}"'.format(region))

            return region

    @staticmethod
    def _wait_iterator():
        return cycle("|/-\\")

    @staticmethod
    def disconnect():
        process = subprocess.run(["piactl disconnect"], shell=True, capture_output=True)

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return True

    @staticmethod
    def reset_settings():
        process = subprocess.run(
            ["piactl resetsettings"], shell=True, capture_output=True
        )

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return True

    @staticmethod
    def set_debug_logging(value=True):

        if not isinstance(value, bool):
            raise SystemError('Arg "value" must be a boolean.')

        args = "piactl set debuglogging {}".format(str(value).lower())
        process = subprocess.run([args], shell=True, capture_output=True)

        if process.returncode != 0:
            raise SystemError(process.stderr.decode("utf-8"))
        else:
            return True
