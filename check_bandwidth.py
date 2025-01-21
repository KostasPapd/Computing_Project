import psutil
import time
import threading
import main

class BandwidthMonitor:
    def __init__(self):
        self.bytes_sent_start, self.bytes_recv_start = self.get_network_usage()
        self.bytes_sent_total = 0
        self.bytes_recv_total = 0
        self.start_time = time.time()
        self.running = True
        self.thread = threading.Thread(target=self.measure_bandwidth_usage)
        self.thread.start()

    def get_network_usage(self):
        net_io = psutil.net_io_counters()
        return net_io.bytes_sent, net_io.bytes_recv

    def convert_bytes(self, num):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024:
                return f"{num:.2f} {unit}"
            num /= 1024

    def measure_bandwidth_usage(self):
        while self.running:
            time.sleep(1)
            bytes_sent_end, bytes_recv_end = self.get_network_usage()
            self.bytes_sent_total = bytes_sent_end - self.bytes_sent_start
            self.bytes_recv_total = bytes_recv_end - self.bytes_recv_start

    def stop(self):
        self.running = False
        self.thread.join()
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"Total bytes sent: {self.convert_bytes(self.bytes_sent_total)}")
        print(f"Total bytes received: {self.convert_bytes(self.bytes_recv_total)}")
        print(f"Time ran for: {duration:.2f} seconds")

if __name__ == "__main__":
    monitor = BandwidthMonitor()
    try:
        main.main()
    finally:
        monitor.stop()