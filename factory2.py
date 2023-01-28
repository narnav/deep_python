_isSecureMode = True


class Account(object):
    __numCreated = 0

    def __new__(cls, *args, **kwargs):
        if not _isSecureMode:
            return super(Account, cls).__new__(cls, *args, **kwargs)
        else:
            return SecureAccount(*args, **kwargs)

    def __init__(self, initial):
        self.__balance = initial
        Account.__numCreated += 1

    def deposit(self, amt):
        self.__balance = self.__balance + amt

    def withdraw(self, amt):
        self.__balance = self.__balance - amt

    def getbalance(self):
        return self.__balance


class SecureAccount(object):

    def __init__(self, initial):
        pass

    def deposit(self, amt):
        pass

    def withdraw(self, amt):
        pass

    def getbalance(self):
        pass
