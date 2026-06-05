# intallation of astronomical packages; astropy, numpy, scipy, matplotlib, astroquery, photutils,
# specutils via pip.
# Opening a FITS file(fits stands for flexible image transport system, fits is a file format used
# by astromer to store telescope images, spectra and time series observation).
# astropy.io is used to open fits file, read image data, read observation metadata and save new fits files

#Importing the fits module to open a fit file
from astropy.io import fits 

#Loading the Hubble Space telescope fits image into hdul
hdul = fits.open(r"C:\Users\Quite Happy\Documents\Data Analysis for beginner\Python for Analysis\Astronomy python\ib7796010\ib7796010_drz.fits")

#Printing the information of the telescope image
hdul.info()

#Printing the first row of the data
print(hdul[0].header)


''''''''''''''''''''''''''''''''''''''''''''''''''
#Visualization of IMAGE_HDU

#Importing ZscaleInterval to reduce the brightness of the star to make 
# the less bright star visible (even out the stars)
from astropy.visualization import ZScaleInterval

#importing matplotlib.pyplot to create the image of the fit file, using 
# plt as the shorthand
import matplotlib.pyplot as plt

#Extracting the pixel data by identifying it name "SCI"
sci_data = hdul["SCI"].data

#Extracting the header metadata of the SCI extension; the information 
# about the image.
sci_header = hdul["SCI"].header

#Plot with Zscale 
interval = ZScaleInterval()
Vmin, Vmax = interval.get_limits(sci_data)

#Creating a blank canva to draw on
plt.figure(figsize =(10,9))

#Displaying the numpy array, giving it color, origin and scale
plt.imshow(sci_data, cmap="gray", origin ="lower", vmin =Vmin, vmax=Vmax)
plt.colorbar(label= "Flux (e^-/s)")

#Adding title above the image
plt.title("HST SCI IMAGE - ib7796010_drz")

#Saving image to system storage
plt.savefig(r"C:\Users\Quite Happy\Documents\Data Analysis for beginner\Python for Analysis\Astronomy python\ib7796010_sci_image.png",
    dpi=300,
    bbox_inches='tight')

#Displaying it in real time
plt.show()


''''''''''''''''''''''''''''''''''''''
#The WHT extension tells you HOW RELIABLE each pixel is. It records 
# how much total exposure time contributed to each pixel during the drizzle
# combining process.
#Getting the weight map of the data
weight_data = hdul['WHT'].data

# Create a bad pixel mask by excluding pixels with zero weight
import numpy as np
bad_mask = weight_data == 0

# Compute per-pixel noise (uncertainty)
# For drizzled data: sigma = 1 / sqrt(WHT)
uncertainty = np.where(weight_data > 0, 1.0 / np.sqrt(weight_data), np.nan)

#Creating the visual using matplotlib, giving it color, origin and scale
plt.imshow(weight_data, cmap='hot', origin='lower')
plt.colorbar(label='Weight (exposure contribution)')
plt.title('Weight Map — low values = unreliable pixels') 

#Saving image to system storage
plt.savefig(r"C:\Users\Quite Happy\Documents\Data Analysis for beginner\Python for Analysis\Astronomy python\ib7796010_WHT_image.png",
    dpi=300,
    bbox_inches='tight')

#Displaying it in real time
plt.show()


''''''''''''''''''''''''''''''''''''''''''''''''''
#CTX is a BITMASK image and each pixel's integer value encodes WHICH 
# individual input exposures contributed to that output pixel in the 
# drizzle combination.
#Extracting the header metadata of the CTX extension and the information 
# about the image. loading it into context data.
context_data = hdul['CTX'].data

#  creates a brand new array that is the SAME SHAPE as ctx_data: (1039, 1093)
number_inputs = np.zeros_like(context_data, dtype=int)
for bit in range(32):
    number_inputs += (context_data >> bit) & 1

#PLOTING THE CONTEXT MAP
plt.imshow(number_inputs, cmap='viridis', origin='lower')
plt.colorbar(label='Number of input exposures per pixel')
plt.title('Context Map')

#Saving image to system storage
plt.savefig(r"C:\Users\Quite Happy\Documents\Data Analysis for beginner\Python for Analysis\Astronomy python\ib7796010_CTX_image.png",
    dpi=300,
    bbox_inches='tight')

#Displaying it in real time
plt.show()
