import pytest
from atm.controller import ATMController

class TestInsertCard:
    def test_success(self):
        controller = ATMController()
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        assert controller._card == card

    def test_already_inserted(self):
        controller = ATMController()
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        with pytest.raises(RuntimeError):
            controller.insert_card("5555-6666-7777-8888")