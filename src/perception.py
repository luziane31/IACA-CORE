# IACA-CORE: Perception Module
# Handles data input from LiDAR and Camera

from config import Configuration

class PerceptionManager:
    def __init__(self):
        # Carrega as configurações do arquivo config.py
        self.config = Configuration()
        self.is_active = True

    def initialize_sensors(self):
        """Inicializa os sensores baseados na configuração"""
        print(f"Initializing {self.config.SYSTEM_NAME} v{self.config.VERSION}...")
        
        if self.config.USE_LIDAR:
            print("[STATUS] LiDAR Sensor: ONLINE")
        
        if self.config.USE_COMPUTER_VISION:
            print("[STATUS] Computer Vision: ONLINE")

    def process_environment(self):
        """Simulação do processamento inicial (Filtro C0)"""
        if self.config.FILTER_LEVEL == "HIGH":
            print("[FILTER] Applying High-Level C0 Filtering to sensory data...")
        
        if self.config.DATA_NORMALIZATION:
            print("[DATA] Normalizing data streams for cognitive processing.")

# Sequência de inicialização para teste
if __name__ == "__main__":
    perception = PerceptionManager()
    perception.initialize_sensors()
    perception.process_environment()

