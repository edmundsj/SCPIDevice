from SCPIDevice import SCPIDevice
import numpy as np
import pyvisa
import pytest
from numpy.testing import assert_equal, assert_allclose

@pytest.fixture
def sdg():
    print("OpeningSDG device...")
    sdg_parameters = {
        'device': SCPIDevice(),
        'id': 'Agilent Technologies,33210A,MY48005679,1.04-1.04-22-2',
    }
    yield sdg_parameters
    print("Closing SDG device...")
    sdg_parameters['device'].close()

def test_visa_init(sdg):
    """
    Check that we get back the correct ID of our device
    """
    actual_device = sdg['device'].device
    desired_type = pyvisa.resources.usb.USBInstrument
    assert_equal(type(actual_device), desired_type)

def test_identify(sdg):
    desired_name = sdg['id']
    actual_name = sdg['device'].identify()
    assert_equal(actual_name, desired_name)
