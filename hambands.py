'''
Based on C code written by Mike Markowski AB3AP
'''

#!/usr/bin/python3

import argparse
from decimal import *

parser = argparse.ArgumentParser(
		description='Simple calculations of half wavelengths of ham bands')
parser.add_argument("-m", "--multiples", type=float, default=5,
		help="The number of multiples to calculate. 5 is the default.")
args = parser.parse_args()

# Ranges of half wavelengths for each ham band
HALFWAVES = [
(1800.0, 2000.0),	# 160m
(3500.0, 4000.0),	# 80m
(5330.5, 5405.0),	# 40m
(7000.0, 7300.0),	# 40m
(10100.0, 10150.0),	# 30m
(14000.0, 14350.0),	# 20m
(18068.0, 14350.0),	# 17m
(21000.0, 21450.0),	# 15m
(24890.0, 24990.0),	# 12m
(28000.0, 29700.0),	# 10m
(50000.0, 54000.0),	# 6m
]

'''
For a given frequency range, calculate the half wavelength range and print
it.  In addition, print up to 4th multiples of each range up to the length
of 160m half wavelength.

Comments are also printed out assuming that the output will saved to a file
which will be used by gnuplot.
'''
def rw(min_kHz, max_kHz):
	lo_freq_MHz = 1.8
	# Max wavelength in band
	lambda_max_ft = 2 * 468 / lo_freq_MHz

	print("# {:.3f} to {:.3f} kHz, too short for {:.3f} MHz"
	.format(min_kHz, max_kHz, lo_freq_MHz))

	qtr_ft = 468 / lo_freq_MHz / 2

	print("{:.3f} 0\n{:.3f} 1\n{:.3f} 1\n{:.3f} 0\n"
	.format(0.0, 0 + (1e-3), qtr_ft, qtr_ft + (1e-3)))

	count = 1

	while True:
		lambda0_ft = count * 468 / (max_kHz * 1e-3)
		lambda1_ft = count * 468 / (min_kHz * 1e-3)

		print("# {:.3f} to {:.3f} kHz, multiple {:}"
		.format(min_kHz, max_kHz, count))

		print("{:.3f} 0\n{:.3f} 1\n{:.3f} 1\n{:.3f} 0\n"
		.format(lambda0_ft - (1e-3), lambda0_ft,
				lambda1_ft - (1e-3), lambda1_ft + (1e-3)))

		# Prepare for the next multiple
		count += 1

		if (lambda1_ft > lambda_max_ft) or (count >= args.multiples):
			break

'''
Our main loop
'''
for halfwave in HALFWAVES:
	rw(halfwave[0], halfwave[1])
