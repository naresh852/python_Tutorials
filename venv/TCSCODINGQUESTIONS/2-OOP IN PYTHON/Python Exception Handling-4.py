def Library(memberfee, installment, book):
    try:
        x=memberfee/installment

        if installment > 3 and installment!=0:
           raise ValueError("Maximum Permitted Number of Installments is 3")
        else:
           print(f"Amount per Installment is  {x}")

    except ZeroDivisionError:
         raise ZeroDivisionError("Number of Installments cannot be Zero.")

    else:
        Harrypotter = ["philosophers stone", "chamber of secrets", "prisoner of azkaban", "goblet of fire",
                   "order of phoenix", "half blood prince", "deathly hallows 1", "deathly hallows 2"]
        if book.lower() in Harrypotter:
           print("It is available in this section")
        else:
           raise NameError("No such book exists in this section")


if __name__ == '__main__':

    memberfee = int(input())
    installment = int(input())
    book = input()

    try:
        Library(memberfee, installment, book)

    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)