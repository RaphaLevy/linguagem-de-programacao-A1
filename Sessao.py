from datetime import date, time

class Sessao:
    def __init__(self, data, hora):
        self.data = date.fromisoformat() #'AAAA-MM-DD'
        self.hora = time.fromisoformat() #'HH:MM:SS'