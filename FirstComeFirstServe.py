#FirstComeFirstServe
# Step 1: Create the number of processes
num_processes = int(input("Enter the number of processes: "))

# Step 2: Get the ID and Service time for each process
processes = []
for i in range(num_processes):
    pid = input("Enter process ID: ")
    service_time = int(input("Enter service time for process {}: ".format(pid)))
    processes.append({'pid': pid, 'service_time': service_time})

# Step 3: Initialize waiting time and total time for the first process
processes[0]['waiting_time'] = 0
processes[0]['total_time'] = processes[0]['service_time']

# Step 4: Calculate total time and processing time for the remaining processes
for i in range(1, num_processes):
    processes[i]['total_time'] = processes[i-1]['total_time'] + processes[i]['service_time']

# Step 5: Calculate waiting time for each process
for i in range(1, num_processes):
    processes[i]['waiting_time'] = processes[i-1]['total_time']

# Step 6: Calculate total time for each process
for i in range(num_processes):
    processes[i]['total_time'] += processes[i]['waiting_time']

# Step 7: Calculate total waiting time for all processes
total_waiting_time = sum(process['waiting_time'] for process in processes)

# Step 8: Calculate total turnaround time for all processes
total_turnaround_time = sum(process['total_time'] for process in processes)

# Step 9: Calculate average waiting time
avg_waiting_time = total_waiting_time / num_processes

# Step 10: Calculate average turnaround time
avg_turnaround_time = total_turnaround_time / num_processes

# Step 11: Display the results
print("Process\tService Time\tWaiting Time\tTotal Time")
for process in processes:
    print("{}\t{}\t\t{}\t\t{}".format(process['pid'], process['service_time'], process['waiting_time'], process['total_time']))
print("Average Waiting Time: {}".format(avg_waiting_time))
print("Average Turnaround Time: {}".format(avg_turnaround_time))
