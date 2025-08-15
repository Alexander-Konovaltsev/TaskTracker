from enum import Enum

class StatusName(Enum):
    OPEN = "Открыт"
    IN_WORK = "В работе"
    MAY_TEST = "Можно тестировать"
    IN_TEST = "Тестируется"
    ON_REVIEW = "На ревью"
    CLOSE = "Закрыт"
