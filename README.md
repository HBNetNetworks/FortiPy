# FortiPy

**FortiPy** is a Python wrapper for the FortiOS API, designed to simplify automation and integration with Fortinet devices. It provides a clean, Pythonic interface to interact with FortiGate firewalls.

## Disclaimer

This project is an **independent, community-developed Python wrapper** for Fortinet APIs. It is **not affiliated with, maintained by, or endorsed by Fortinet, Inc.**

All product names, logos, and trademarks used in this project are the property of their respective owners. "Fortinet", "FortiGate", and other associated names are trademarks or registered trademarks of Fortinet, Inc., used here solely for descriptive and interoperability purposes under fair use.


## Features

- Access and manage FortiOS devices via API  
- Designed for easy extension to support FortiManager, FortiSwitch, and FortiAnalyzer in future releases  
- Simplifies common network automation tasks  
- Supports Python 3.6+  

## Installation

    pip install fortipy

## Usage

Basic example:

    from fortipy import FortiOS

    # Initialize connection
    fortigate = FortiOS(host='192.168.1.99', token='your-api-token')

    # Get firewall policies
    policies = fortigate.get_firewall_policies()
    print(policies)

## Roadmap

- Add FortiManager API support  
- Add FortiSwitch API support  
- Add FortiAnalyzer API support  
- Improved error handling and logging  

## Contributing

Contributions and suggestions are welcome! Please open issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

© 2025 Jaco
