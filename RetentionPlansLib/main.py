from datetime import datetime

class RetentionPlansRuler:
    def __init__(self, plan_type: str, snpsht_date: str) -> None:
        plan_type = plan_type.lower()
        match plan_type:
            case "standard":
                # 42 days
                day = self.check_period_daily(snpsht_date, 42) # for each snapshot of the day
            case "gold":
                # 42 days + 12 moths (372 days) ~= 414 days total
                day =self.check_period_daily(snpsht_date, 42) # for each snapshot of the day
                month = self.check_period_mothly(snpsht_date, 372) # for the last snapshot of month
            case "platinum":
                # 42 days + 12 months (372 days) + 7 years (2604 days) ~= 2646 days total
                day = self.check_period_daily(snpsht_date, 42) # for each snapshot of the day
                month = self.check_period_mothly(snpsht_date, 372) # for the last snapshot of month
                year = self.check_period_yearly(snpsht_date, 2604) # for the last snapshot of year

    """ 
    If any of these bellow return true, there is a snapshot. If it returns false, it doesnt.
    Also, all of them could be resumed in one function where it would get by parameter the length in days to each case, X days, months or years
    and a list of snapshots taken by that ERP instance in the said period etc.
    But they are broke down in three for simplification of cases, since there is no list, id or traceable relations. 
    """
                
    def check_period_daily(target_date, retention_days) -> bool:
        # will not be using -3 UTC
        today = datetime.now()

    def check_period_mothly(target_date, retention_days) -> bool:
        # will not be using -3 UTC
        today = datetime.now()

    def check_period_yearly(target_date, retention_days) -> bool:
        # will not be using -3 UTC
        today = datetime.now()
