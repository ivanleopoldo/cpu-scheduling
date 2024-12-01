class RoundRobin:
    def __init__(self, processes, quantum):
        self.n = len(processes)
        self.processes = processes
        self.quantum = quantum

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
        queue = []
        time = 0
        completed_processes = []
        executed_burst_time = {p["pid"]: 0 for p in self.processes}

        while any(p["bt"] > 0 for p in self.processes):
            for process in processes:
                if process["at"] <= time and process["bt"] > 0 and process not in queue:
                    queue.append(process)

            if queue:
                current_process = queue.pop(0)
                if current_process["bt"] > self.quantum:
                    time += self.quantum
                    current_process["bt"] -= self.quantum
                    queue.append(
                        current_process
                    )  # Put the process back to the queue if it's not done
                else:
                    time += current_process["bt"]
                    current_process["ct"] = time
                    current_process["bt"] = 0
                    completed_processes.append(current_process)

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
    quantum = int(input("Enter the time quantum: "))
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

    rr = RoundRobin(processes, quantum)

    completion_time = rr.completion_time()
    avg_tat = rr.turnaround_time()
    avg_wt = rr.waiting_time()
    cpu_usage = rr.cpu_usage()
    rr.display_gantt_chart()

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"CPU Utilization: {cpu_usage:.2f}%")

