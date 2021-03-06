import os
import sys
file_location = os.path.dirname(os.path.abspath(__file__))
source_location = os.path.abspath(os.path.join(file_location, '..', 'source/'))

sys.path.insert(0, source_location)
from SCPIDevice import SCPIDevice

class Agilent33210A(SCPIDevice):
    def __init__(self, lib_type='pyvisa', resource_index=0):
        super().__init__(lib_type=lib_type, resource_index=resource_index)

    @property
    def frequency(self):
        freq = self.query('FREQUENCY?')
        return float(freq)

    @frequency.setter
    def frequency(self, frequency):
        self.write_line('FREQUENCY ' + str(frequency) + 'HZ')

    @property
    def amplitude(self):
        volt = self.query('VOLTAGE?')
        return float(volt)

    @amplitude.setter
    def amplitude(self, volt):
        self.write_line('VOLTAGE ' + str(volt) + 'V')

    @property
    def offset_voltage(self):
        volt = self.query('VOLTAGE:OFFSET?')
        return float(volt)

    @offset_voltage.setter
    def offset_voltage(self, volt):
        self.write_line('VOLTAGE:OFFSET ' + str(volt) + 'V')

    @property
    def output_on(self):
        return bool(int(self.query('OUTPUT?')))

    @output_on.setter
    def output_on(self, output):
        if output == True:
            output_string = 'ON'
        else:
            output_string = 'OFF'
        self.write_line('OUTPUT ' + output_string)
