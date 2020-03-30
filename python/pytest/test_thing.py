from thing import PasswordValidator

def test_invalid_empty_password():
    password_validate = PasswordValidator("")
    assert False == password_validate.validate()

def test_invalid_less_8_chars():
    password_validate = PasswordValidator("1234")
    assert False == password_validate.validate()

def test_valid_more_20chars():
    password_validate = PasswordValidator("12341234abcccccscdjdsncdj")
    assert True == password_validate.validate()

def test_invalid_more_8chars_all_upper():
    password_validate = PasswordValidator("TTTTTTTT")
    assert False == password_validate.validate()

def test_valid_more_8chars_upper_lower():
    password_validate = PasswordValidator("TTTTTTTt")
    assert True == password_validate.validate()

def test_valid_more_8chars_upper_digit():
    password_validate = PasswordValidator("TTTTTTT1")
    assert True == password_validate.validate()

def test_valid_more_8chars_lower_digit():
    password_validate = PasswordValidator("ttttttt1")
    assert True == password_validate.validate()
