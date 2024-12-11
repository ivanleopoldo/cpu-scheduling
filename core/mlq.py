import queue


class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_burst_time = burst_time
        self.completion_time = 0


def calculate_waiting_turnaround_times(processes):
    completion_time = 0
    waiting_times = []
    turnaround_times = []

    for process in processes:
        completion_time += process.burst_time
        process.completion_time = completion_time
        turnaround_time = process.completion_time - process.arrival_time
        turnaround_times.append(turnaround_time)
        waiting_time = turnaround_time - process.burst_time
        waiting_times.append(max(0, waiting_time))

    return waiting_times, turnaround_times


def run_queue(process_queue):
    while not process_queue.empty():
        current_process = process_queue.get()
        print(
            f"Running {current_process.name} in Priority {current_process.priority} Queue"
        )

        current_process.remaining_burst_time = (
            0  # Complete the remaining burst time for simplicity
        )


def display_table(processes):
    waiting_times, turnaround_times = calculate_waiting_turnaround_times(processes)

    print(
        "\nProcess\tPriority\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time"
    )
    for process in processes:
        print(
            f"{process.name}\t{process.priority}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{waiting_times[process.name - 1]}\t\t{turnaround_times[process.name - 1]}"
        )


if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        name = i + 1
        arrival_time = int(input(f"Enter arrival time for Process {name}: "))
        burst_time = int(input(f"Enter burst time for Process {name}: "))
        priority = int(
            input(f"Enter priority for Process {name} (1 for High, 2 for Low): ")
        )

        processes.append(Process(name, arrival_time, burst_time, priority))

    high_priority_queue = queue.Queue()
    low_priority_queue = queue.Queue()

    for process in processes:
        if process.priority == 1:
            high_priority_queue.put(process)
        else:
            low_priority_queue.put(process)

    run_queue(high_priority_queue)
    run_queue(low_priority_queue)

    display_table(processes)
