def my_function(a):
    if a < 20:
        return
        print("Bad")
    if a < 80:
        return "Passed"
    else:
        return "Good"
print(my_function(15))