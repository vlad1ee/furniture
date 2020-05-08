class Furniture:
    def __init__(self, bed, wardrobe, table):
        self.bed = bed
        self.wardrobe = wardrobe
        self.table = table
        

class House(Furniture):
    def __init__(self, bed, wardrobe, table, household_type, total_area):
        super().__init__(bed, wardrobe, table)
        self.household_type = household_type
        self.total_area = total_area
        self.furniture_name_list = [self.bed, self.wardrobe, self.table]
        self.remaining_area = None
    
    def area(self):
            self.remaining_area = self.total_area - (self.bed + self.wardrobe + self.table)
            return self.remaining_area

    def __str__(self):
            return f'''household_type: {self.household_type}, total_area: {self.total_area} m2, remaining_area: {self.remaining_area} m2, furniture_name_list: {self.furniture_name_list}'''

house = House(4, 2, 1.5, 'some type', 50)
house.area()
print(house)
