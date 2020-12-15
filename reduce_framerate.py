import cv2 

output='output.mp4'

vid_cap = cv2.VideoCapture('video.mp4') 
length = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))


fourcc = 'mp4v'  # output video codec
fps = vid_cap.get(cv2.CAP_PROP_FPS)/4
w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
vid_writer = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))

print('old framerate = %g' % fps)

hasFrames,image = vid_cap.read()
i=1
while hasFrames:
    i+=1
    if (i % 4) == 0:
        vid_writer.write(image)
        print('writing %g / %g' % (i, length))
    hasFrames,image = vid_cap.read()

output_cap = cv2.VideoCapture(output) 
print('new framerate = %g' % vid_cap.get(cv2.CAP_PROP_FPS))