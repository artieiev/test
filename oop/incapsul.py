class BankAccount(object):
	"""BankAcaunt"""
	def __init__(self, name, balance, passport):
		self._name = name
		self.__balance = balance
		self.__passport =passport

	def _print_date(self):
		print(self._name, self.__balance, self.__passport)
		

ac1 = BankAccount('Bob',15400,'6565_78786')
print(ac1._BankAccount__passport)