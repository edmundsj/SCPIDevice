from pyscpi import twos_to_integer, twos_to_voltage, count_to_voltage
import pytest

def testTwosToInteger(self):
    """
    Check that this function converts a set of three bytes in twos complement to a signed integer. Checks
    two 3-byte arrays and one 6-byte array.
    """
    testBytes = np.array([255, 255, 255]) # check for proper sign conversion
    desiredInteger = -1
    actualInteger = twosToInteger(testBytes)
    self.assertEqual(desiredInteger, actualInteger)

    testBytes = np.array([100, 255, 255])
    desiredInteger = 6619135
    actualInteger = twosToInteger(testBytes)
    self.assertEqual(desiredInteger, actualInteger)

    testBytes = np.array([255, 255, 255, 100, 255, 255])
    desiredIntegers = np.array([-1, 6619135])
    actualIntegers = twosToInteger(testBytes)
    assert_allclose(desiredIntegers, actualIntegers, atol=1e-5)


def testCountToVoltage(self):
    """
    Test converting a raw ADC count into a voltage
    """
    desiredValue = 5.0
    actualCount = pow(2, 23)
    actualValue = countToVoltage(actualCount, maxVoltage=5)
    assert_allclose(desiredValue, actualValue)

def testTwosToVoltage(self):
    desiredVoltage = np.array([5.0])
    testBytes = np.array([127, 255, 255])
    actualVoltage = twosToVoltage(testBytes, maxVoltage=5, differential=True)
    assert_allclose(desiredVoltage, actualVoltage, atol=1e-5)
