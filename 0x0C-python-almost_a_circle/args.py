def __init__(self, **kwargs):
    self.street = street,
    self.apt = apt,
    self.city = city,
    self.state = state
    self.zip = zip


@property
def __str__(self):
    return f"{self.street}, {self.apt}, {self.city}, {self.state}, {self.zip}"
