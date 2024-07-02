steps_taken=int(input("enter the number of  steps you have taken:"))
time_elapsed=int(input("enter the time elapsed in minute"))
if steps_taken >= 1000 and time_elapsed <= 10:
    print(True)
else:
    print(False)