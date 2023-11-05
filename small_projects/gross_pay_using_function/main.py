import pay_script

# Gross pay with Overtime 1.5 times over 40 hours

try:
    work_hour = float(input("Enter working hours in number.."))
    rate = float(input("Enter rate per hour..."))

    op = pay_script.new_funct(work_hour, rate)
    print(f"Pay: {op}")
except ValueError:
    print("Error, Please enter numeric input only!!!")
