class FCFS:
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

    def completion_time(self):
        prev = 0
        sorted_processes = sorted(self.processes, key=lambda x: x["at"])
        for index, process in enumerate(sorted_processes):
            process["ct"] = prev + process["bt"]
            if index == 0:
                process["ct"] = process["bt"]
                if process["at"] != 0:
                    process["ct"] += process["at"]
            prev = process["ct"]
        return sorted_processes

    def cpu_usage(self):
        total_burst_time = sum(process["bt"] for process in self.processes)
        total_turnaround_time = sum(process["tat"] for process in self.processes)
        cpu_usage = (total_burst_time / total_turnaround_time) * 100
        return cpu_usage

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
        processes.append(
            {
                "pid": process_id,
                "at": arrival_time,
                "bt": burst_time,
                "ct": 0,
                "tat": 0,
                "wt": 0,
            }
        )

    fcfs = FCFS(processes)

    completion_time = fcfs.completion_time()
    avg_tat = fcfs.turnaround_time()
    avg_wt = fcfs.waiting_time()
    cpu_usage = fcfs.cpu_usage()
    fcfs.display_gantt_chart()

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"CPU Utilization: {cpu_usage:.2f}%")
