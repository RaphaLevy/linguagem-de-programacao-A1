from Sala import Sala

class Midgard(Sala):
    MAX_ASSENTOS = 120
    MIN_ASSENTOS = 60
    def __init__(self, nro_assentos):  
        super().__init__(nro_assentos)
