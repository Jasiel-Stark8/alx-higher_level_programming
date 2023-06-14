# Name, age and bank withdrawal verification

"""parent class Account for account validation and access:"""


class Account:
    """Define and initialize parent class Account"""
    def __init__(self, name, age, bank, password=1234):
        self.name = name
        self.age = age
        self.bank = bank
        self.__password = password

    def validate_age(self):
        """Validate age"""
        while True:
            age = input("Enter your age: ")
            try:
                age = int(age)
            except ValueError:
                print("Please enter numeric digits only.")

            if age < 18 or age > 150:
                print("Please enter a valid age.")
                continue
            break

    @property
    def validate_password(self):
        """Validate Password"""
        while True:
            password = input(print("Enter your password: "))

            if self.__password == password:
                try:
                    self.__password = int(password)
                    print("Access granted.")
                    return render_template("dashboard.html")
                except ValueError:
                    print("Please enter numeric digits only.")
                    continue
            return
