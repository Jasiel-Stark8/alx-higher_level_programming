class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass_fail(self, marks):
        try:
            if marks > 70:
                return 'PASS'
            return 'FAIL'
        except ValueError:
            print("Invalid marks")
