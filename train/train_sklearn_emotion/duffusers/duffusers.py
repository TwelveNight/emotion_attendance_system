from diffusers import DiffusionPipeline
import torch
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")


import random
import os

os.makedirs('/content/faces/happy', exist_ok=True)
os.makedirs('/content/faces/sad', exist_ok=True)
os.makedirs('/content/faces/surprised', exist_ok=True)


ethnicities = ['a latino', 'a white', 'a black', 'a middle eastern', 'an indian', 'an asian']

genders = ['male', 'female']

emotion_prompts = {'happy': 'smiling',
                   'sad': 'frowning, sad face expression, crying',
                   'surprised': 'surprised, opened mouth, raised eyebrows',
                   }


for j in range(250):

    for emotion in emotion_prompts.keys():

        emotion_prompt = emotion_prompts[emotion]

        ethnicity = random.choice(ethnicities)
        gender = random.choice(genders)

        # print(emotion, ethnicity, gender)

        prompt = 'Medium-shot portrait of {} {}, {}, front view, looking at the camera, color photography, '.format(ethnicity, gender, emotion_prompt) + \
                 'photorealistic, hyperrealistic, realistic, incredibly detailed, crisp focus, digital art, depth of field, 50mm, 8k'
        negative_prompt = '3d, cartoon, anime, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ' + \
                          '((grayscale)) Low Quality, Worst Quality, plastic, fake, disfigured, deformed, blurry, bad anatomy, blurred, watermark, grainy, signature'

        img = pipeline(prompt, negative_prompt=negative_prompt).images[0]

        img.save('/content/faces/{}/{}.png'.format(emotion, str(j).zfill(4)))

        # plt.imshow(img)
        # plt.show()

