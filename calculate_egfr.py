def calculate_egfr(age, weight, serum_creatinine, is_male):
    if is_male:
        constant = 1
    else:
        constant = 0.85

    creatinine_clearance = ((140 - age) * weight) / (serum_creatinine * 72) * constant
    egfr = creatinine_clearance * 0.0113

    return egfr

# Example usage:
age = 40
weight = 70
serum_creatinine = 1.2
is_male = True

egfr = calculate_egfr(age, weight, serum_creatinine, is_male)
print("eGFR:", egfr)
