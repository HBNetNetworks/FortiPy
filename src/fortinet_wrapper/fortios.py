"""Module Name: config.py

Project Name: fortinet-wrapper

Description:
    Loads and stores the config for this project.

Usage:
    This module can be imported to access configuration variables
        or utility functions:
        import config

Author: HBNet Networks
"""

from enum import Enum

import requests

# === Enums start here ===

class FortiOSVersion(Enum):
    """FortiOS version"""

    FORTIOS_7_2 = '7.2'
    FORTIOS_7_4 = '7.4'

class APIURL(Enum):
    """API URL for FortiOS"""

    GLOBAL = 'api/v2/cmdb/system/global'
    INTERFACES = 'api/v2/cmdb/system/interface'

# === Enums end here ===

class FortiOS():
    """FortiOS device class

    This class represents a single Fortigate device and is used to perform all
    API functions.
    For initialization the base URL, API Key and FortiOS version is required.
    """

    # Base values to connect to device
    base_url = str()
    api_key = str()
    verify_ssl = bool()
    version = FortiOSVersion

    # Public variables
    system_global = {}

    # Private variables
    _base_headers = {
        'Accept' : 'application/json',
        'Authorization' : str()
        }

    # Device structures
    interfaces = {}

    # === Private methods start here ===

    # TODO: Remove version, set this from system global
    def __init__(
            self, base_url: str,
            api_key: str,
            version: FortiOSVersion,
            *,
            verify_ssl: bool = True,
            get_global: bool = True):
        """Initialize a Fortigate device.

        Initializes

        Args:
            base_url (str, required): Base URL of the device API.
            api_key (str, required): API key for authentication.
            version (FortiOSVersion, required): FortiOS version.
            verify_ssl (bool, optional): Verify SSL certificate? Defaults to True.
            get_global (bool, optional): Get global conf on init? Defaults to True.

        Raises:
            ValueError: If required parameters are not specified.

        Returns:
            None

        """
        # Confirm required parameters are specified
        if not base_url:
            raise ValueError('Base URL is required')
        if not api_key:
            raise ValueError('API Key is required')
        if not version:
            raise ValueError('FortiOS version is required')

        self.base_url = base_url
        self.api_key = api_key
        self.verify_ssl = verify_ssl
        self.version = version

        self._base_headers['Authorization'] = f'Bearer {self.api_key}'

        if get_global: # Retrieve system global information
            self._get_system()

    def _do_get(self, url: str, params: dict | None = None) -> dict:
        """Perform a GET request to device API

        Args:
            url (str, required): API URL.
            params (dict, optional): Additional query parameters.

        Raises:
            ValueError if required parameters are not specified.

        Returns:
            dict: JSON with response from the API call

        """
        if params is None: # If no params specified, use empty dict
            params = {}

        request = requests.get(
            f'{self.base_url}/{url}',
            headers=self._base_headers,
            params=params,
            verify=self.verify_ssl, timeout=10
            )
        if request.status_code == 200:
            return request.json()
        else:
            raise ValueError(
                f'GET request to {url} failed with status \
                code {request.status_code}: {request.text}')

    def _get_system(self):
        """Get basic system information

        Gets the system global configuration and stores it locally
        """
        self.system_global = self._do_get(APIURL.GLOBAL.value)

        self.hostname = self.system_global['results']['hostname']
        self.version = self.system_global['version']
        self.serial = self.system_global['serial']

    # === Private methods end here ===

    # === Public methods start here ===

    def get_system_global(self) -> dict:
        """Get system global configuration

        Returns:
            dict: System global configuration

        """
        if not self.system_global: # If not already retrieved, get it
            self._get_system()
        return self.system_global

    def interface(self,name='') -> list:
        """Get interfaces from the device

        Args:
            name (str, optional): Interface to get. Defaults to '' (all interfaces).

        Returns:
            list: List with dictionary of interface information

        """
        try:
            if name: # If a name is specified get that interface
                response = self._do_get(f'{APIURL.INTERFACES.value}/{name}')
            else: #Get all interfaces
                response = self._do_get(APIURL.INTERFACES.value)
        except ValueError as e:
            raise ValueError(f'Failed to get interfaces: {e}') from e

        return response['results']

    # === Public methods end here ===
