import argparse

from alpss.alpss_watcher import Watcher
from alpss.alpss_main import alpss_main
import os
import json

"""
Credit to Michael Cho
https://michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
"""


def start_watcher():
    w = Watcher()
    w.run()


def load_json_config(config):
    """Load configuration from a JSON file or return directly if it's already a dictionary."""
    if isinstance(config, dict):
        return config  # If already a dictionary, return it

    if isinstance(config, str) and os.path.exists(config):
        with open(config, "r") as file:
            return json.load(file)  # Load JSON directly

    raise ValueError(
        "Invalid config input: Provide a dictionary or a valid JSON file path."
    )


def alpss_main_with_config(config=None):
    """
    Run ALPSS with a given YAML configuration.

    Args:
        config (str or dict, optional): Path to a YAML config file or a dictionary containing config parameters.
    """
    if config is None:
        # If called from CLI, parse arguments
        parser = argparse.ArgumentParser(
            description="Run ALPSS using a YAML config file"
        )
        parser.add_argument(
            "config_path", type=str, help="Path to the YAML configuration file"
        )
        args = parser.parse_args()
        config = args.config_path

    # Load the YAML config
    config_data = load_json_config(config)

    # Run ALPSS with the loaded config
    alpss_main(**config_data)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Run ALPSS using a YAML config file")
#     parser.add_argument(
#         "config_path", type=str, help="Path to the YAML configuration file"
#     )
#     args = parser.parse_args()

#     run_alpss(args.config_path)

# def run_alpss():
#     parser = argparse.ArgumentParser(description="Run ALPSS on a file")
#     parser.add_argument(
#         "filename",
#         type=str,
#         help="The name of the file to run ALPSS on",
#     )
#     args = parser.parse_args()
#     alpss_main(
#         filename=args.filename,
#         save_data="yes",
#         start_time_user="none",
#         header_lines=0,
#         time_to_skip=0e-6,
#         time_to_take=10e-6,
#         t_before=10e-9,
#         t_after=200e-9,
#         start_time_correction=0e-9,
#         freq_min=1e9,
#         freq_max=5e9,
#         smoothing_window=1001,
#         smoothing_wid=3,
#         smoothing_amp=1,
#         smoothing_sigma=1,
#         smoothing_mu=0,
#         pb_neighbors=400,
#         pb_idx_correction=0,
#         rc_neighbors=400,
#         rc_idx_correction=0,
#         sample_rate=128e9,
#         nperseg=512,
#         noverlap=435,
#         nfft=5120,
#         window="hann",
#         blur_kernel=(5, 5),
#         blur_sigx=0,
#         blur_sigy=0,
#         carrier_band_time=250e-9,
#         cmap="viridis",
#         uncert_mult=100,
#         order=6,
#         wid=15e7,
#         lam=1550.016e-9,
#         C0=4540,
#         density=1730,
#         delta_rho=9,
#         delta_C0=23,
#         delta_lam=8e-18,
#         theta=0,
#         delta_theta=5,
#         exp_data_dir="/srv/hemi01-j01/ALPSS/tests/input_data",
#         out_files_dir="/srv/hemi01-j01/ALPSS/tests/output_data2",
#         # exp_data_dir="/Users/Administrator/Desktop/PDV_DATA",
#         # out_files_dir="/Users/Administrator/Desktop/ALPSS_output/custom",
#         display_plots="yes",
#         spall_calculation="yes",
#         plot_figsize=(30, 10),
#         plot_dpi=300,
#     )
