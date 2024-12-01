class PriorityPreemptiveScheduling:
    def __init__(self, processes):
        self.n = len(processes)
        self.processes = processes

    def turnaround_time(self):
        total_turnaround_time = 0
        for process in self.processes:
            process["tat"] = process["ct"] - process["at"]
            total_turnaround_time += process["tat"]

        avg = total_turnaround_time / self.n
        return avg

    def waiting_time(self):
        total_waiting_time = 0
        for process in self.processes:
            process["wt"] = process["tat"] - process["bt"]
            total_waiting_time += process["wt"]
        avg = total_waiting_time / self.n
        return avg

    def cpu_usage(self):
        total_burst_time = sum(process["bt"] for process in self.processes)
        total_turnaround_time = sum(process["tat"] for process in self.processes)
        cpu_usage = (total_burst_time / total_turnaround_time) * 100
        return cpu_usage

    def completion_time(self):
        processes = sorted(self.processes, key=lambda x: x["at"])
        time = 0
        completed_processes = []
        ready_queue = []
        executed_burst_time = {
            p["pid"]: 0 for p in self.processes
        }  # To track executed burst time for each process

        while processes or ready_queue:
            while processes and processes[0]["at"] <= time:
                ready_queue.append(processes.pop(0))

            if ready_queue:
                ready_queue.sort(key=lambda x: x["priority"])
                current_process = ready_queue[0]

                if executed_burst_time[current_process["pid"]] < current_process["bt"]:
                    executed_burst_time[current_process["pid"]] += 1
                    time += 1

                    if (
                        executed_burst_time[current_process["pid"]]
                        == current_process["bt"]
                    ):
                        current_process["ct"] = time
                        completed_processes.append(current_process)
                        ready_queue.remove(current_process)

            else:
                time += 1

        self.processes = completed_processes
        return completed_processes

    def display_gantt_chart(self):
        print("\nGantt Chart:")
        for p in self.processes:
            print("+" + "-" * 5, end="")
        print("+")

        for p in self.processes:
            print(f"| {p['pid']}".ljust(6), end="")
        print("|")

        for p in self.processes:
            print("+" + "-" * 5, end="")
        print("+")

        current_time = 0
        for p in self.processes:
            print(f"{current_time}".ljust(6), end="")
            current_time = p["ct"]
        print(f"{current_time}")


if __name__ == "__main__":
    n = int(input("Number of processes: "))
    processes = []

    for i in range(n):
        process_id = chr(65 + i)
        arrival_time = int(input(f"Arrival time of Process {process_id}: "))
        burst_time = int(input(f"Burst time of Process {process_id}: "))
        priority = int(input(f"Priority of Process {process_id}: "))
        processes.append(
            {
                "pid": process_id,
                "at": arrival_time,
                "bt": burst_time,
                "priority": priority,
                "ct": 0,
                "tat": 0,
                "wt": 0,
            }
        )

    priority_scheduling = PriorityPreemptiveScheduling(processes)

    completion_time = priority_scheduling.completion_time()
    avg_tat = priority_scheduling.turnaround_time()
    avg_wt = priority_scheduling.waiting_time()
    cpu_usage = priority_scheduling.cpu_usage()
    priority_scheduling.display_gantt_chart()

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"CPU Utilization: {cpu_usage:.2f}%")
