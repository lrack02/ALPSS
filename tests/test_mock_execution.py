import pytest
from unittest.mock import patch
from alpss.alpss_main import alpss_main
import matplotlib.pyplot as plt


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
