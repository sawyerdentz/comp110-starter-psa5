"""
Module: data_analyzer

Module that allows us to import, analyze, and graph data that has a linear
relationship.

Authors:
1) Sawyer Dentz - sdentz@sandiego.edu
2) Matt Oderlin - moderlin@sandiego.edu
"""

import matplotlib.pyplot as pp

def separate(data_points):
    """
    Seperates a list of tuples containing x and y values into two lists of x and y values

    Parameters:
    data_points (type: list): A list of tuples containg x and y values

    Returns:
    (type: tuple): A tuple containg a list of x values and a list of y values
    """

    # Initialize empty lists
    x_vals = []
    y_vals = []

    # Loop through data and add values to lists
    for points in data_points:
        x_vals.append(points[0])
        y_vals.append(points[1])

    # Return lists as a tuple
    return (x_vals, y_vals)


def regression_slope(data_points):
    """
    Calculates the slope of the line of best fit for the given data points

    Parameters:
    data_points (type: list): A list of tuples containg x and y values

    Returns:
    (type: float): The slope of the line of best fit
    """

    # Initialize accumulator variables
    sum_xy = 0.0
    sum_xx = 0.0
    sum_x = 0.0
    sum_y = 0.0

    # Loop through data and update accumulators
    for point in data_points:
        sum_x += float(point[0])
        sum_y += float(point[1])

        sum_xy += float(point[0]) * float(point[1])
        sum_xx += float(point[0]) ** 2

    # Calculate mean x and y values
    mean_x = sum_x / len(data_points)
    mean_y = sum_y / len(data_points)
    
    # Calculate the numerator and denomenator of the formula
    numerator = sum_xy - (len(data_points) * mean_x * mean_y)
    denomenator = sum_xx - (len(data_points) * (mean_x ** 2))

    # Return the evaluated formula as a float
    return (numerator / denomenator)


def plot_regression(data_points):
    """
    Plots the line of best fit using the given data points

    Parameters:
    data_points (type: list): A list of tuples containg x and y values

    Returns:
    None
    """

    # Initialize variables
    largest_x = 0.0
    sum_x = 0.0
    sum_y = 0.0

    # Loop through data and update largest_x and accumulator variables
    for point in data_points:
        if point[0] > largest_x:
            largest_x = point[0]
        
        sum_x += point[0]
        sum_y += point[1]
    
    # Calculate mean x and y values
    mean_x = sum_x / len(data_points)
    mean_y = sum_y / len(data_points)

    # Calculate both y1 and y2 values for x=0 and x=largest_x
    y1 = mean_y + regression_slope(data_points) * (0 - mean_x)
    y2 = mean_y + regression_slope(data_points) * (largest_x - mean_x)

    # Plot line of best fit using calculated x and y values
    pp.plot([0, largest_x], [y1, y2])



def plot_data(data_points):
    """
    Plots a scatted plot using the given data points

    Parameters:
    data_points (type: list): A list of tuples containg x and y values

    Returns:
    None
    """
    
    # Get x and y values from data_points using separate function
    x_vals, y_vals = separate(data_points)
    
    # Plot data using x_vals and y_vals
    pp.scatter(x_vals, y_vals)


def get_data(filename):
    """
    gets x and y values, x label, and y label from a given filename

    Parameter:
    filename (type: string): The string of the filename to get data from

    Returns:
    (type: tuple): A tuple containg three items: A list of (x,y) tuples, a label for the x values, 
    and a label for the y_values
    """

    # Open file
    f = open(filename, "r")

    # Read header and set x and y labels
    header = f.readline().split(",")
    x_label = header[0]
    y_label = header[1].rstrip("\n")

    # Initialize empty list
    coords = []

    # Loop through file and add (x,y) tuples to list
    for line in f:
        split_line = line.split(",")
        coords.append((float(split_line[0]), float(split_line[1])))

    # Return tuple containing list of (x,y) tuples, x label, and y label
    return coords, x_label, y_label


def main():
    """
    Asks user for a filename, plots both the scatter plot and line of best fit,
    then updates labels on graph.
    """

    # Ask user for filename
    data_filename = input("Enter the name of the data file: ")

    # Get data from specified file
    coords, x_label, y_label = get_data(data_filename)

    # Plot scatter plot and line of best fit
    plot_data(coords)
    plot_regression(coords)

    # Update labels
    pp.xlabel(x_label)
    pp.ylabel(y_label)

    # Show graph
    pp.show()


"""
WARNING: Do NOT modify anything below this point, sp23.
"""
if __name__ == "__main__":
    main()
