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