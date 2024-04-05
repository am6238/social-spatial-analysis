#   04/05/2024 Alex Medoff
#   -------------------------
#   Define the classes to be used by this python project.
#   ------------------------------------------------------

# import libraries
import numpy as np
import os
import re

# Define the main class: "Analysand"
class Analysand:
    """
    This is the main class that contains all
    the experimental data, and the class implements
    all the analysis we wish to run on it.

    The class contains the neural data matrix,
    mouseXY position, and ROI information.
    """
    pass        

# Define the class: "FourChamber"
class FourChamber:
    """
    This is the class that represents a single
    fourchamber experiment. The main parameter
    is the "path" which gives the path to the folder
    where all the data for this experiment can be
    found.

    This class implements methods that do things like:
        1) extract the neural data from .mat files
        2) extract the mouse XY positions from the DLC data
        3) extract the ROI midpoint data from the .yml file
    """
    def __init__(self,
            path: str,
            matlabDatafile: str = "populationMatrix.mat",
            roiFilename: str = "roiMidPointsList.yml",
            sessionKeySuffix = "_sessionKey.xlsx",
            camNum: int = 1,
            h5filetag: str = "filtered.h5"):
        """
        PARAMETERS

        path: str, the path to this experiment. For example,
              "/InscopixExperiments/FourChamber_Completed/MouseS79/20220715/"

        matlabDatafile: str, the name of the .mat file within the "path"
                        directory, which contains three variables:
                            1. "X" matrix [nNeurons x nTimesteps]
                            2. "session" vector with session labels
                            3. "time" vector with timestep numbers

        roiFilename: str, the name of the roi midpoints yaml file.

        sessionKeySuffix: str, the suffix of the session key filename.

        camNum: int, whether to use cam1 or cam0. Default cam1.

        h5filetag: str, the string tag to look for when identifying
                   the h5 files from which to extract XY position data.

        """

        # set all the passed-in parameters as attributes
        self.path = path
        self.matlabDatafile = matlabDatafile
        self.roiFilename = roiFilename
        self.sessionKeySuffix = sessionKeySuffix
        self.camNum = camNum
        self.h5filetag = h5filetag

        # initialize other attributes
        
        # attributes of neural data
        self.X = None
        self.sessions = None
        self.time = None

        # attributes of mouse XY position
        self.noseX = None
        self.noseY = None
        self.tailX = None
        self.tailY = None

        # attributes of interactive bouts
        self.roiOccupancy = None

    def loadNeuralData(self):
        """
        Method that loads the MATLAB file and extracts neural data.

        PARAMETERS
            
        self

        OUTPUT

        fills self.X, self.sessions, and self.time.

        """
        matlabFile = os.path.join(self.path, self.matlabDatafile)
        







