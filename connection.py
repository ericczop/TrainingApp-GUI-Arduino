import serial

class Connection:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serialInst = None
        self.data_providing = True

    def open(self):
        try:
            self.serialInst = serial.Serial(port=self.port, baudrate=self.baudrate)
            return True
        except serial.SerialException:
            print(f"Cannot open port {self.port}. Make sure Arduino is connected.")
            return False

    def read_data(self):
        data_list = []
        self.data_providing = True
        try:
            while self.data_providing:
                if self.serialInst and self.serialInst.is_open and self.serialInst.in_waiting:
                    packet = self.serialInst.readline().decode('utf').rstrip('\r\n')
                    data_list.extend(packet.split())
                    print(data_list)
        except KeyboardInterrupt:
            pass
        return [int(x) for x in data_list]

    def stop_providing(self):
        self.data_providing = False

    def close(self):
        if self.serialInst:
            self.serialInst.close()
