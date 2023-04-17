#Round Robin Scheduling
def round_robin(processes, quantum):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = [p[1] for p in processes]
    current_time = 0
    done = False

    while not done:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    current_time += quantum
                    remaining_time[i] -= quantum
                else:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - processes[i][1]
                    remaining_time[i] = 0

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print("Round Robin Scheduling")
    print(f"Average waiting time: {avg_waiting_time:.2f}")
    print(f"Average turnaround time: {avg_turnaround_time:.2f}")
