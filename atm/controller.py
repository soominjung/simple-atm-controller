class ATMController:
    def __init__(self):
        self._card = None

    def insert_card(self, card):
        if self._card is not None:
            raise RuntimeError("Card already inserted")
        self._card = card