"""Module Name: fortios.py

Project Name: fortinet_wrapper

Description:
    Represents an instance of a FortiOS device.

Usage:
    This module can be imported to create an instance of this class:
        from fortinet_wrapper.fortios import FortiOS

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

    # Private variables
    _base_url: str
    _api_key: str
    _verify_ssl: bool
    _version: FortiOSVersion
    _system_global: dict
    _hostname: str
    _serial: str
    _base_headers = {
        'Accept' : 'application/json',
        'Authorization' : str()
        }

    # Device structures
    _interfaces = {}

    # === Public properties start here ===

    @property
    def base_url(self) -> str:
        """Base URL of the device API

        Returns:
            str: Base URL of the device API

        """
        return self._base_url

    @property
    def api_key(self) -> str:
        """API Key for authentication

        Returns:
            str: API Key for authentication

        """
        return self._api_key

    @property
    def verify_ssl(self) -> bool:
        """Verify SSL certificate?

        Returns:
            bool: True if SSL certificate should be verified, False otherwise

        """
        return self._verify_ssl

    @property
    def version(self) -> FortiOSVersion:
        """FortiOS version

        Returns:
            FortiOSVersion: Version of the FortiOS

        """
        return self._version

    @property
    def hostname(self) -> str:
        """Hostname of the device

        Returns:
            str: Hostname of the device

        """
        return self._system_global.get('results', {}).get('hostname', '')

    @property
    def serial(self) -> str:
        """Serial number of the device

        Returns:
            str: Serial number of the device

        """
        return self.system_global.get('serial', '')

    @property
    def system_global(self) -> dict:
        """System global configuration

        Returns:
            dict: System global configuration

        """
        return self._system_global

    # === Public properties end here ===

    # === Private methods start here ===

    # TODO: Remove version, set this from system global
    def __init__(
            self, base_url: str,
            api_key: str,
            version: FortiOSVersion,
            *,
            verify_ssl: bool = True):
        """Initialize a Fortigate device.

        Initializes

        Args:
            base_url (str, required): Base URL of the device API.
            api_key (str, required): API key for authentication.
            version (FortiOSVersion, required): FortiOS version.
            verify_ssl (bool, optional): Verify SSL certificate? Defaults to True.

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

        self._base_url = base_url
        self._api_key = api_key
        self._verify_ssl = verify_ssl
        self._version = version

        self._base_headers = self._base_headers.copy()  # Copy base headers
        self._base_headers['Authorization'] = f'Bearer {self.api_key}'

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
            f'{self._base_url}/{url}',
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
        try:
            self._system_global = self._do_get(APIURL.GLOBAL.value) # Get system global
        except ValueError as e:
            raise ValueError(f'Failed to get system global configuration: {e}') from e

        self._hostname = self._system_global['results']['hostname']
        self._version = self._system_global['version']
        self._serial = self._system_global['serial']

    # === Private methods end here ===

    # === Public methods start here ===

    def get_system_global(self) -> dict:
        """Get system global configuration

        Returns:
            dict: System global configuration

        """
        if not self._system_global: # If not already retrieved, get it
            self._get_system()
        return self._system_global

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
