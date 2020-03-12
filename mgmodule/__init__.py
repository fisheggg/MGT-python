import os
from ._input_test import mg_input_test
from ._videoreader import mg_videoreader
from ._flow import Flow


class MgObject:
    """ 
    Initializes Musical Gestures data structure from a given parameter video file.

    Parameters:
    -----------
    - filename (str): Name of input parameter video file.
    - filtertype (str): 'Regular', 'Binary', 'Blob' (see function filterframe).
    - thresh (float): A number in [0,1]. Eliminates pixel values less than given threshold.
    - starttime (float): Cut the video from this start time (min) to analyze what is relevant.
    - endtime (float): Cut the video at this end time (min) to analyze what is relevant.
    - blur (str): 'Average' to apply a blurring filter, 'None' otherwise.
    - skip (int): When proceeding to analyze next frame of video, this many frames are skipped.
    - color (bool): True does the analysis in RGB, False in grayscale.
    - contrast (float): Apply +/- 100 contrast to video.
    - brightness (float): Apply +/- 100 brightness to video.
    - crop (str): 'none', 'manual', 'auto' to select cropping of relevant video frame size.
    """

    def __init__(self, filename, filtertype='Regular', thresh=0.05, starttime=0, endtime=0, blur='None', skip=0, color=True, contrast=0, brightness=0, crop='None', keep_all=False):

        self.filename = filename
        # name of file without extension (only-filename)
        self.of = os.path.splitext(self.filename)[0]
        # file extension
        self.fex = os.path.splitext(self.filename)[1]
        self.color = color
        self.starttime = starttime
        self.endtime = endtime
        self.skip = skip
        self.filtertype = filtertype
        self.thresh = thresh
        self.blur = blur
        self.contrast = contrast
        self.brightness = brightness
        self.crop = crop
        self.keep_all = keep_all
        self.test_input()
        self.get_video()
        self.flow = Flow(self.filename)

    from ._motionvideo import mg_motionvideo as motion
    from ._motionvideo import plot_motion_metrics
    from ._cropvideo import mg_cropvideo, find_motion_box, find_total_motion_box
    from ._motionhistory import mg_motionhistory as motionhistory
    from ._show import mg_show as show
    from ._history import history
    from ._average import mg_average_image as average

    def test_input(self):
        """ Gives feedback to user if initialization from input went wrong. """
        mg_input_test(self.filename, self.filtertype,
                      self.thresh, self.starttime, self.endtime, self.blur, self.skip)

    def get_video(self):
        """ Creates a video attribute to the Musical Gestures object with the given correct settings. """
        self.length, self.width, self.height, self.fps, self.endtime, self.of, self.fex = mg_videoreader(
            self.filename, self.starttime, self.endtime, self.skip, self.contrast, self.brightness, self.crop, keep_all=self.keep_all)

        # update filename after the processes
        self.filename = self.of + self.fex

    def __repr__(self):
        return f"MgObject('{self.filename}')"
