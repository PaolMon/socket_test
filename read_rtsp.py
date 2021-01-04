import numpy as np
from matplotlib import pyplot as plt
import ffmpeg


width = 1080 #2560
height = 720 #1440

dim = width * height * 3

process1 = (
    ffmpeg
    .input('rtsp://192.168.1.17/11', s='{}x{}'.format(width, height))
    .output('-', format='rawvideo')
    .run_async(pipe_stdout=True)
)


in_bytes = process1.stdout.read(dim)
print('first done')
while process1.poll() is None:
    in_bytes = process1.stdout.read(dim)
    if not in_bytes:
        print('something missing')
        break
    in_frame = (
        np
        .frombuffer(in_bytes, np.uint8)
        .reshape([height, width, 3])
    )


process1.wait()

