__author__ = 'parallels'
with open("temp-time", "r") as infile:
    timeline = infile.read().split("\n")

for line in timeline:
    if "User time (seconds):" in line:
        time_info = line.replace("User time (seconds):", "")

with open("time_info", "a") as outfile:
    outfile.write(time_info)
