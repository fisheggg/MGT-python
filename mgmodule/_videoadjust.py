import numpy as np
import cv2

def contrast_brightness(of,vidcap,fps,width,height,contrast,brightness):
    """
    Edit contrast and brightness of the video.
    
    of (str): filename without extension
    vidcap: cv2 capture of video file, with all frames ready to read with vidcap.read().
    fps, width, height are simply info about vidcap
    contrast (float): apply +/- 100 contrast to video
    brightness (float): apply +/- 100 brightness to video
    
    return: cv2 video capture of edited video file
    """
    count = 0;
    if brightness != 0 or contrast != 0:
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(of + '_cb.avi',fourcc, fps, (width,height))
        success,image = vidcap.read()
        while success: 
            success,image = vidcap.read()
            if not success:
                break
            image = np.int16(image) * (contrast/127+1) - contrast + brightness
            image = np.clip(image, 0, 255)
            out.write(image.astype(np.uint8))  
            count += 1
        out.release()
        vidcap = cv2.VideoCapture(of + '_cb.avi')

    return vidcap

def skip_frames(of, vidcap, skip, fps, width, height):
    """
    Frame skip, convenient for saving time/space in an analysis of less detail looking at big picture movement. Skips the given number of frames, making a compressed version of the input video file.
    
    of (str): filename without extension
    vidcap: cv2 capture of video file, with all frames ready to read with vidcap.read().
    fps, width, height are simply info about vidcap
    skip (int): When proceeding to analyze next frame of video, this many frames are skipped.
    
    return:
        cv2 video capture of edited video file
        length, fps, width, height from this video capture
    """
    count = 0;
    if skip != 0:
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter(of + '_skip.avi',fourcc, int(fps/skip), (width,height))
        success,image = vidcap.read()
        while success: 
            success,image = vidcap.read()
            if not success:
                break
            # on every frame we wish to use
            if (count % skip ==0):
              out.write(image.astype(np.uint8))  
            
            count += 1
        out.release()
        vidcap = cv2.VideoCapture(of + '_skip.avi')

        length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return vidcap, length, fps, width, height