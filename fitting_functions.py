def linear(m,x,b):
    y = (m*x) + b
    return y
def slope_units(x_units,y_units):
    x_unit = x_units.rstrip("s")
    y_unit = y_units.rstrip("s")
    units = x_unit + "/" + y_unit
    return units
def print_equation(m,b,x_units,y_units):
    x_unit = x_units.rstrip("s")
    y_unit = y_units.rstrip("s")
    units = x_unit + "/" + y_unit
    print("The equation of the line is: y =", m ,units , "x +",b, y_unit)

