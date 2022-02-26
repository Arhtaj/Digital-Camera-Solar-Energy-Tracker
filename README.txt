Digital Camera solar energy tracker, by Thomas Mikhail

The purpose of this script is to identify where a solar panel should face given an image in JPEG format.
It uses a combination of roughly estimatings wavelengths and intensity from rgb values, and then determining
the "area" of the image with the most and "highest quality" light. While such an algorithm is less energy 
and cost efficient than using simple solar trackers, it may be useful for obtaining data; for example in
cities where panels may only be able to absorb reflected light, this algorithm should be able to find the
best directions at different seasons/months per year.

Usage:
Enter path to image in main.py line 13.

Values and relative weights were obtained by rough curve fitting comparing the relative sensitivity of each
wavelength to the relative energy output from a silicon solar panel. Data obtained from the following sources,
and csv files provided under "Data". 

Typical silicon photovoltaic cell spectral response to solar spectrum:
https://www.researchgate.net/figure/Typical-silicon-photovoltaic-cell-spectral-response-to-solar-spectrum_fig3_237202290
Phone camera sensor relative response:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8347217/
