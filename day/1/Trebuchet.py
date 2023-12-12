#!/usr/bin/env python3
#-*- coding:'utf-8' -*-

def process_line(line):
    list_of_numbers = []
    for char in line:
        #check if character is a number
        if char.isnumeric():
            #add the number to the list
            list_of_numbers.append(str(char))
        #check if not a number    
        elif not char.isnumeric():
            #do nothing.
            continue  
    #sum the first number of the line and the last one
    sum_list = list_of_numbers[0] + list_of_numbers[-1]
    #add to the variable that will send the calibration value
    #sum += sum_list
    return int(sum_list)


def calibration_values(file):
    """

    Function created for working the lookup file.
    :param path(str) -- Path of the calibration document.
    """

    sum = 0
    file = open(file, 'r')
    #read line by line
    for line in file.readlines():
        line_value = process_line(line)
        sum += line_value
    file.close()
    return write_output(sum)

def sum_values(sum):
    sum_integers = 0
    for number in sum:
        #input('Adding {0}'.format(number))
        sum_integers += int(number)
        #print(sum_integers)
    print(sum_integers)

def write_output(text, file='output.txt'):
    output = open(file, 'w')
    output.write(str(text))
    output.close()
    return print('Task completed: please check file: {0}'.format(file))


if __name__ == '__main__':
    calibration_values('input.txt')