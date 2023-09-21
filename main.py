import cv2, os, time, glob
from tqdm import tqdm


def extract_images(pathIn):

    saving_path = "frames"
    if not os.path.exists(saving_path):
        os.mkdir(saving_path)
    else:
        for file in glob.glob(saving_path + "/*"):
            os.remove(file)

    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(pathIn)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames:", video_length)
    count = 0
    print ("Converting video..")

    progress_bar = tqdm(range(video_length))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imwrite(os.path.join(saving_path, f"frame_{count + 1}.jpg"), frame)
        count = count + 1
        progress_bar.update(1)
        if (count > (video_length-1)):
            time_end = time.time()
            cap.release()
            print ("\nDone extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break


video_path = "video/test.mp4"
extract_images(video_path)