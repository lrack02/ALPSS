import pytest
from unittest.mock import patch
from alpss.alpss_main import alpss_main
import matplotlib.pyplot as plt


# Mocking the inputs dictionary and the required functions
@pytest.fixture
def valid_inputs():
    return {
        "filepath": "input_data/example_file.csv",
        "save_data": "yes",
        "start_time_user": "none",
        "header_lines": 0,
        "time_to_skip": 0e-6,
        "time_to_take": 10e-6,
        "t_before": 10e-9,
        "t_after": 200e-9,
        "start_time_correction": 0e-9,
        "freq_min": 1e9,
        "freq_max": 5e9,
        "smoothing_window": 1001,
        "smoothing_wid": 3,
        "smoothing_amp": 1,
        "smoothing_sigma": 1,
        "smoothing_mu": 0,
        "pb_neighbors": 400,
        "pb_idx_correction": 0,
        "rc_neighbors": 400,
        "rc_idx_correction": 0,
        "sample_rate": 128e9,
        "nperseg": 512,
        "noverlap": 435,
        "nfft": 5120,
        "window": "hann",
        "blur_kernel": (5, 5),
        "blur_sigx": 0,
        "blur_sigy": 0,
        "carrier_band_time": 250e-9,
        "cmap": "viridis",
        "uncert_mult": 100,
        "order": 6,
        "wid": 15e7,
        "lam": 1550.016e-9,
        "C0": 4540,
        "density": 1730,
        "delta_rho": 9,
        "delta_C0": 23,
        "delta_lam": 8e-18,
        "theta": 0,
        "delta_theta": 5,
        "out_files_dir": "output_data/",
        "display_plots": "no",  # Overwritten from the original value
        "spall_calculation": "yes",
        "plot_figsize": (30, 10),
        "plot_dpi": 300,
    }


# Test for valid inputs and outputs, assuming the function runs correctly
def test_alpss_main_success(valid_inputs):
    with patch("alpss.alpss_main.spall_doi_finder") as mock_spall_doi_finder, patch(
        "alpss.alpss_main.carrier_frequency"
    ) as mock_carrier_frequency, patch(
        "alpss.alpss_main.carrier_filter"
    ) as mock_carrier_filter, patch(
        "alpss.alpss_main.velocity_calculation"
    ) as mock_velocity_calculation, patch(
        "alpss.alpss_main.instantaneous_uncertainty_analysis"
    ) as mock_iua, patch(
        "alpss.alpss_main.spall_analysis"
    ) as mock_spall_analysis, patch(
        "alpss.alpss_main.full_uncertainty_analysis"
    ) as mock_fua, patch(
        "alpss.alpss_main.plot_results"
    ) as mock_plotting, patch(
        "alpss.alpss_main.save"
    ) as mock_saving:

        mock_plotting.return_value = plt.Figure()
        mock_saving.return_value = dict()

        # Call the function
        result = alpss_main(**valid_inputs)

        assert isinstance(result[0], plt.Figure)
        assert isinstance(result[1], dict)

        mock_spall_doi_finder.assert_called_once()
        mock_carrier_frequency.assert_called_once()
        mock_carrier_filter.assert_called_once()
        mock_velocity_calculation.assert_called_once()
        mock_iua.assert_called_once()
        mock_spall_analysis.assert_called_once()
        mock_fua.assert_called_once()
        mock_plotting.assert_called_once()
        mock_saving.assert_called_once()
