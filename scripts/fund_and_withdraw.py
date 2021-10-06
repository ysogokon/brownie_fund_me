from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Account (fund): {account}")
    entrance_fee = fund_me.getEntranceFee()

    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"Account (withdraw): {account}")
    fund_me.withdraw({"from": account})


# 0.25000000000000000
def main():
    fund()
    withdraw()
