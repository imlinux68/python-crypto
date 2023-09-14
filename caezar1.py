#!/bin/python

alfabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_input = input("Enter a string: ")

input_length = len(str_input)

str_output = ""

for i in range(input_length):
    character = str_input[i]
    location_of_character = alfabets.find(character)
    new_location_of_character = location_of_character + 3
    str_output += alfabets[new_location_of_character]

print("Encrypted text is: ", str_output)