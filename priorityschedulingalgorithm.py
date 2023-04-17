#priority scheduling algorithm
# Step 1: Get the number of processes, burst time, and priority
n = int(input("Enter the number of processes: "))
burst_time = []
priority = []
for i in range(n):
    burst_time.append(int(input("Enter burst time for process {}: ".format(i+1))))
    priority.append(int(input("Enter priority for process {}: ".format(i+1))))

# Step 2: Using for loop i=0 to n-1 do step 1 to 6
total_waiting_time = 0
total_turnaround_time = 0
T = [0] * n
wt = [0] * n

for i in range(n):
    # Step 3: If i=0,wait time=0,T[0]=b[0]
    if i == 0:
        wt[i] = 0
        T[i] = burst_time[i]
    else:
        # Step 4: T[i]=T[i-1]+b[i] and wt[i]=T[i]-b[i]
        T[i] = T[i-1] + burst_time[i]
        wt[i] = T[i] - burst_time[i]
    
    # Step 5: Total waiting time is calculated by adding the waiting time for each process
    total_waiting_time += wt[i]
    
    # Step 6: Total turnaround time is calculated by adding all total time of each process
    total_turnaround_time += T[i]
    
# Step 7: Calculate Average waiting time by dividing the total waiting time by total number of processes
average_waiting_time = total_waiting_time / n

# Step 8: Calculate Average turnaround time by dividing the total time by the number of processes
average_turnaround_time = total_turnaround_time / n

# Step 9: Display the result
print("Average waiting time:", average_waiting_time)
print("Average turnaround time:", average_turnaround_time)
