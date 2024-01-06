import matplotlib.pyplot as plt
#==========================================#
# Place your histogram function after this line
def histogram(students: list[dict], attribute: str) -> None:
    # Create a dictionary to count the occurrences of each attribute value
    counts = {}
    for student in students:
        value = student[attribute]
        if isinstance(value, float):
            # Define the intervals for floating point values
            value = int(value // 0.5) * 0.5
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    # Convert the dictionary to two lists for plotting
    values = list(counts.keys())
    frequencies = list(counts.values())

    # Plot the histogram using bar chart
    plt.bar(values, frequencies, width=0.5)
    plt.xlabel(attribute)
    plt.ylabel('Frequency')
    plt.title('Histogram of {}'.format(attribute))
    plt.show()
    
    return None

        

# Do NOT include a main script in your submission
