import re
import psycopg2
import random
from collections import Counter


#The Web page provided(HTML code)
web_page = """<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		colour:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="colour:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="colour:orange;">Output</span></p>
<p>
</body>
</html>
""" 

# using regex to extract the colours from the table data(td)
colours = re.findall(r'<td>[A-Z]+<\/td>\s*<td>([A-Z]+(?:, [A-Z]+)*)<\/td>', web_page)

# convert the table data(td) into a single string and split it into a list
colours = ' '.join(colours).split(', ')

"""
1. Which colour of shirt is the mean colour?(mean in this context is 
interpreted as the most common colour, as colours are not numerical values but categorical data.)
"""
mean_colour = Counter(colours).most_common(1)[0][0]

# 2. Which colour is mostly worn throughout the week?
mostly_worn_colour = Counter(colours).most_common(1)[0][0]

# 3. Which colour is the median?
# Sort the colours alphabetically
sorted_colours = sorted(colours)

# Find the number of colours
n = len(sorted_colours)

# Check if the number of colours is odd or even
if n % 2 == 1:
    # If odd, pick the middle colour
    median_colour = sorted_colours[n // 2]
else:
    # If even, average the two middle colours
    middle_index = n // 2
    median_colour = (sorted_colours[middle_index - 1], sorted_colours[middle_index])

# 4. BONUS Get the variance of the colours
colour_frequencies = Counter(colours)
mean_frequency = sum(colour_frequencies.values()) / len(colour_frequencies)
variance = sum((freq - mean_frequency) ** 2 for freq in colour_frequencies.values()) / len(colour_frequencies)

# 5. BONUS if a colour is chosen at random, what is the probability that the color is red?
red_probability = colour_frequencies.get('RED', 0) / sum(colour_frequencies.values())

# 6. Save the colours and their frequencies in PostgreSQL database
'''conn = psycopg2.connect(database="my_database", user="my_name", password="my_password", host="my_host", port="my_port")
cur = conn.cursor()
for color, frequency in colour_frequencies.items():
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))
conn.commit()
conn.close()
'''
# 7. BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_search(arr, target, index=0):
    '''
Description:
The recursive_search function recursively searches for a target element within a given array.

Parameters:

arr: The array to search within.
target: The target element to search for.
index (optional): The starting index for the search. Default is 0.
Returns:

If the target element is found within the array, the function returns the index of the first occurrence of the target element.
If the target element is not found within the array, the function returns -1
'''
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_search(arr, target, index + 1)

#8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10
def generate_binary_number():
    """Generate a random 4-digit binary number."""
    binary_number = ""
    for _ in range(4):
        bit = random.randint(0, 1)
        binary_number += str(bit)
    return binary_number

def binary_to_decimal(binary_number):
    """Convert a binary number to base 10 (decimal)."""
    decimal_number = int(binary_number, 2)
    return decimal_number

# 9. Write a program to sum the first 50 fibonacci sequence.
def fibonacci_sum(n):
    """Calculate the sum of the first n Fibonacci numbers."""
    fib_sum = 0
    fib_prev = 0
    fib_curr = 1
    for _ in range(n):
        fib_sum += fib_curr  # Add current Fibonacci number to sum
        fib_next = fib_prev + fib_curr  # Calculate next Fibonacci number
        fib_prev, fib_curr = fib_curr, fib_next  # Update Fibonacci sequence
    return fib_sum

# Testing the codes above
print("Mean colour:", mean_colour)
print("Mostly worn colour:", mostly_worn_colour)
print("Median colour:", median_colour)
print("Variance:", variance)
print("Probability of choosing red:", red_probability)
print("Recursive search:", recursive_search([1, 2, 3, 4, 5], 3))
print("Random binary number:", generate_binary_number())
print("Binary to decimal:", binary_to_decimal("1010"))
print("Fibonacci sum:", fibonacci_sum(50))
