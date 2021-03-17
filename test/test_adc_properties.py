import pytest
import numpy as np
from pyscpi import MCP, twos_to_voltage
import matplotlib.pyplot as plt

def mcp():
    device = MCP()
    device.reset()

    yield {'device': device}

    device.reset()
    device.close()

def testNoiseSpectralDensity(mcp):
    """
    Check that the noise spectral density of our ADC is less than some desired threshold far away
    from the location of our signal (assumed here at 1kHz)
    """
    # First, disable the motor so that the associated noise (hopefully) goes away
    mcp['device'].motorEnable = False

    desiredMeasurements = 10000
    halfMeasurements = int(desiredMeasurements/2)
    samplingFrequency = 4.68 # kHz
    frequencies = np.arange(0, samplingFrequency/2, samplingFrequency/desiredMeasurements)

    signalFrequency = 1 # kHz
    startNoiseFrequency = signalFrequency * 2
    stopNoiseFrequency = samplingFrequency/2
    noiseBandwidth = (stopNoiseFrequency - startNoiseFrequency)
    startNoiseBin = int(startNoiseFrequency / samplingFrequency * desiredMeasurements)

    mcp['device'].Configure(desiredMeasurements)
    data = mcp['device'].Measure()
    times = np.arange(0, desiredMeasurements / samplingFrequency, 1/samplingFrequency)
    voltages = twos_to_voltage(data)
    dcOffset = np.mean(voltages)
    voltages -= dcOffset

    # The single-sided voltage spectral power (rms, by definition)
    voltageSpectralPower = np.square(np.abs(np.fft.fft(voltages/len(voltages))))[0:halfMeasurements]*2

    voltageNoiseRMS = np.sqrt(np.sum(voltageSpectralPower[startNoiseBin:]) )
    voltageNoisePSD = 1e9 * voltageNoiseRMS / np.sqrt(noiseBandwidth * 1e3) # in nV / rtHz

    noiseUpperBound = 400 # Differential converter: 120-150, TIA: 250, total ~300. 
    print(f'Noise PSD: {voltageNoisePSD}')
    self.assertLess(voltageNoisePSD, noiseUpperBound, msg=f'Noise PSD is {voltageNoisePSD} nV/rtHz, expected < {noiseUpperBound}nV/rtHz. RMS Integrated noise is {voltageNoiseRMS*1e6} uV')
