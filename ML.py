ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# Sort the list again after adding min and max ages
ages.sort()

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]

# Find the average age
average_age = sum(ages) / n

# Find the range of the ages
range_of_ages = max_age - min_age

# Print the results
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")
print(f"Median age: {median_age}")
print(f"Average age: {average_age}")
print(f"Range of ages: {range_of_ages}")
