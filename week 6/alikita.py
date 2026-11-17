# import os
#
#
# def cwd(): #defines cwd as a function
#     path = os.getcwd()
#     print("Current working directory: {path}" )
#     print(f"The directory contains the following files:")
#     for file in os.listdir(path):
#         print(file)
#
# def run():
#     print("processing. . .  ")
#     cwd()
#
# if __name__ == "__main__":
#     run()
from matplotlib import pyplot as plt


# def observed():
#     observations = {"car", "Sky Scraper", "Sky scraper", "Bike", "House"}
#     return observations
#
# def run_task1():
#     print(observed())
#
# run_task1()

# def observed():
#     observations = []
#
#     for count in range(7):
#         print ("Please enter an observation")
#         observations.append(input())
#
#     return observations
#
# def run_task2():
#     print("Counting observations...")
#     observations = observed()
#
#     observations_set = set()
#     for observation in observations:
#         data = (observation, observations.count(observation))
#         observations_set.add(data)
#
#     for data in observations_set:
#         print(f"{data[0]} observed {data[1]}")
#
# run_task2()

# def observed():
#     observations = []
#
#     for count in range(5):
#         print("Please enter an observation:")
#         observations.append(input())
#
#     return observations
#
# def remove_observations(observations):
#     is_running = True
#
#     while (is_running):
#         print("Do you wish to remove an observation (yes/no)?")
#         response = input()
#
#         if response == "yes":
#             print("PLease enter the observation you wish to remove:")
#             observation = input()
#             observations.remove(observation)
#
#         else:
#             is_running = False
#
# def run_task3():
#     observations = observed()
#     remove_observations(observations)
#
#     observations_set = set()
#     for observation in observations:
#         data = (observation, observations.count(observation))
#         observations_set.add(data)
#
#     for data in sorted(observations_set):
#         print(f"{data[0]} observed {data[1]} times.")
#
# run_task3()

# import matplotlib.pyplot as plt
#
# x = [0, 5, 10]
#
# y = [0, 50, 100]
#
# plt.plot(x, y)
# plt.show()

# def Run_Task1():
#     x_values = [1, 2, 3, 4, 5]
#     y_values = [1, 4, 9, 16, 25]
#     display_line(x_values, y_values)
#
# def display_line(x, y):
#     plt.plot(x, y)
#     plt.xlabel('x values')
#     plt.ylabel('y values')
#     plt.show()
#
# Run_Task1()

import matplotlib.pyplot as plt

def coordinate():
    print("Please enter an x value:")
    x=int(input())
    print("Please enter an y value:")
    y=int(input())

    return x,y

def path():
    print("Retreiving path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return x_values, y_values

def run_task1():
    values = path()
    plt.plot(values[0],values[1],  "r--o")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()

run_task1()