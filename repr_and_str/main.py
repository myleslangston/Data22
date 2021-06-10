class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):  # designed to return something useful. Better for logging as don't always want a string. Just chuck one in when using classes.
        return f"Location(latitude = {self.latitude}, longitude = {self.longitude})"

    def __str__(self):  # similar to repr but returns it as a string. No point having both, either or.
        return f"(latitude = {self.latitude}, longitude = {self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(f"The coordinates for the Birmingham academy are: {bham_academy}")