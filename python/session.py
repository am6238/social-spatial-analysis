#   10/13/2024
#   --------------------------
#   Define the session class.
#   Author: Rajyashree Sen
#   --------------------------

# import packages
import os
import fnmatch

# functions
def generateListBySuffix(inputPath,inputFileFormat):
    fileNames = []
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if file.endswith(inputFileFormat):
                 fileNames.append(os.path.join(root, file))
    return fileNames

def generateList(inputPath,inputFilePattern):
    fileNames = []
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            if fnmatch.fnmatch(file, inputFilePattern):
                 fileNames.append(os.path.join(root, file))
    return fileNames

# define the session class
class Session:
    def __init__(self,
                 experimentDateFolderPath: str,
                 sessionFolderPrefix: str = 'Session',
                 sessionNumber: int):

        '''
        Takes as inputs: 1)the experiment date folder path, 2)the session number & 3)the session foldername prefix
        Returns: 1)the session folder path,
        Saves: 1)the experiment folder path, 2)the session number & 3)the session folder path
        '''

        self.inputPath     = experimentDateFolderPath
        self.sessionNumber = sessionNumber
        self.sessionPath   = os.path.join(self.inputPath,f"{sessionFolderPrefix}{self.sessionNumber}")


    def _get_imagingFileName(self,
                             imagingFileExtenstion: str = 'isxd'
                            ):
        '''
        Takes as new inputs: 1)imaging file extension
        Returns & saves: 1)imaging file full path
        '''

        imagingFileName = generateList(self.sessionPath, f"*{imagingFileExtenstion}*")[0]
        self.imagingFileName = imagingFileName


    def _generate_video(self,
                        camImagesFolderIdentifier: str = 'cam1',
                        outputVideoFileExtension: str = 'avi',
                        fps = 20
                       ):
        '''
        Takes as new inputs: 1)camImages folder name identifier, 2)output video file format, 3)frame rate (fps)
        Returns: 1)video generated from the still images within the camImages folder
        Saves: 1)output video full filepath, 2) outputVideoFileExtension
        '''
        self.sessionVideoFilePath = '' #code here#
        self.sessionVideoFileFormat = outputVideoFileExtension
        pass


    def _DLC_analyze_video(self,
                           configFile: str,
                           shuffle: int = 1,
                           displayedbodypartsList: list):
        '''
        Takes as new inputs: 1)DLC config path, 2) shuffle, 3) list of body parts to display on final video
        Returns & saves: 1)video generated from the still images within the camImages folder, 2) output video full filepath
                         3)DLC scorer name
                         4)csv file, 5)filtered csv file,
                         6)h5 file, 7)filtered h5 file,
                         8)pickle file
        '''


        # print(f"Starting to analyze: {self.sessionVideoFilePath")

        # video analysis
        self.scorername = deeplabcut.analyze_videos(configFile,
                                                    self.sessionVideoFilePath,
                                                    shuffle=shuffle,
                                                    videotype=self.sessionVideoFileFormat,
                                                    save_as_csv=True)

        # filter predictions
        deeplabcut.filterpredictions(configFile,
                                     [self.videoFileInputPath],
                                     save_as_csv=True,
                                     shuffle=shuffle)

        # create labeled video
        deeplabcut.create_labeled_video(configFile,
                                        self.videoFileInputPath,
                                        shuffle = shuffle,
                                        videotype = self.sessionVideoFileFormat,
                                        filtered = True,
                                        trailpoints = 10,
                                        draw_skeleton = True,
                                        displayedbodyparts = displayedbodypartsList)

        # store csv, h5 and pickle filenames - consider skipping if using a different class for csv files - but save scorername somewhere
        #self.csvFile            = ...
        #self.filteredcsvFile    = ...
        #self.h5File             = ...
        #self.pickleFile         = ...

    def _get_roiOccupancyMatrix(self,
                               sessionKeyExcelFile: str,
                               roiYamlFile: str,
                               distanceThreshold: float,
                               orientationThreshold: float):
        '''
        Takes as new inputs: 1)sessionKey excel sheet full path,
                             2)roi yaml file full path,
                             3)distance threshold to determine roi occupancy
                             4)orientation threshold to determine roi occupancy
        Uses from saved input: 1)DLC frame-by-frame data in h5 (or csv?) format
        Returns & saves: 1) frame-by-frame (x,y) locations (array),
                         2) frame-by-frame boolean for occupancy in each roi specified by the toi yaml file (boolean)
        '''
        pass

    def _plot_2D_traj(self):
        '''
        Takes as new input: 1)colors to indicate each roi/individual
        Uses from saved input: 1) roi Occupancy matrix (boolean), 2) x,y locations of nose (array)
        Returns & saves: 1) 2D trajectory plot, 2) full file path for trajectory plot
        '''
        pass

    def _plot_3D_traj(self):
        '''
        Takes as new input: 1)colors to indicate each roi/individual
        Uses from saved input: 1)roi Occupancy matrix (boolean), 2) x,y locations of nose (array)
        Returns & saves: 1) 3D trajectory plot, 2) full file path for trajectory plot
        '''
        pass

    def _plot_ethogram(self):
        '''
        Takes as new input: 1)colors to indicate each roi/individual
        Uses from saved input: 1)roi Occupancy matrix (boolean), 2) x,y locations of nose (array)
        Returns & saves: 1) ethogram, 2) full file path for ethogram
        '''
        pass
