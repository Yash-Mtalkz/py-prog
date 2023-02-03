class Fees:

    def __init__(self, firstname, lastname, fees):

        self.firstname = firstname
        self.lastname = lastname
        self.fees = fees

    def __str__(self):
        return f'id:{self.id} ' \
               f'firstname: {self.firstname}; ' \
               f'Lastname: {self.lastname}; ' \
               f'Department: {self.fees}'


