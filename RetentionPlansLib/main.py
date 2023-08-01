class RetentionPlansRuler:
    def __init__(self, plan_type: str, snpsht_date: str) -> None:
        plan_type = plan_type.lower()
        match plan_type:
            case "default":
                self.check_period()
            case "gold":
                self.check_period()
            case "platinum":
                self.check_period()
            
    
    def check_period():
        pass