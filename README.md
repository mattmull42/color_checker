# color-checker

Characterization of a ColorChecker


# Files and directories

* **CC**:
Contains the reflectances of the color checker for each case of the color checker. It contains two files :
    - A numpy archive of the reflectance matrix (1st dimension is the case, 2nd dimension is spectral) and the wavelength sample along which the reflectances are measured.
    - A csv file of the reflectances in function of the wavelength.

* **CC_GEOM**:
Contains the reflectances of the color checker for each case of the color checker acquired with different angles. It contains two files :
    - A numpy archive of the reflectance tensor (1st dimension is the case, 2nd dimension is angular, 3rd dimension is spectral), the angle samples and the wavelength samples along which the reflectances are measured.
    - For each case of the color checker a csv file of the reflectances in function of the angle and the wavelength.

* **plots**:
Contains the plots of the reflectances, for the CC acquisition, CC_GEOM. The directory 'joint' contains  the CC and CC_GEOM on the same plots for each case. Moreover the file 'all_cases.png' in 'plots/CC/' is the plot of all the cases.

* **color_checker.png**:
The color checker and the cases indexing.

* **plot_notebook.ipynb**:
A simple notebook that shows how to open the numpy archives and to plot the reflectances and save them if needed.

* **ploter.py**:
The python functions used by the notebook for the plots.

* **requirements.txt**:
The list of python modules in order to run the notebook.