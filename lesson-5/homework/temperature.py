def convert_cel_to_far(num):
    return num * 1.8 + 32
def convert_far_to_cel(num):
    return (num - 32) / 1.8


temp = int(input("Enter temperature in degrees F:"))
print(temp, "degrees F =", convert_far_to_cel(temp), "degrees C")
temp2 = int(input("Enter temperature in degrees C:"))
print(temp2, "degrees C =",convert_cel_to_far(temp2) , "degrees F")