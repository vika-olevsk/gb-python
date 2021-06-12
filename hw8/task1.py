class Date:
    def __init__(self, d, m, y) -> None:
        self.day = d
        self.month = m
        self.year = y

    @classmethod
    def get_date(cls, date):
        d, m, y = list(map(int, date.split('-')))
        return cls(d, m, y)

    @staticmethod
    def chech_corr(obj):
        if obj.day == 0 or obj.day > 31:
            print('Invalid day!!')
        elif obj.month == 0 or obj.month > 12:
            print('Invalid month!!')
        elif obj.year == 0 or obj.year > 2021:
            print('Invalid year!!')
        else:
            print('Correct date')

    


date1 = Date.get_date('11-10-2995')
print(date1.month)
Date.chech_corr(date1)
