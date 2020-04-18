


PIAPY
===
Simple Python 3.7 wrapper around the command line interface for The Private Internet Access VPN desktop client.

No additional requirements.

PIA knowledge bank article can be seen [here](https://www.privateinternetaccess.com/helpdesk/kb/articles/pia-desktop-comPmand-line-interface)

Developed and tested on a Linux Ubuntu machine. Not tested on Windows.

Work in progress, feel free to contact me.

## Instructions
 * PIA client must be installed.
 * PIA client must be running to use the connect command
 * Install running:
   * `pip install PiaPy`
* Import the package
  * `from piapy import PiaVpn`
* Initialize a new VPN object with:
  * `new_obj = PiaVpn()`
* Use it.

## Methods

Working on  this . . .

| methods       |args              | expected result  |
|--              |--                 |--                |
|regions         |                            |  |
| region         |  |
| set_region     | server=None, auto, random, server_name |
| connect        | verbose=False, timeout=20 |
| disconnect     |  |
| ip             |  |
| status         |  |


## Example

  working on this ...

    from piapy import PiaVpn

    vpn = PiaVpn()
    vpn.status()
    vpn.disconnect()
    vpn.connect(verbose=True)
    vpn.ip()



## License

With MIT open source license
