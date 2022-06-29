import numpy as np

unit_in = "m"
value_in = 10
unit_out = "in"
unit_type = "lenght"

units_lenght = np.array(  ["m"    , "in" ])
units_convert = np.array([[1      , 25400],
                          [1/25400, 1    ]])

pos_in = np.where(units_lenght == unit_in)
pos_out = np.where(units_lenght == unit_out)

value_out = value_in * float(units_convert[pos_in,pos_out])

print(str(value_out) + " " + unit_out)
