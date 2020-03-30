class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def isValidPassword(self):
        hasDigit, hasUpper, hasLower=False, False, False
        
        for c in self.password:
            if c.isupper():
                hasUpper=True
            elif c.islower():
                hasLower=True
            elif c.isdigit():
                hasDigit=True
        
        return [hasDigit, hasLower, hasUpper].count(True)>=2
    
    def validate(self):
        if len(self.password)>=20:
            return True
        if len(self.password)<8:
            return False
        
        return self.isValidPassword()
    