from Sala import Sala

class Asgard(Sala):
    MAX_ASSENTOS = 30
    MIN_ASSENTOS = 15
    def __init__(self, nro_assentos):  
        super().__init__(nro_assentos)
