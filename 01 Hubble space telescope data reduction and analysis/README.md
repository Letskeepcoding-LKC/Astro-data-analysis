Hubble Space Telescope Data Reduction and Analysis.
Personal Research Project | Python · Astropy · NumPy · Matplotlib
I've been working through real Hubble Space Telescope (HST) FITS data as part of a self-directed project to build 
practical skills in astronomical data analysis. The work started simply as opening a drizzled HST image and understanding
what each extension in the file actually means, then the exploration grown into a hands-on exploration of how to professional observe
process and interpret raw telescope data.
So far I've worked through the full structure of a drizzled FITS file: extracting the science image (SCI), 
using the weight map (WHT) to identify unreliable pixels and compute per-pixel noise, and decoding the context map (CTX) using bitwise
operations to determine how many individual exposures contributed to each region of the sky. Each of these steps mirrors the kind of 
data quality assessment that goes into real HST pipeline work.
The goal isn't just to produce plots — it's to understand why each step exists and what happens to your science if you skip it.
That distinction betweenrunning code and understanding data is what I'm most focused on developing.
This project is ongoing, working toward a complete reduction pipeline: from raw FITS input through calibration, source detection,
aperture photometry, and catalog production.
