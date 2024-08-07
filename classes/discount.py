class Discount:
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    def __str__(self):
        return f"Скидка: {self.description} ({self.discount_percent}%)"

