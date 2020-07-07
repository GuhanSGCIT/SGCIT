class Date:
    def __init__(self, date):
        self.date = date.split('/')
        self.day = int(self.date[0])
        self.month = int(self.date[1])
        self.year = int(self.date[2])
        
    def get_validity(self):
        months_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_30_days = [4, 6, 9, 11]
        if self.month not in range(1, 13):
            return False
        
        if self.month in months_31_days:
            max_day = 31
        elif self.month in months_30_days:
            max_day = 30
        elif self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0: #Condition For Leap Year
            max_day = 29
        else:
            max_day = 28
        
        if self.day < 0 or self.day > max_day:
            return False
        
        #Incrementing Date
        new_year = self.year
        if self.day == max_day:
            new_day = 1
            if self.month == 12:
                new_month = 1
                new_year = self.year + 1
            else:
                new_month = self.month + 1
        else:
            new_day = self.day + 1
            new_month = self.month
        
        
        new_date = str(new_day)+"/"+str(new_month)+"/"+str(new_year)
        return new_date
            
def main():
    date = input("Enter date in (DD/MM/YYYY) format: ")
    obj = Date(date)
    res = obj.get_validity()
    if res == False:
        print("Date is invalid!")
    else:
        print("Date is valid!")
        print("Next Day:", res)
    
    
if __name__ == "__main__":
    main()
