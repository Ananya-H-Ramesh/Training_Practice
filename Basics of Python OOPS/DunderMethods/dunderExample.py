import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(process)s %(levelname)s %(message)s"
                    )


class BankAccount:
    '''Class Representing bank account with simple operations'''

    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def __add__(self, amount):
        """
        Add the given amount to the account balance.

        Args:
            amount (float): The amount to be added to the balance.
        Returns:
            self: The updated object.
        Raises:
            ValueError: If the amount is less than or equal to 0.
        """
        try:
            if amount > 0:
                self.balance += amount
                logging.info(f'Added {amount} to account {self.account_number}')
            else:
                raise ValueError('Invalid amount')
                
        except ValueError as e:
            logging.error(str(e))
        return self
        

    def __sub__(self, amount):
        """
        Subtract the given amount from the account balance.
        Args:
            amount (float): The amount to be subtracted from the balance.
        Returns:
            self: The updated object.
        Raises:
            ValueError: If the amount is greater than the current balance.
        """
        try:
            if amount <= self.balance:
                self.balance -= amount
                logging.info(f'Subtracted {amount} from account {self.account_number}')
            else:
                raise ValueError('Insufficient funds or invalid amount')
            
        except ValueError as e:
            logging.error(str(e))
        return self
        

    def __str__(self):
        """
        Return a string representation of the account.

        Returns:
            str: A formatted string that includes the account number and balance.
        """
        return f'Account Number: {self.account_number}\nBalance: {self.balance}'


