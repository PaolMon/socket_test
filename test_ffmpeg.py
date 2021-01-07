
import ffmpeg
import cv2
import numpy as np
import sys

rtsp_url = 'rtsp://192.168.1.17/11'
print('starting...')
try:
    probe = ffmpeg.probe(rtsp_url)
except ffmpeg.Error as e:
    print(e.stderr, file=sys.stderr)
    sys.exit(1)

video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
if video_stream is None:
    print('No video stream found', file=sys.stderr)
    sys.exit(1)

width = int(video_stream['width'])
height = int(video_stream['height'])
print('found video stream {}x{}'.format(width, height))
dim = width * height * 3

process1 = (
    ffmpeg
    .input(rtsp_url)
    .output('-', format='rawvideo')
    .run_async(pipe_stdout=True)
)

while process1.poll() is None:
        frame = process1.stdout.read(dim)
        y = np.frombuffer(frame, dtype=np.uint8, count=-1)
        img0=np.reshape(y, (height, width, 3))
        img = cv2.resize(img0, (1280,720))
        cv2.imshow("received", img)
        if cv2.waitKey(1) == ord('q'):  # q to quit
            raise StopIteration