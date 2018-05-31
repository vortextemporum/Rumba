from rumba import *

n = 8

bam = Shuffle(n)
# print(bam.sequence)
bam.scaleToVideo(n)

video_arguments = {
    "output": "test_1.mp4",
    "length": 1,
    "offset": random.uniform(0.05,0.1)

}


bam.testPattern(**video_arguments)