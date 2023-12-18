#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    divisor = []
    
    for count in range(list_length):
        result = 0
    
        try:
            num1 = my_list_1[count] if count < list_length else 0
            num2 = my_list_2[count] if count < list_length else 0
            result = num1 / num2
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            divisor.append(result)
    return divisor
