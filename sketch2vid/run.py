import sys
import os
sys.path.append("/home/mverghese/Documents/vignesh-VLR/sketch2vid/vid2vid")
sys.path.append("/home/mverghese/Documents/vignesh-VLR/sketch2vid/arXiv2020-RIFE")
from run_tests import video2video
from moviepy.editor import ImageSequenceClip
import subprocess
input_vid = "input.mp4"
output_vid = "out.mp4"

def images_to_video_new(input_dir, output_path, fps=30):
    # Get all image file names in the input directory
    image_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg') or f.endswith('.png')]

    # Sort the file names alphabetically
    image_files.sort()

    # Create an ImageSequenceClip from the images
    clip = ImageSequenceClip([os.path.join(input_dir, f) for f in image_files], fps=fps)

    # Write the clip to a video file
    clip.write_videofile(output_path, fps=fps, codec='libx264')


#video_path = 'vid2vid/__assets__/canny_videos_mp4/deer_pic.jpeg'
#prompt = "Deer walking in the street"
#params = {"t0": 44, "t1": 47 , "motion_field_strength_x" : 12, "motion_field_strength_y" : 12, "video_length": 2}

#prompt = 'oil painting of a deer, a high-quality, detailed, and professional photo'
#images_to_video_new('vid2vid/__assets__/frames', 'vid2vid/__assets__/canny_videos_mp4/myvideo_new.mp4', 1)
#video_path = 'vid2vid/__assets__/canny_videos_mp4/interski.mp4'
#out_path = f'./final_{prompt}.mp4'
#model.process_controlnet_canny(video_path, prompt=prompt, save_path=out_path)
prompt = "Realistic painting of deer"
image_path = 'vid2vid/__assets__/frames'
skribble_anim = 'vid2vid/__assets__/canny_videos_mp4/myvideo_new.mp4'
images_to_video_new(image_path, skribble_anim)
input_vid = skribble_anim
output_vid = "output.mp4"
#video2video(input_vid, output_vid, prompt)

my_env = os.environ.copy()
my_env["PATH"] = "/home/mverghese/Documents/vignesh-VLR/sketch2vid/arXiv2020-RIFE" + my_env["PATH"]
result = subprocess.Popen(['env/bin/python', 'arXiv2020-RIFE/inference_video.py', '--exp=5', '--video=vid2vid/output.mp4', '--fps=20', '--skip'], env=my_env, stdout=subprocess.PIPE)
print(result.stdout)



