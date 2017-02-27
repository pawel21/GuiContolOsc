from IODevice import IODevice
import numpy as np


class RigolDS1104B:
    def __init__(self, device):
        self.dev = IODevice(device)

    def write(self, command):
        self.dev.write(command)

    def read(self, command):
        return self.dev.read(command)

    def run(self):
        self.write("RUN")

    def stop(self):
        self.write("STOP")

    def get_time_scale(self):
        self.write(":TIM:SCAL?")
        value = self.read(100)
        return float(value)

    def set_time_scale_in_second(self, value):
         self.write(":TIM:SCAL " + str(value))

    def get_scale(self, channel):
        command = "CHANnel" + str(channel) + ":SCALe?"
        self.write(command)
        value = self.read(100)
        return value

    def set_scale_in_volt(self, channel, value):
        command = "CHANnel" + str(channel) + ":SCALe " + str(value)
        self.write(command)

    def get_data(self):
        self.write(":WAVeform:FORMat ASCii")
        self.write(":WAVeform:DATA? CHANnel1")
        y = self.read(10000)
        y = (y[12:].decode()).split(',')
        voltage = np.zeros(len(y))
        for i in range(0, len(y)):
            voltage[i] = float(y[i])
        time_scale = float(self.get_time_scale())
        time = np.linspace(0, time_scale * 12, 600)
        return time, voltage
