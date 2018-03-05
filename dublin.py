# import numpy


class Car:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.is_driving = False
        self.driving_steps_left = 0
        self.ride_idxs = []

    def get_loc(self):
        return self.row, self.column

    def change_loc(self, x, y):
        self.row = x
        self.column = y


class Ride:
    def __init__(self, start_row, start_column, end_row, end_column,
                 earliest_start, latest_finish):
        self.start_row = start_row
        self.start_column = start_column
        self.end_row = end_row
        self.end_column = end_column
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

    def get_start_loc(self):
        return self.start_row, self.start_column

    def get_end_loc(self):
        return self.end_row, self.end_column

    def ride_duration(self):
        return count_distance(self.get_start_loc(), self.get_end_loc())

    def max_ride_duration(self):
        return self.latest_finish - self.earliest_start


# function that returns the distance between two intersections
def count_distance(a, b):
    return sum(tuple(abs(x - y) for x, y in zip(a, b)))


# extracting data from the input file
with open('a_example.in', 'r') as input_file:
    data_lines = []
    for line in input_file:
        data_lines.append(line.split())

rows_count = int(data_lines[0][0])
columns_count = int(data_lines[0][1])
vehicles_count = int(data_lines[0][2])
rides_count = int(data_lines[0][3])
bonus = int(data_lines[0][4])
steps_count = int(data_lines[0][5])

start_rows = []
start_columns = []
end_rows = []
end_columns = []
earliest_starts = []
latest_finishes = []

for line in data_lines[1:]:
    start_rows.append(int(line[0]))
    start_columns.append(int(line[1]))
    end_rows.append(int(line[2]))
    end_columns.append(int(line[3]))
    earliest_starts.append(int(line[4]))
    latest_finishes.append(int(line[5]))

# initializing rides array
rides = []

for i in range(rides_count):
    rides.append(Ride(start_rows[i], start_columns[i],
                      end_rows[i], end_columns[i],
                      earliest_starts[i], latest_finishes[i]))

# initializing cars array
cars = []

for i in range(vehicles_count):
    cars.append(Car())

# simulation loop
with open('out.txt', 'a') as output_file:
    for i in range(0, steps_count):
        for j in range(0, vehicles_count):
            for k in range(0, rides_count):
                pass
