"""Password Policy Class to handle the data."""

class PasswordPolicy:
    """Simplify handling the password data."""

    def __init__(self, minimum, maximum, character, password):
        """Constructor dunder method."""
        self.minimum = minimum
        self.maximum = maximum
        self.character = character
        self.password = password

    def is_valid_password(self):
        """Check if the password fits its rules."""
        char_count = 0
        for char in self.password:
            if char_count > self.maximum:
                return False
            if char == self.character:
                char_count+=1
        
        if char_count <= self.maximum and char_count >= self.minimum:
            return True