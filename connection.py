import serial
import time


class Connection:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serialInst = None

    def open(self):
        try:
            self.serialInst = serial.Serial(port=self.port, baudrate=self.baudrate)
            return True
        except serial.SerialException:
            print(f"Cannot open port {self.port}. Make sure Arduino is connected.")
            return False

    def read_data(self, run_time):
        data_list = []
        try:
            start_time = time.time()

            while time.time() - start_time < run_time:
                if self.serialInst and self.serialInst.is_open and self.serialInst.in_waiting:
                    packet = self.serialInst.readline().decode('utf').rstrip('\r\n')
                    data_list.extend(packet.split())
                    print(data_list)
        except KeyboardInterrupt:
            pass
        return [int(x) for x in data_list]

    def close(self):
        if self.serialInst:
            self.serialInst.close()
