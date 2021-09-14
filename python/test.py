# enter an age which is type integer
try:
    with open("test.py") as someFile:
        someFile.__exit__
    age = int(input("Age:"))
    xfactor = 10/age
    # someFile.close()        #This will not execute if there is exception in line 4 or 5
except (ValueError, ZeroDivisionError) as x:
    print("You didn't enter age as integer\n")
    print(x, "\ntype of exception: ", type(x))
    # someFile.close()           #This will only be executed in case of exception
else:
    print("No exception\n")
    print("Continue execution")
    # someFile.close()  # This will not execute in case of exception
    # Putting it here and in exception block both.Solution:Use final block
    # will be repititive code
finally:
    someFile.close()


# sequence of execution
# execute try >if error>execute except>
# execute try >if no  error>execute else
