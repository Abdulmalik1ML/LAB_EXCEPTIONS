# Below you have a code that raises an exception , using what you learned do the following:
# Find what type of exception is raised.
# Hanlde the exception in try..except
# If operation successful , print "the operation is successful"
# if operation fails, handle the specific exception that is raised , and print a relevant message.
def additoin(x, y):
     x = 10
     y = 20
  
     print("Addition:", x + b)
try:
    additoin(10, 20)
except NameError:
     print("the operation is not successful")
except Exception as e:
    print(e.__class__)
else:
    print("the operation is successful")
