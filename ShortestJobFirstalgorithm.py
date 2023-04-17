#Shortest Job First algorithm
# Step 1: Get the number of processes
n = int(input("Enter the number of processes: "))

# Step 2: Get the id and service time for each process
processes = []
for i in range(n):
    pid = input("Enter process ID: ")
    bt = int(input("Enter process service time: "))
    processes.append((pid, bt))

# Step 3: Initially the waiting time of first short process as 0 and total time of first short is process the service time of that process.
total_time = processes[0][1]
wt = 0
avg_wt = 0
avg_tat = 0

# Step 4: Calculate the total time and waiting time of remaining process.
for i in range(1, n):
    # Sort processes by service time
    processes.sort(key=lambda x: x[1])

    # Calculate waiting time for current process
    wt = total_time

    # Update total time and waiting time
    total_time += processes[i][1]
    avg_wt += wt
    avg_tat += total_time

# Step 9: Calculate average waiting time by dividing the total waiting time by total number of processes.
avg_wt /= n

# Step 10: Calculate average turnaround time by dividing the total waiting time by total number of process.
avg_tat /= n

# Step 11: Display the result
print("Average Waiting Time:", avg_wt)
print("Average Turnaround Time:", avg_tat)
