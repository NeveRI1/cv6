from cv6 import signal_plot_ops as spo

signal = spo.load_signal_from_txt("ekg_signal.txt")

print("Average:", spo.signal_avg(signal))

spo.plot_signal(signal)
