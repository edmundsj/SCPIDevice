import pyvisa

class SCPIDevice:
    def __init__(self, lib_type='pyvisa', device_name='',
            read_termination='\n', write_termination='\n'):
        self.lib_type = lib_type
        if self.lib_type == 'pyvisa':
            self.get_visa_device(device_name=device_name,
                    read_termination=read_termination,
                    write_termination=write_termination)
        else:
            raise NotImplementedError

    def get_visa_device(
            self, device_name='', read_termination='\n',
            write_termination='\n'):
        """
        Initializes our device using the Visa resource manager
        """
        rm = pyvisa.ResourceManager()
        resource_list = rm.list_resources()
        if len(resource_list) == 0:
            raise RuntimeError("No resources found")
        for rname in resource_list:
            try:
                self.device = rm.open_resource(rname)
                self.read_termination = read_termination
                self.write_termination = write_termination
                device_name_actual = self.identify()
                if device_name == '':
                    break # Use the first available resource
                else:
                    if device_name == device_name_actual:
                        break # Use the resource with the desired name
            except UserWarning:
                pass

    @property
    def read_termination(self):
        return self._read_termination

    @read_termination.setter
    def read_termination(self, read_termination):
        self._read_termination = read_termination
        if self.lib_type == 'pyvisa':
            self.device.read_termination = read_termination

    @property
    def write_termination(self):
        return self._write_termination

    @write_termination.setter
    def write_termination(self, write_termination):
        self._write_termination = write_termination
        if self.lib_type == 'pyvisa':
            self.device.write_termination = write_termination


    def query(self, string):
        self.write_line(string)
        return self.read_line()

    def read_line(self):
        if self.lib_type == 'pyvisa':
            return self.device.read()

    def write_line(self, string):
        if self.lib_type == 'pyvisa':
            self.device.write(string)

    def read_bytes(self, n_bytes):
        if self.lib_type == 'pyvisa':
            return self.device.read_bytes(n_bytes)

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
