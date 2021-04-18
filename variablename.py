import re
def variableName(name):
    return not re.findall('([^a-z_0-9])',name.lower()) and not name[0].isdigit()

# Correct variable names consist only of English letters,
# digits and underscores and they can't start with a digit.



# por lo visto ya existe una funcion para esto
def variableName2(name):
    return name.isidentifier()





name1= "var_1__Int"      #true
name2= "qq-q"            #false


print (variableName(name1))

#%%

import re

s="([hi](459))"

print("".join(re.findall('([^a-z0-9])',s)))
