#   10/07/2024
#   -----------------------------
#   Define the Experiment class.
#   -----------------------------

# import packages
import os
import numpy as np
import re
import .session

# define experiment class
class Experiment:
    def __init__(self,
            name: str,
            path: str,
            sessionKeyPath: str=None,
            roiPath: str=None,
            sessions: [Session]=None,
            gatheredDataPath: str=None,
            X: np.ndarray(dtype=np.float64, ndim=3)=None,
            animalLabels: np.ndarray(dtype=np.int16, ndim=1)=None,
            siteLabels: np.ndarray(dtype=np.int16, ndim=1)=None):

        """
        This is the main experiment class.
        ---------------------------------------
        
        CLASS VARIABLES 
        
        NAME -- a string, either "TwoChamber", "FourChamber",
                "OneChamber", etc.

        PATH -- the path to the experiment folder, where all
                the data is stored (roiMidpoints, sessionKey,
                and individual session folders, etc).

        SESSIONKEYPATH -- path to the session key file.

        ROIPATH -- path to the roiMidpointsList.yaml file.

        SESSIONS -- list of instances of the Session class, one
                    for each session in the experiment.

        GATHEREDDATAPATH -- path to the gatheredData.mat file.

        X -- the full matrix of neural data from this experiment,
             of shape [neurons x timesteps].

        X_svm -- the matrix of neural data but organized according to
                 bouts and averaged across time for each bout. Of 
                 shape [neurons x bouts]


        """


