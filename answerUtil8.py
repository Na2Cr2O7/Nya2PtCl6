# import argparse
# import random
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from model.model_minimind import MiniMindConfig, MiniMindForCausalLM
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from model.model_vlm import MiniMindVLM, VLMConfig
from model.model_lora import *
from colorama import Fore
import torch
from PIL import Image
import os
try:
    import torch_directml  # type: ignore

    device = torch_directml.device(0) # GPU 0 (intel HD Graphics 520)
    print(Fore.GREEN + 'Using DirectML for GPU acceleration')
except ImportError:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
max_seq_len=8192
hidden_size=768
num_hidden_layers=16

lm_config = VLMConfig(hidden_size=hidden_size, num_hidden_layers=num_hidden_layers,
                          max_seq_len=max_seq_len, use_moe=False)
print(Fore.BLUE + f'Using device: {device}')
tokenizer = AutoTokenizer.from_pretrained('./model')
ckp='./out/sft_vlm_768.pth'
model = MiniMindVLM(lm_config, vision_model_path="./model/vision_model/clip-vit-base-patch16")
print(f'Loading checkpoint from {ckp}')
state_dict = torch.load(ckp, map_location=device)
model.load_state_dict({k: v for k, v in state_dict.items() if 'mask' not in k}, strict=False)
model.to(device)
model.eval()
vision_model, preprocess = model.vision_encoder, model.processor
vision_model.eval()
vision_model.to(device)
def predict2(question, pixel_tensors):
    prompt = f"{model.params.image_special_token}\n{question}"
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=340,
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
import flask
import json
app = flask.Flask(__name__)

@app.route('/<modelName>/<question>/<imageDir>', methods=['POST'])
def get_answer(modelName, question, imageDir=None):
    if imageDir is None or not os.path.exists(os.path.abspath(imageDir)):
        imageDir='null.png'
    image = Image.open(os.path.abspath(imageDir)).convert('RGB')
    pixel_tensors = MiniMindVLM.image2tensor(image, preprocess).to(device).unsqueeze(0)

    print(modelName, question,imageDir)
    answer=predict2(question, pixel_tensors)
    print(answer)
    dt=json.dumps({'question':question,'answer':answer})
    with open('replyHistory.txt','a') as f:
        f.write(dt)
    return flask.jsonify({'answer': answer})

@app.route('/<modelName>/<question>', methods=['POST'])
def get_answer_without_image(modelName, question):
    imageDir='null.png'
    return get_answer(modelName, question, imageDir)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)