import pytest
import os

@pytest.fixture
def valid_inputs():

    base_dir = os.path.dirname(__file__)  # Get the directory of conftest.py
    filepath = os.path.join(base_dir, "input_data", "example_file.csv")
    out_files_dir = os.path.join(base_dir, "output_data")

    return {
        "filepath": filepath,
        "save_data": "yes",
        "start_time_user": "none",
        "header_lines": 1,
        "time_to_skip": 2.3e-06,
        "time_to_take": 1.5e-06,
        "t_before": 5e-09,
        "t_after": 5e-08,
        "start_time_correction": 0.0,
        "freq_min": 1500000000.0,
        "freq_max": 4000000000.0,
        "smoothing_window": 601,
        "smoothing_wid": 3,
        "smoothing_amp": 1,
        "smoothing_sigma": 1,
        "smoothing_mu": 0,
        "pb_neighbors": 400,
        "pb_idx_correction": 0,
        "rc_neighbors": 400,
        "rc_idx_correction": 0,
        "sample_rate": 80000000000.0,
        "nperseg": 512,
        "noverlap": 435,
        "nfft": 5120,
        "window": "hann",
        "blur_kernel": (5, 5),
        "blur_sigx": 0,
        "blur_sigy": 0,
        "carrier_band_time": 2.5e-07,
        "cmap": "viridis",
        "uncert_mult": 100,
        "order": 6,
        "wid": 50000000.0,
        "lam": 1.547461e-06,
        "C0": 4540,
        "density": 1730,
        "delta_rho": 9,
        "delta_C0": 23,
        "delta_lam": 8e-18,
        "theta": 0,
        "delta_theta": 5,
        "out_files_dir": out_files_dir,
        "display_plots": "no",
        "spall_calculation": "yes",
        "plot_figsize": (30, 10),
        "plot_dpi": 300,
    }
