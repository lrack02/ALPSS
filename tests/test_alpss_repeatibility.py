import pytest
from alpss.alpss_main import alpss_main


def test_alpss_main_output(valid_inputs):
    # Call the function with valid inputs
    results = alpss_main(**valid_inputs)

    # Expected values from the CSV data (ignoring date, time, filename, and runtime)
    expected_values = {
        "Velocity at Max Compression": 828.0849443007512,
        "Time at Max Compression": 6.300750500023988e-07,
        "Velocity at Max Tension": 464.46467142515036,
        "Time at Max Tension": 6.476500600052781e-07,
        "Velocity at Recompression": 574.0505816377753,
        "Time at Recompression": 6.557375600013682e-07,
        "Carrier Frequency": 2232111412.128054,
        "Spall Strength": 1427973173.609772,
        "Spall Strength Uncertainty": 10692214.866814513,
        "Strain Rate": 2278592.4760455955,
        "Strain Rate Uncertainty": 537339.1422056587,
        "Peak Shock Stress": 3251972384.76348,
        "Spect Time Res": 9.625000834177745e-10,
        "Spect Freq Res": 15624998.645815466,
        "Spect Velocity Res": 12.089538014726124,
        "Signal Start Time": 6.140750532205402e-07,
        "Smoothing Characteristic Time": 2.9298752539258723e-09,
    }

    # Extract the results dictionary (results[1] should be the output dictionary)
    result_dict = results[1]

    # Iterate over the expected values and assert that the results match
    for key, expected_value in expected_values.items():
        assert key in result_dict, f"Key '{key}' not found in the results."
        assert result_dict[key] == pytest.approx(
            expected_value, abs=1
        ), f"Mismatch for '{key}': expected {expected_value}, got {result_dict[key]}"
