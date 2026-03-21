# IACA-CORE: Primary Configuration File
# Define sensing parameters

class Configuration:
    SYSTEM_NAME = "IACA-CORE"
    VERSION = "1.0.0"

    # Sensing Settings
    SENSORY_SAMPLING_RATE = 0.5
    USE_LIDAR = True
    USE_COMPUTER_VISION = True

    # C0 Filter (Pre-processing)
    FILTER_LEVEL = "HIGH"
    DATA_NORMALIZATION = True

    # Cognitive Parameters


