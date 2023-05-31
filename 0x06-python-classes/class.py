class user:
    id = 89
    name = "no name"
    __psasword = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name


u = user("John")
print(u.name)
print(u.id)
print(u.is_new)