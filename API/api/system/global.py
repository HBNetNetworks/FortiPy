"""
system/global API definitions
"""
from enum import Enum

# === Enums start here ===

class Language(Enum):
    """System language"""

    ENGLISH = "english"
    FRENCH = "french"
    SPANISH = "spanish"
    PORTUGESE = "portuguese"
    JAPANESE = "japanese"
    TRACH = "trach"
    SIMCH = "simch"
    KOREAN = "korean"

class AdminHttpsSslVersions(Enum):
    """Admin SSL/TLS versions"""

    V1 = "tlsv1-1"
    V2 = "tlsv1-2"
    V3 = "tlsv1-3"


# === Enums end here ===

# === JSON dict definitions start here ===



# ===JSON dict definitions end here ===
