import pytest
from pyscpi import MCP, Agilent
from numpy.testing import assert_equal

@pytest.fixture
def mcp():
    device = MCP()
    device.reset()
    yield {'device': device}
    device.reset()
    device.close()

@pytest.mark.mcp
def test_measure(mcp):
    """
    Asserts that the result of a measurement is a set of three bytes, and that no more than 3 bytes are returned
    """
    desiredMeasurements = 1
    measuredData = mcp['device'].Measure()
    assert_equal(len(measuredData), 3)
    assert_equal(mcp['device'].inWaiting(), 0) # Verify that there ore no bytes left to be read


@pytest.mark.mcp
def test_measure_byte_count(mcp):
    """
    Asserts that the Configure() function can be used to measure between 1 and 100,000 measurements without
    dropping a single byte.
    """
    desiredMeasurementsList = [1, 10, 100, 1000, 10000]

    for desiredMeasurements in desiredMeasurementsList:
        desiredBytes = desiredMeasurements * 3
        mcp['device'].Configure(desiredMeasurements)
        data = mcp['device'].Measure()
        actualBytes = len(data)
        assert_equal(actualBytes, desiredBytes,
                msg=f'Received wrong number of bytes. Actual bytes: {actualBytes}.' + \
                f'Desired bytes: {desiredBytes}' + \
                f'attempt restart of the arduino.\n')

@pytest.mark.skip
@pytest.mark.mcp
def test_measure_large_byte_count(mcp):
    """
    Asserts that we can measure very large numbers of measurements (1 million in this test) without dropping
    any bytes.
    """
    desiredMeasurements = int(500000)
    desiredBytes = desiredMeasurements * 3
    mcp['device'].Configure(desiredMeasurements)
    data = mcp['device'].Measure() # If this isn't blocking, it should probably be made blocking.
    actualBytes = len(data)
    assert_equal(actualBytes, desiredBytes,
                msg=f'Received wrong number of bytes. Actual bytes: {actualBytes}.' + \
                f'Desired bytes: {desiredBytes}' + \
                f'attempt restart of the arduino.\n')

@pytest.mark.mcp
def test_synchronization_points(mcp):
    """
    Confirm that we get the expected number of data synchronization events when we sample in a given time period.
    Assumes an external 1kHz square wave is being applied to pin 20 on the Teensy.
    """
    f_sync = 105
    desired_sync_pulses = 8
    n_samples = int(mcp['device'].sampling_frequency/f_sync * desired_sync_pulses)

    breakpoint()
    agilent = Agilent()
    agilent.frequency = f_sync
    agilent.output_on = True
    agilent.verify()

    mcp['device'].n_samples = n_samples
    mcp['device'].measure()

    actual_sync_pulses = mcp['device'].sync_points()
    agilent.output_on = False
    assert_equal(actual_sync_pulses, desired_sync_pulses, msg='Failed to synchronize to external function generator. Is it turned on?')

@pytest.mark.mcp
def test_synchronization_data(mcp):
    """
    Verify that the synchronization data we get is "reasonable" - that is that points are separated by very close
    to their expected frequency of 1kHz. This assumes there is a square wave at 1kHz sending data to the Teensy.
    """
    f_sync = 105
    desired_sync_pulses = 3
    n_samples = int(
            mcp['device'].sampling_frequency/f_sync * desired_sync_pulses)
    mcp['device'].n_samples = n_samples
    mcp['device'].measure()
    actual_sync_pulses = mcp['device'].sync_points()
    syncData = mcp['device'].sync_data()
    bytesPerDataPoint = 3
    desiredSyncBytes = bytesPerDataPoint * desired_sync_pulses

    # check that the data has the right number of bytes in it
    assert_equal(len(syncData), desiredSyncBytes)
    measurementPoints = twosToInteger(syncData)
    measurementDeltas = np.diff(measurementPoints)
    timeDeltas = 1 / mcp['device'].sampling_frequency * measurementDeltas
    approxFrequencies = np.reciprocal(timeDeltas)
    np.testing.assert_allclose(approxFrequencies[0], f_sync, atol=1e-4)
    assertAlmostEqual(approxFrequencies[1], f_sync)
