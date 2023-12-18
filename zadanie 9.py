import csv
import requests
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

#Wczytywanie pliku
url = 'https://raw.githubusercontent.com/uzh-rpg/agile_autonomy/958c0d22e11d28a4d73b627029cf62ef1a1a95ab/data_generation/viz_utils/pole_avoidance/reference_trajectory.csv'
response = requests.get(url)
content = response.text
string_io = StringIO(content)
reader = csv.reader(string_io)

# Pomijaj pierwszy wiersz
next(reader)

# Listyyyyyyyyyy
time_start_list = []
pos_x_list = []
pos_y_list = []
pos_z_list = []
velocities = []

# Ustawienie kolumn, list
for line in reader:
    time_start = line[0]
    pos_x = float(line[1])
    pos_y = float(line[2])
    pos_z = float(line[3])
    vel_x = float(line[4])
    vel_y = float(line[5])
    vel_z = float(line[6])

    time_start_list.append(time_start)
    pos_x_list.append(pos_x)
    pos_y_list.append(pos_y)
    pos_z_list.append(pos_z)

    # Szybkość, Nie wiem czy dobrze???????????????
    speed = np.linalg.norm([vel_x, vel_y, vel_z])
    velocities.append(speed)

# Zapis danych do pliku csv
with open("velocity.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time Start", "Speed"])  # Nagłówki kolumn

    for time_start, speed in zip(time_start_list, velocities):
        writer.writerow([time_start, speed])

# Listy do numpy
pos_x_array = np.array(pos_x_list)
pos_y_array = np.array(pos_y_list)
pos_z_array = np.array(pos_z_list)

# średnie pozycje
mean_pos_x = np.mean(pos_x_array)
mean_pos_y = np.mean(pos_y_array)
mean_pos_z = np.mean(pos_z_array)

#  wyniki na konsole
print(f"Średnia pozycja w osi X: {mean_pos_x}")
print(f"Średnia pozycja w osi Y: {mean_pos_y}")
print(f"Średnia pozycja w osi Z: {mean_pos_z}")

# Tworzenie wykresów
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

# Wykres 1
axs[0].plot(time_start_list, pos_x_list, color='blue')
axs[0].set_ylabel('Pos X')
axs[0].set_title('Wykresy w zależności od Time Start')

# Wykres 2
axs[1].plot(time_start_list, pos_y_list, color='red')
axs[1].set_ylabel('Pos Y')

# Wykres 3
axs[2].plot(time_start_list, pos_z_list, color='green')
axs[2].set_xlabel('Time Start')
axs[2].set_ylabel('Pos Z')

# Dodanie timestampów na osi x dla ostatniego wykresu
axs[2].set_xticks(time_start_list[::10])
axs[2].set_xticklabels(time_start_list[::10], rotation=45, ha="right")

plt.show()






