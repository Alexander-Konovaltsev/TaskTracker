from PyQt6.QtWidgets import QLabel, QLineEdit, QComboBox
from widgets.combo_box import ComboBox

def empty_fields_check(fields_list: list[list[QLineEdit | QLabel | QComboBox]]) -> int:
    errors = 0
    for fields in fields_list:
        fields[2].setVisible(False)

    for fields in fields_list:
        if type(fields[1]) is not ComboBox:
            if len(fields[1].text()) == 0 or fields[1].text().isspace():
                fields[2].setText(f"Необходимо заполнить «{fields[0].text()}»")
                fields[2].setVisible(True)
                errors += 1
        else: 
            if fields[1].currentIndex() == -1:
                fields[2].setText(f"Необходимо выбрать «{fields[0].text()}»")
                fields[2].setVisible(True)
                errors += 1
    return errors

def emai_check(email_input: QLineEdit, email_validation_text: QLabel) -> bool:
    email_validation_text.setVisible(False)
    email = email_input.text()
    
    def email_validation_fail():
        email_validation_text.setText("Значение не является правильным email адресом")
        email_validation_text.setVisible(True)

    if '@' not in email:
        email_validation_fail()
        return False
    
    dog_index = email.index('@')
    if len(email[:dog_index]) == 0:
        email_validation_fail()
        return False

    if '.' not in email[dog_index + 1:]:
        email_validation_fail()
        return False

    dot_index = email.index('.')
    if len(email[dog_index + 1:dot_index]) == 0:
        email_validation_fail()
        return False

    if len(email[dot_index + 1:]) == 0:
        email_validation_fail()
        return False
    
    return True
