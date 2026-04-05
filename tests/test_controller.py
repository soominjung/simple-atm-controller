import pytest
from atm.controller import ATMController
from atm.bank import MockBankAPI

class TestInsertCard:
    def test_success(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        assert controller._card == card

    def test_already_inserted(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        with pytest.raises(RuntimeError):
            controller.insert_card("5555-6666-7777-8888")

class TestEnterPin:
    def test_success(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        controller.enter_pin("1234")
        assert controller._authenticated

    def test_no_card(self):
        controller = ATMController(bank_api=MockBankAPI())
        with pytest.raises(RuntimeError):
            controller.enter_pin("1234")

    def test_invalid_pin(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        with pytest.raises(RuntimeError):
            controller.enter_pin("0000")