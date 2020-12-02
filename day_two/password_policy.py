"""Password Policy Class to handle the data."""

class PasswordPolicy:
    """Simplify handling the password data."""

    def __init__(self, minimum, maximum, character, password):
        """Constructor dunder method."""
        self.minimum = minimum
        self.maximum = maximum
        self.character = character
        self.password = password

    def is_valid_password_p1(self):
        """Check if the password fits its rules."""
        char_count = 0
        for char in self.password:
            if char_count > self.maximum:
                return False
            if char == self.character:
                char_count+=1
        if char_count <= self.maximum and char_count >= self.minimum:
            return True

    def is_valid_password_p2(self):
        """Check if the password is valid for part two."""
        if self.password[self.minimum-1] == self.character and self.password[self.maximum-1] == self.character:
            return False
        elif self.password[self.minimum-1] == self.character or self.password[self.maximum-1] == self.character:
            return True
        return False