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
            path: str)

        """
        This is the main experiment class.
        ---------------------------------------
        
        CLASS VARIABLES 
        
        NAME -- a string, either "TwoChamber", "FourChamber",
                "OneChamber", etc.

        PATH -- a string, the path to the experiment folder,
                where the data is stored (roiMidpoints, sessionKey,
                and individual session folders, etc).

        SESSIONKEYPATH -- a string, path to the session key file.

        ROIPATH -- a string, path to the roiMidpointsList.yaml file.

        SESSIONS -- list of instances of the Session class, one
                    for each session in the experiment.

        GATHEREDDATAPATH -- a string, path to the gatheredData.mat file.

        X -- np.ndarray(dtype=np.float64, ndim=2), the full matrix of
             neural data from this experiment, of shape [neurons x timesteps].

        NOSEX -- vector of the mouse nose position through experiment
        NOSEY -- (see above)
        TAILX -- (see above)
        TAILY -- (see above)

        SESSIONLABELS -- session labels that index X, position vectors
                         (noseX, noseY, etc...)

        """
        
        # -------------------

        # set the name and path from input
        self.name = name
        self.path = path

        # get the sessionkey path, roipath
        mouse = re.search("MouseS\d{2,3}", self.path).group(0)
        date  = re.search("20\d{6}", self.path).group(0)
        self.sessionKeyPath = os.path.join(self.path, f"{date}_sessionKey.xlsx")
        self.roiPath = os.path.join(self.path, "roiMidPointsList.yml")

        # call method to create the list of Sessions
        self.findSessions()

        # -------------------------------------------
        # ----- METHODS --------------------
        # ----------------------

        def findSessions(self):
            """
            looks through self.path to identify the session
            folders, and then creates an instance of the 
            session class for each folder, puts them all
            into a list, and sets that as self.sessions.
            
            INPUTS
            
            self -- the instance of Experiment
            
            OUTPUTS
            
            returns nothing. initializes self.sessions

            """
            
            # initialize sessions list
            sessions = []

            # step through files in self.path
            for f in os.listdir(self.path):

                # if isdir and contains "Session",
                # then use it to create Session
                if os.path.isdir(os.path.join(self.path, f)) and "Session" in f:
                    session = Session(os.path.join(self.path, f)) 
                    sessions.append(session)

            # set self.sessions = sessions
            self.sessions = sessions
        
        def generateVideosFromImagesAllSessions(self):
            """
            loops through each session in self.sessions
            and calls the method in the Session class that
            generates videos from images.
            
            INPUTS

            self -- the instance of Experiment

            OUTPUTS

            returns nothing. generates session videos.

            """

        def runDLCAllSessions(self):
            """
            runs deep lab cut on all the sessions
            in self.sessions.

            INPUTS

            self -- the instance of Experiment

            OUTPUTS

            returns nothing. generates deeplabcut files.

            """


