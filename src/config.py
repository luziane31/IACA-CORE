# IACA-CORE: Arquivo de Configuração Principal
# Define os parâmetros de sensoriamento e filtros cognitivos

class Config:
    SYSTEM_NAME = "IACA-CORE"
    VERSION = "1.0.0"
    
    # Configurações de Sensoriamento
    SENSORY_SAMPLING_RATE = 0.5 
    USE_LIDAR = True
    USE_COMPUTER_VISION = True

    # Filtro C0 (Pré-processamento)
    FILTER_LEVEL = "HIGH"
    DATA_NORMALIZATION = True

    # Parâmetros Cognitivos
    COGNITIVE_MODE = "ADAPTIVE"
    LATENCY_THRESHOLD = 150 

config = Config()

