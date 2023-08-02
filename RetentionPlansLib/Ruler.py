from datetime import date, datetime

class Ruler:
    def classify(self, plan_type: str, expiration_date: str):
        """
        plan_type: 'standard', 'gold', or 'platinum'
        snpsht_date: must be in format dd/mm/yy
        """
        plan_type = plan_type.lower()
        expiration_date = datetime.strptime(expiration_date, '%d/%m/%Y').date()
        retained = "The referred snapshot is retained."
        deleted = "The referred snapshot is deleted."

        match plan_type:
            case "standard":
                # 42 days
                day = self.check_period(expiration_date, 42) # for each snapshot of the day
                if day is False:
                    print(deleted)
                else:
                    print(retained)
            case "gold":
                # 42 days + 12 months (~372 days) ~= 414 days total
                day =self.check_period(expiration_date, 42) # for each snapshot of the day
                month = self.check_period(expiration_date, 372) # for the last snapshot of month
                if day is False and month is False:
                    print(deleted)
                else:
                    print(retained)
            case "platinum":
                # 42 days + 12 months (~372 days) + 7 years (~2604 days) ~= 2646 days total
                day = self.check_period(expiration_date, 42) # for each snapshot of the day
                month = self.check_period(expiration_date, 372) # for the last snapshot of month
                year = self.check_period(expiration_date, 2604) # for the last snapshot of year
                if day is False and month is False and year is False:
                    print(deleted)
                else:
                    print(retained)
                    
    def check_period(self, target_date: date, retention_days: int) -> bool:
        """ 
        If the function bellow return true, there is a snapshot. If it returns false, it doesnt.
        They are called multiple times since there is difference in the storage politics for 
        the last or different occurances of snapshots 
        through time (last of the month for 1 year, the last of the year for 7 years).
        Will not be using -3 UTC
        """
        today = date.today()
        difference_days = target_date - today
        if difference_days.days <= retention_days:
            return True
        else:
            return False
        