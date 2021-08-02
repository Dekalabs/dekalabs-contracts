import brownie
import pytest
from brownie import WhitelistMock, accounts


@pytest.fixture
def whitelistmock():
    return accounts[0].deploy(WhitelistMock)


def test_add_address_to_whitelist(whitelistmock):
    whitelistmock.addAddressToWhitelist(accounts[1])
    assert whitelistmock.whitelist(accounts[1])


def test_add_addresses_to_whitelist(whitelistmock):
    whitelistmock.addAddressesToWhitelist([accounts[1], accounts[2]])
    assert whitelistmock.whitelist(accounts[1])
    assert whitelistmock.whitelist(accounts[2])


def test_remove_address_to_whitelist(whitelistmock):
    whitelistmock.addAddressToWhitelist(accounts[1])
    assert whitelistmock.whitelist(accounts[1])

    whitelistmock.removeAddressFromWhitelist(accounts[1])
    assert not whitelistmock.whitelist(accounts[1])


def test_remove_addresses_to_whitelist(whitelistmock):
    whitelistmock.addAddressesToWhitelist([accounts[1], accounts[2]])
    assert whitelistmock.whitelist(accounts[1])
    assert whitelistmock.whitelist(accounts[2])

    whitelistmock.removeAddressesFromWhitelist([accounts[1], accounts[2]])
    assert not whitelistmock.whitelist(accounts[1])
    assert not whitelistmock.whitelist(accounts[2])


def test_add_address_to_whitelist_only_owner(whitelistmock):
    with brownie.reverts():
        whitelistmock.addAddressToWhitelist(accounts[1], {"from": accounts[1]})
    assert not whitelistmock.whitelist(accounts[1])


def test_call_only_whitelisted(whitelistmock):
    with brownie.reverts():
        whitelistmock.onlyWhitelistedCanDoThis({"from": accounts[1]})

    whitelistmock.addAddressToWhitelist(accounts[1])
    assert whitelistmock.onlyWhitelistedCanDoThis({"from": accounts[1]})
