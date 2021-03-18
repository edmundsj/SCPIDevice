from pyscpi import Agilent
import numpy as np
import pyvisa
import pytest
import pint
from numpy.testing import assert_equal, assert_allclose

@pytest.fixture
def agilent():
    print("Opening Agilent 33210A device...")
    agilent_parameters = {
        'device': Agilent(),
        'id': 'Agilent Technologies,33210A,MY48005679,1.04-1.04-22-2',
    }
    yield agilent_parameters
    print("Closing Agilent33210A device...")
    agilent_parameters['device'].reset()
    agilent_parameters['device'].close()

@pytest.mark.agilent
def test_visa_init(agilent):
    """
    Check that we get back the correct ID of our device
    """
    actual_device = agilent['device'].device
    desired_type = pyvisa.resources.usb.USBInstrument
    assert_equal(type(actual_device), desired_type)

@pytest.mark.agilent
def test_identify(agilent):
    desired_name = agilent['id']
    actual_name = agilent['device'].identify()
    assert_equal(actual_name, desired_name)

@pytest.mark.agilent
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

@pytest.mark.agilent
def test_set_amplitude(agilent):
    desired_voltage = 0.5
    agilent['device'].amplitude= desired_voltage
    actual_voltage = agilent['device'].amplitude
    assert_equal(actual_voltage, desired_voltage)

@pytest.mark.agilent
def test_set_frequency(agilent):
    desired_frequency = 100
    agilent['device'].frequency = desired_frequency
    actual_frequency = agilent['device'].frequency
    assert_equal(actual_frequency, desired_frequency)

@pytest.mark.agilent
def test_set_output(agilent):
    output_desired = True
    agilent['device'].output_on = True
    output_actual = agilent['device'].output_on
    assert_equal(output_actual, output_desired)

    output_desired = False
    agilent['device'].output_on = False
    output_actual = agilent['device'].output_on
    assert_equal(output_actual, output_desired)

@pytest.mark.agilent
def test_offset(agilent):
    offset_desired = 0.1
    agilent['device'].offset_voltage = offset_desired
    offset_actual = agilent['device'].offset_voltage
    assert_equal(offset_actual, offset_desired)

@pytest.mark.agilent
def test_verify_correct(agilent):
    agilent['device'].verify()

@pytest.mark.agilent
def test_verify_incorrect_amplitude(agilent):
    agilent['device']._amplitude = 500 # This is just wrong
    with pytest.raises(AssertionError):
        agilent['device'].verify()

@pytest.mark.agilent
def test_verify_incorrect_frequency(agilent):
    agilent['device']._frequency = 99 # This is just wrong
    with pytest.raises(AssertionError):
        agilent['device'].verify()

@pytest.mark.agilent
def test_verify_incorrect_offset(agilent):
    agilent['device']._offset_voltage = 0.2 # This is just wrong
    with pytest.raises(AssertionError):
        agilent['device'].verify()

@pytest.mark.agilent
def test_verify_incorrect_output(agilent):
    agilent['device']._output_on = True # This is just wrong
    with pytest.raises(AssertionError):
        agilent['device'].verify()

