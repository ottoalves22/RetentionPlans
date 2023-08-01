# RetentionPlans
Practical test simulating the retention plan of supposed snapshots of ERP instances

## Problem description
Task: Retention Plans:
    When we backup a specific ERP instance, we keep the snapshot copies according to the Retention Plan.
    So, if the rule of the retention plan is to keep the snapshots for 7 days, it would mean that a snapshot created today should be deleted after 7 days, and so on.
    We need to create a lib that receives a retention plan and a date, and it should tell us if the snapshot for this date should be retained or deleted.

    The plans and rules are the following:
    - Standard: 42 days retention
          We will retain each snapshot daily for 42 days
    - Gold: 42 days and 12 months retention
           We will retain each snapshot daily for 42 days
           We will retain the last snapshot of the month for 12 months
    - Platinum (42 days, 12 months and 7 years)
           We will retain each snapshot daily for 42 days
           We will retain the last snapshot of the month for 12 months
           We will retain the last snapshot of the year for 7 years

You need to test your code as a requirement and you can use any library you prefer.