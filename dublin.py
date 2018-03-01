# import numpy


class Car:
    def __init__(self):
        self.row = 0
        self.column = 0

    def change_pos(self, x, y):
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


with open('b_should_be_easy.in') as easy:
    data_lines = []
    for line in easy:
        data_lines.append(line.split())


rows = int(data_lines[0][0])
columns = int(data_lines[0][1])
vehicles = int(data_lines[0][2])
rides = int(data_lines[0][3])
bonus = int(data_lines[0][4])
steps = int(data_lines[0][5])

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


rides_array = []

for i in range(rides):
    rides_array.append(Ride(start_rows[i], start_columns[i],
                            end_rows[i], end_columns[i],
                            earliest_starts[i], latest_finishes[i]))

cars = []

for i in range(vehicles):
    cars.append(Car())


print(rides_array[0].latest_finish)