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

    # initialize global variables (i.e. are
    # true for every instance of the Experiment class)
    FRAMERATE = 20
    PCA_WINDOW = [-1,4]

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

        X_SVM -- np.ndarray(dtype=np.float64, ndim=3), the matrix of neural data
                 organized to be used by the SVM. Of the shape [neurons x bouts]
        
        X_SVM_SESSIONLABELS -- np.ndarray(dtype=np.int16, ndim=1), the labels
                               for every bout of X_SVM. Shape [bouts]
        X_SVM_ANIMALLABELS -- (similar to above)
        X_SVM_SITELABELS -- (similar to above)

        NOSEX -- vector of the mouse nose position through experiment
        NOSEY -- (see above)
        TAILX -- (see above)
        TAILY -- (see above)

        X_SESSIONLABELS -- session labels that index X, position vectors
                           (noseX, noseY, etc...)

        """
        
        # -------------------

        # set the name and path from input
        self.name = name
        self.path = path
        
        # initialize all the other local variables
        self.sessions = []
        self.sessionKeyPath = ""
        self.roiPath = ""
        self.gatheredDataPath = ""
        self.correctedCellRegisterPath = ""
        self.svmResultsPath = ""
        self.svmShuffledResultsPath = ""
        self.pcaAnimalComponentsPath = ""
        self.pcaSiteComponentsPath = ""
        self.X = None
        self.X_svm = None
        self.X_svm_sessionLabels = None
        self.X_svm_animalLabels = None
        self.X_svm_siteLabels = None
        self.X_pca = None
        self.X_pca_sessionLabels = None
        self.X_pca_animalLabels = None
        self.X_pca_siteLabels = None
        self.noseX = None
        self.noseY = None
        self.tailX = None
        self.tailY = None
        
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

    def runMotionCorrection(self):
        """
        opens MATLAB and runs the motion correction
        script on this experiment path. (can do this
        using the matlab.engine python package)

        INPUTS

        self -- the instance of Experiment

        OUTPUTS

        returns nothing. runs motion correction.
        
        """

    def identifyCorrectedCellRegistration(self):
        """
        method to be run AFTER having corrected the
        motion correction in MATLAB. This method
        will then look into the experiment path
        to find the corrected .mat file.

        INPUTS

        self -- the instance of Experiment

        OUTPUTS

        returns nothing. Sets self.correctedCellRegisterPath.
        
        """
    
    def connectBehaviorAndNeuralData(self):
        """
        opens MATLAB and runs the scripts to
        connect the behavioral and neural data.

        INPUTS

        self -- the instance of Experiment

        OUTPUTS

        returns nothing. runs connect scripts.

        """

    def getX_svm(self):
        """
        opens MATLAB and runs a script there
        that unpacks the gatheredData.mat file
        to get the X_svm, sessionLabels, siteLabels,
        and animalLabels.

        INPUTS

        self -- the instance of Experiment

        OUTPUTS

        returns nothing. sets the following variables:
            
            X_svm : np.ndarray(dtype=np.float64,ndim=2),
                    of the shape [neurons x bouts]
            X_svm_sessionLabels : np.ndarray(dtype=np.int16, ndim=1),
                            of the shape [bouts]
            X_svm_siteLabels    : (same as sessionLabels)
            X_svm_animalLabels  : (same as sessionLabels)

        """

    def runSVM(self):
        """
        runs animal and site SVMs.

        INPUTS

        self -- the instance of Experiment. Will mostly make
                use of the following variables:
            X_svm
            X_svm_sessionLabels
            X_svm_siteLabels
            X_svm_animalLabels

        OUTPUTS

        returns nothing. generates figures, produces text in console,
        and saves the SVM results in the path. Thus, it sets the following
        variable:
            
            svmResultsPath : String
            svmShuffledResultsPath : String
        """

    def getX_pca(self):
        """
        opens MATLAB and runs a script there
        that unpacks the gatheredData.mat file
        to get the X_pca, and its associated labels.

        INPUTS

        self -- the instance of Experiment

        OUTPUTS

        returns nothing. sets the following variables:

            X_pca : np.ndarray(dtype=np.float64, ndim=3),
                    of the shape [neurons x timesteps x bouts]
            X_pca_sessionLabels : np.ndarray(dtype=np.int16, ndim=1),
                                    of the shape [bouts]
            X_pca_siteLabels : (same as above)
            X_pca_animalLabels: (same as above)
        """

    def runPCA(self):
        """
        runs PCA for animal and site separately.

        INPUTS

        self -- the instance of Experiment. Will mostly make
                use of the following variables:

            X_pca
            X_pca_sessionLabels
            X_pca_siteLabels
            x_pca_animalLabels

        OUTPUTS

        returns nothing. generates figures, produces text in console,
        and saves the PCA components in the path. Thus, it sets the
        following variable:
            
            pcaAnimalComponentsPath : String
            pcaSiteComponenetsPath : String
        """


