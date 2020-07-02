
# Zero division error
a = 5
b = 0   # if you put 2 hereb than Exception block will not run
try:
    print(a/b)

except Exception as e:      # e is obj of Exception and print the exception error
    print('Cant not divide by zero', e)
print('--------')

# Whenever you open a resource you have to close it also

# it will not show "Resource close" since the program ran successfully, so we will use 'finally'
a = 5
b = 2  # if you put 2 here than Exception block will not run
try:
    print('Resource open')
    print(a/b)
    k = int(input('Enter no. = '))
    print(k)

except Exception as e:      # e is obj of Exception and print the exception error
    print('Cant not divide by zero', e)
except ValueError as e:
    print("Invalid input")
except ZeroDivisionError as e:
    print("Cant not divide by zero")
except Exception:
    print('Something fishy')                # ?Handle all error when we dnt now which type of error will come

finally:
    print("Resource close")
