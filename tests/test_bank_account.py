from src.my_app.Bank_of_Anders import BankKonto
import pytest

z = BankKonto()


def test_deposit():
    #Kör pytest -s -v och mata in 20.
    expected = "Du har satt in 20.0 kr på ditt konto. Ditt saldo är nu 20.0 kr."
    actual = z.deposit()
    assert actual == expected

def test_check_balance():

    expected = 'Ditt saldo är 20.0 kr.'
    actual = z.account_balance()
    assert actual == expected

#@pytest.mark.skip(reason="no way of currently testing this")
def test_not_enough_balance():
    #Ange 30.
    expected = False
    actual = z.enough_balance()
    assert actual == expected

def test_enough_balance():
    #Ange 10.
    expected = True
    actual = z.enough_balance()
    assert actual == expected


def test_withdraw():
    #Ange 10
    expected = "Du har tagit ut 10.0 kr från ditt konto. Ditt saldo är 10.0 kr."
    actual = z.withdraw()
    assert actual == expected


def test_withdraw_fail():
    #Ange 20
    expected = "Du kan inte ta ut så mycket. Ditt saldo är 10.0 kr."
    actual = z.withdraw()
    assert actual == expected


def interest():
    expected = "Din ränta ligger på 0.0%"
    actual = z.interest()
    assert actual == expected

#20, 30, 10, 10, 20