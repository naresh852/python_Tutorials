
class MinimumDepositError(Exception):
    pass
class MinimumBalanceError(Exception):
    pass

def Bank_ATM(balance ,choice ,amount):
    try:
        updatedbal =balance
        if balance <500:
            raise ValueError("As per the Minimum Balance Policy, Balance must be at least 500")
        elif choice==1:
            if amount <2000:
                raise MinimumDepositError("The Minimum amount of Deposit should be 2000.")
            else:
                updatedbal =balance +amount
        else:
            updatedbal2 =balance -amount
            if updatedbal2 <500:
                raise MinimumBalanceError("You cannot withdraw this amount due to Minimum Balance Policy")
            else:
                updatedbal =balance -amount
    except Exception as e:
        raise e
    else:
        print(f"Updated Balance Amount:  {updatedbal}")





if __name__ == '__main__':

    bal = int(input())
    ch = int(input())
    amt = int(input())

    try:
        Bank_ATM(bal ,ch ,amt)


    except ValueError as e:
        print(e)
    except MinimumDepositError as e:
        print(e)
    except MinimumBalanceError as e:
        print(e)