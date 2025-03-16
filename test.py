import cv2 as cv

video_file = 'c:/Users/benet/Desktop/비전/비전1/4620511-uhd_2160_4096_25fps.mp4'
target_format = 'avi'
target_fourcc = 'XVID'

video = cv.VideoCapture(video_file)

flip = False

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    target = cv.VideoWriter()
    recording = False 

    while True:
        valid, img = video.read()
        if not valid:
            break

        display = img.copy()

        if flip:
            display = cv.flip(display, 1) 

        if recording:
            center = (50, 50)
            cv.circle(display, center, radius=10, color=(0, 0, 255), thickness=-1)

        cv.imshow('Video Player', display)

        key = cv.waitKey(wait_msec)
        if key == 27:  
            break
        elif key == 32:  
            if recording:
                target.release()
                recording = False
            else:
                target_file = video_file[:video_file.rfind('.')] + '.' + target_format
                h, w, *_ = img.shape
                is_color = (img.ndim > 2) and (img.shape[2] > 1)
                target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)
                recording = True
        elif key == ord('f'): 
            flip = not flip

        if recording:
            target.write(display)

    if recording:
        target.release()

    cv.destroyAllWindows()
