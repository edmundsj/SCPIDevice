from Agilent33210A import Agilent33210A
import numpy as np
import pyvisa
import pytest
from numpy.testing import assert_equal, assert_allclose

@pytest.fixture
def agilent():
    print("Opening Agilent 33210A device...")
    agilent_parameters = {
        'device': Agilent33210A(),
        'id': 'Agilent Technologies,33210A,MY48005679,1.04-1.04-22-2',
    }
    yield agilent_parameters
    print("Closing Agilent33210A device...")
    agilent_parameters['device'].reset()
    agilent_parameters['device'].close()

def test_visa_init(agilent):
    """
    Check that we get back the correct ID of our device
    """
    actual_device = agilent['device'].device
    desired_type = pyvisa.resources.usb.USBInstrument
    assert_equal(type(actual_device), desired_type)

def test_identify(agilent):
    desired_name = agilent['id']
    actual_name = agilent['device'].identify()
    assert_equal(actual_name, desired_name)

def test_reset(agilent):
    desired_frequency = 1000
    desired_amplitude = 0.1
    desired_offset = 0
    agilent['device'].reset()
    actual_frequency = agilent['device'].frequency
    actual_voltage = agilent['device'].amplitude
    actual_output = agilent['device'].output_on
    actual_offset = agilent['device'].offset_voltage

    assert_equal(actual_voltage, desired_amplitude)
    assert_equal(actual_frequency, desired_frequency)
    assert_equal(actual_output, False)
    assert_equal(actual_offset, desired_offset)

def test_set_voltage(agilent):
    desired_voltage = 0.5
    agilent['device'].amplitude= desired_voltage
    actual_voltage = agilent['device'].amplitude
    breakpoint()
    assert_equal(actual_voltage, desired_voltage)

def test_set_frequency(agilent):
    desired_frequency = 100
    agilent['device'].frequency = desired_frequency
    actual_frequency = agilent['device'].frequency
    assert_equal(actual_frequency, desired_frequency)

def test_set_output(agilent):
    output_desired = True
    agilent['device'].output_on = True
    output_actual = agilent['device'].output_on
    assert_equal(output_actual, output_desired)

    output_desired = False
    agilent['device'].output_on = False
    output_actual = agilent['device'].output_on
    assert_equal(output_actual, output_desired)

def test_offset(agilent):
    offset_desired = 0.1
    agilent['device'].offset_voltage = offset_desired
    offset_actual = agilent['device'].offset_voltage
    assert_equal(offset_actual, offset_desired)

def test_verify(agilent):
    agilent['device'].verify()
