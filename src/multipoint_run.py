import pandas as pd
from alpss_main import alpss_main

ch1 = pd.DataFrame([[1550.000,1550.016,10]], columns = ["tar_lam","ref_lam","probe_number"])
ch2 = pd.DataFrame([[1531.116,1531.140,6],[1537.397,1537.453,9],[1543.730,1543.810,15]], columns = ["tar_lam","ref_lam","probe_number"])
ch3 = pd.DataFrame([[1531.236,1531.316,3],[1537.549,1537.605,8],[1543.906,1543.930,19]], columns = ["tar_lam","ref_lam","probe_number"])

# ch1 = pd.DataFrame([[1550.000,1550.016,10]], columns = ["tar_lam","ref_lam","probe_number"])
# ch2 = pd.DataFrame([[1531.116,1531.140,6],[1537.397,1537.453,9]], columns = ["tar_lam","ref_lam","probe_number"])
# ch3 = pd.DataFrame([[1531.236,1531.316,3],[1537.549,1537.605,8],[1543.906,1543.930,19],[1550.116,1550.26,19]], columns = ["tar_lam","ref_lam","probe_number"])

# channels = {'ch1': ch1, 'ch2': ch2, 'ch3': ch3}
channels = {'ch3': ch3}
for name, channel in channels.items():
    for probe in range(len(channel)):
        ref_lam = channel["ref_lam"][probe]
        tar_lam = channel["tar_lam"][probe]
        probe_number = channel["probe_number"][probe]

        upshift = 3E8 / tar_lam - 3E8 / ref_lam #beat frequency offset in GHz
        freq_min = upshift - 1.5
        freq_max = upshift + 1

        alpss_main(
            filepath=r"C:\Users\lucas\OneDrive - Johns Hopkins\Ramesh Lab - Research\Papers\MPDV\pdv_data\input_data\Multi_PDV_test--20260311--00023_"+name+".csv",
            multipoint_probe = probe_number,
            save_data="yes",
            start_time_user='cusum', #cusum, explicit start time, or none
            header_lines=0,
            time_to_skip=0.01e-6,
            time_to_take=3e-6,
            t_before=100e-9,
            t_after=500e-9,
            start_time_correction=0e-9,
            freq_min=freq_min * 1e9,
            freq_max=freq_max * 1e9,
            smoothing_window=1001,
            smoothing_wid=3,
            smoothing_amp=1,
            smoothing_sigma=1,
            smoothing_mu=0,
            pb_neighbors=400,
            pb_idx_correction=0,
            rc_neighbors=400,
            rc_idx_correction=0,
            sample_rate=128e9,
            nperseg=600,
            noverlap=500,
            nfft=5120,
            window="hann",
            blur_kernel=(5, 5),
            blur_sigx=0,
            blur_sigy=0,
            carrier_band_time=500e-9,
            cusum_offset=10,
            cusum_threshold=1000,
            cmap="viridis",
            uncert_mult=8,
            carrier_filter_type='sin_fit_subtract',  #sin_fit_subtract, gaussian_notch, or none
            t_fit_begin=200e-9,
            t_fit_end=500e-9,
            order=6,
            wid=0.1e9,
            lam=ref_lam*1e-9,
            C0=10740,    
            density=3987,
            delta_rho=10,
            delta_C0=23,
            delta_lam=8e-18,
            theta=0,
            delta_theta=5,
            out_files_dir=(r"C:\Users\lucas\OneDrive - Johns Hopkins\Ramesh Lab - Research\Papers\MPDV\pdv_data\output_data"),
            display_plots="yes",
            spall_calculation="no",
            plot_figsize=(30, 10),
            plot_dpi=100,
        )