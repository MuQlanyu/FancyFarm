class Money:
    """
        Класс Суммы денег на карте
    Поля:
        instance: текущая сумма
    """
    instance = None

    @classmethod
    def get_money(cls):
        """Возвращает сумму"""
        if cls.instance is None:
            cls.instance = 0
        return cls.instance

    @classmethod
    def assign(cls, amount):
        """Присваивает сумму"""
        cls.instance = amount

    @classmethod
    def change_money(cls, delta):
        """Изменяют сумму"""
        if cls.instance is None:
            cls.instance = delta
        else:
            cls.instance += delta

