import pyvisa
import serial

class SCPIDevice:
    def __init__(self, lib_type='pyvisa', resource_index=0):
        self.lib_type = lib_type
        if lib_type == 'pyvisa':
            self.device = self.get_visa_device(resource_index=resource_index)
        else:
            raise NotImplementedError

    def get_visa_device(self, resource_index=0):
        """
        Initializes our device using the Visa resource manager
        """
        rm = pyvisa.ResourceManager()
        resource_list = rm.list_resources()
        if len(resource_list) == 0: raise RuntimeError("No resources found")
        if len(resource_list) > 1:
            print("Multiple resources found")
            for i in range(len(resource_list)):
                print(f'{i}: {resource_list[i]}')
                print(f'Defaulting to {i}: {resource_index}. Pass different ' + \
                  'resource_index if desired')
        device = rm.open_resource(resource_list[resource_index])
        device.read_termination = '\n'
        return device

    def read_line(self):
        if self.lib_type == 'pyvisa':
            return self.device.read()

    def write_line(self, string):
        if self.lib_type == 'pyvisa':
            self.device.write(string)

    def query(self, string):
        self.write_line(string)
        return self.read_line()

    def close(self):
        self.device.close()

    def identify(self):
        self.write_line('*IDN?')
        return self.read_line()

    def reset(self):
        self.write_line('*RST')
