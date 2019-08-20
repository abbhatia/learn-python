# Help methods
help(5)

# all objects methods
dir(5)

# specific documentation
abs.__doc__

# variables

myvar = 3
mystr = "abi"

#You can also use multiple variables on one line
mystr, myvar = myvar, mystr
mystr
myvar

# Common  collections
sample = [1, ["another", "list"], ("a", "tuple")]
sample[-1] # last item

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
mydict["pi"] = 3.15 # This is how you change dictionary values.
mytuple = (1, 2, 3)
myfunction = len
print(myfunction(sample))

# List operations



