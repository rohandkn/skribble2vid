import gradio as gr
import cv2
import copy
import os
import subprocess
from PIL import Image

number_of_sketch_frames = 3 #@param {type:"slider", min:1, max:7, step:1}

def generate_video(prompt, *sketches):
    input_sketches_path = 'rife-interop/input_images'
    os.makedirs(input_sketches_path, exist_ok=True)
    
    
    # print("hellooooooooooooooo")
    # print(prompt)
    # print(sketches)

    # Save sketches as PNGs
    for idx, sketch in enumerate(sketches):
        rgb_sketch = sketch.convert('RGB')
        rgb_sketch.save(os.path.join(input_sketches_path, f'{idx}.png'))


    # Run the inference_video.py script
    subprocess.run(['python3', 'inference_video.py', '--img', 'input_images', '--png'], cwd='rife-interop')

    # Run the run_tests.py script
    subprocess.run(['python3', 'run_tests.py', '--prompt', prompt], cwd='vid2vid')

    # Load the output video
    output_video_path = 'vid2vid/output_vid/output.mp4'
    return output_video_path


prompt_input = gr.inputs.Textbox(label="Enter a text prompt")

sketch_inputs = [gr.Sketchpad(label="Draw Here", brush_radius=5, type="pil", shape=(120, 120)) for _ in range(number_of_sketch_frames)]
input_sketch = [prompt_input] + sketch_inputs

output = gr.outputs.Video(label="Generated video")

iface = gr.Interface(
    fn=generate_video,
    inputs=input_sketch,
    outputs=output,
    title="Sketch The Future",
    description="Sketch desired frames and enter text prompt to generate a video result."
)

if __name__ == "__main__":
    iface.launch(share=True)
