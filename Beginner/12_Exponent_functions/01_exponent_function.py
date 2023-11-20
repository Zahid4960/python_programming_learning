def raise_to_power(base_number, power_number):
    result = 1

    for number in range(power_number):
        result *= base_number
    return result
 
print(raise_to_power(2, 3)) # 8
print(raise_to_power(3, 2)) # 9 
print(raise_to_power(2, 6)) # 64