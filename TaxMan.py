class TaxMan:
    def __init__(self, items, percent):
        self.percent = round(float(f'1.{percent[0:-1]}'), 2)
        self.items = items
        self.total = total = 0
    def percent(self):
        return self.percent()
    def myList(self):
        return self.items()
    def calc_total(self):
        self.total = round(sum(list(map(lambda i: i['price'], self.items))) * self.percent, 2)
    def get_total(self):
        return self.total