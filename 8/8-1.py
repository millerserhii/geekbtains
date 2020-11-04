class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"day - {self.day}, month - {self.month}, year - {self.year}"

    @classmethod
    def extract(cls, str_date):
        day, month, year = map(int, str_date.split('-'))
        spl_date = cls(day, month, year)
        return spl_date

    @staticmethod
    def validate(str_date):
        day, month, year = map(int, str_date.split('-'))
        return "Date is correct" if day <= 31 and month <= 12 and year <= 9999 \
            else "Date is incorrect, check it"


d1 = Date()
print(d1.extract("11-12-1963"))
print(d1.validate("11-12-1963"))
