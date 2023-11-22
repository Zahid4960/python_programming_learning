import sys
sys.path.append("../modules/")

import greetings
import month_converter

print(greetings.say_hi("Zahid")) # Hello Zahid!
print(month_converter.convert_month_from_params("2")) # February
print(month_converter.convert_month_from_params("1kd")) # Invalid params to convert month