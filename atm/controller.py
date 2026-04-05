

class ATMController:
    def __init__(self, bank_api):
        self._card = None
        self._bank_api = bank_api
        self._authenticated = False

    def insert_card(self, card):
        if self._card is not None:
            raise RuntimeError("Card already inserted")
        self._card = card

    def enter_pin(self, pin):
        if self._card is None:
            raise RuntimeError("Card not inserted yet")
        if not self._bank_api.validate_pin(self._card, pin):
            raise RuntimeError("Invalid PIN")
        self._authenticated = True