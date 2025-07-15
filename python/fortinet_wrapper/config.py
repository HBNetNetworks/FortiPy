"""
Module Name: config.py
Project Name: fortinet-wrapper

Description:
    Loads and stores the config for this project.

Usage:
    This module can be imported to access configuration variables
        or utility functions:
        import config
        print(<your_module_name>.SOME_CONSTANT)

    Or run directly (if applicable):
        python <your_module_name>.py

Author: HBNet Networks
Created: YYYY-MM-DD
Last Modified: YYYY-MM-DD
"""

import os

from dotenv import load_dotenv

load_dotenv()  # load vars from .env into environment

ENVIRONMENT = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
API_KEY = os.getenv("API_KEY", None)

# Additional config logic if needed
if ENVIRONMENT == "production" and not API_KEY:
    raise ValueError("API_KEY must be set in production")
