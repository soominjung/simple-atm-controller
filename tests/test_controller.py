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

class TestSelectAccount:
    def test_success(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        controller.enter_pin("1234")
        controller.select_account("Savings")
        assert controller._selected_account.account_type == "Savings"

    def test_not_authenticated(self):
        controller = ATMController(bank_api=MockBankAPI())
        with pytest.raises(RuntimeError):
            controller.select_account("Checking")

    def test_empty_accounts_list(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "9999-0000-1111-2222"
        controller.insert_card(card)
        controller.enter_pin("9012")
        with pytest.raises(RuntimeError):
            controller.select_account("Checking")

    def test_card_not_in_accounts(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "3333-4444-5555-6666"
        controller.insert_card(card)
        controller.enter_pin("3456")
        with pytest.raises(RuntimeError):
            controller.select_account("Checking")

    def test_account_type_not_found(self):
        controller = ATMController(bank_api=MockBankAPI())
        card = "1111-2222-3333-4444"
        controller.insert_card(card)
        controller.enter_pin("1234")
        with pytest.raises(RuntimeError):
            controller.select_account("Investment")