import my_module

from my_module import multi
from my_module import person


print(my_module.PI) #accessing variable 

multiplication = multi(3,5)
print(multiplication) #accessing function

person_naveen = person("naveen",21,"designer","23/4/2023") 

message = person_naveen.greetings()

print(message)


