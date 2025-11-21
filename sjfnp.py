class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        self.start_time = -1
        self.finish_time = 0
        self.remaining_time = burst_time

        self.waiting_time = 0
        self.turnaround_time = 0


def run_sjf(process_list):
    # Copy proses agar aman
    processes = [Process(p["pid"], p["arrival_time"], p["burst_time"]) for p in process_list]

    current_time = 0
    completed = 0
    gantt_chart = []
    completed_processes = []

    while completed < len(processes):

        # Ambil proses yang sudah datang & belum selesai
        ready = [p for p in processes if p.arrival_time <= current_time and p.finish_time == 0]

        # Bila tidak ada proses → IDLE
        if len(ready) == 0:
            next_arrival = min([p.arrival_time for p in processes if p.finish_time == 0])
            gantt_chart.append(("IDLE", current_time, next_arrival))
            current_time = next_arrival
            continue

        # Pilih proses dengan burst paling kecil (SJF)
        ready.sort(key=lambda p: p.burst_time)
        p = ready[0]

        # Eksekusi
        p.start_time = current_time
        p.finish_time = current_time + p.burst_time
        gantt_chart.append((p.pid, current_time, p.finish_time))
        current_time = p.finish_time

        # Hitung WT & TAT
        p.turnaround_time = p.finish_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        completed_processes.append(p)
        completed += 1

    return gantt_chart, completed_processes
