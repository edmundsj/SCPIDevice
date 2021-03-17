import pyvisa
from pyscpi import SCPIDevice, twos_to_voltage
import os
import numpy as np

class MCP3561(SCPIDevice):
    def __init__(self, lib_type='pyvisa',
            device_name='MCP3561 Dev Board v1', read_termination='\r\n', write_termination='\n', sampling_frequency=9760,
            n_samples=1, offset_voltage=1.138):
        self.lib_type = lib_type
        super().__init__(lib_type=lib_type, device_name=device_name,
                read_termination=read_termination,
                write_termination=write_termination)
        self._n_samples = n_samples
        self._n_bytes = n_samples * 3 + 1
        self._n_synchronization_pulses = 0
        self.sampling_frequency = sampling_frequency

        self._microsteps_per_nm = 30.3716*1.011 # calibrated from 800nm - 1700nm. Optimized for 5nm steps.
        self._microsteps_correction = -6.17*1e-6

        if(os.path.isfile('device_settings.txt')):
            with open('device_settings.txt', 'r') as settingsFile:
                data = json.load(settingsFile)
                self._wavelength = data['wavelength']
        else:
             self._wavelength = 1000


    """
    Check that all the parameters are what we want them to be
    """
#def verify(self):

    @property
    def n_samples(self):
        return self._n_samples

    @n_samples.setter
    def n_samples(self, n_samples):
        if self._n_samples != n_samples:
            self._n_samples = n_samples
            self._n_bytes= n_samples*3 + 1
            self.write_line('CONFIGURE ' + str(n_samples))

    def measure(self):
        old_timeout = self.device.timeout
        measurement_time = self._n_samples / self.sampling_frequency
        if(measurement_time > self.device.timeout - 0.1):
            self.device.timeout = measurement_time + 0.1

        bytes_written = self.write_line('MEASURE?')
        measured_data = self.read_bytes(self._n_bytes)

        if len(measured_data) == 0:
            raise ValueError(f"No data measured from device. Attempted to read {self._n_bytes} bytes.")
        verification_char = measured_data[0]
        if chr(verification_char) != '#':
            raise ValueError(
                f'Did not receive verification character #. Actual character is {verification_char}')

        measured_bytes = np.frombuffer(
                measured_data[1:], dtype=np.uint8)

        if measurement_time > old_timeout:
            self.device.timeout = old_timeout

        return measured_bytes

    def generateData(self, n_samples=1000, sync=True):
        """
        :param n_samples: The number of points of data to collect
        :param sync: Whether to report synchronization points from an external reference (True/False)
        :returns: data - a pandas data frame
        """
        self.n_samples = n_samples
        voltages = twos_to_voltage(self.measure()) - self.offset_voltage
        times = np.arange(0, n_samples/ self.sampling_frequency,
                          1/self.sampling_frequency)
        pi_phase_indices = twosToInteger(self.getSyncData())
        sync_column = np.zeros(n_samples, dtype=np.int)
        sync_column[pi_phase_indices] = 1 # Sync event

        data = pd.DataFrame(data={
            'Time (s)': times,
            'Voltage (mV)': voltages*1e3,
            'Sync': sync_column})

        return data

