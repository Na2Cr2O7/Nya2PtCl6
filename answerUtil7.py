# import argparse
# import random
import warnings
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from model.model_minimind import MiniMindConfig, MiniMindForCausalLM
from model.model_lora import *
from colorama import Fore
try:
    import torch_directml  # type: ignore

    device = torch_directml.device(0) # GPU 0 (intel HD Graphics 520)
    print(Fore.GREEN + 'Using DirectML for GPU acceleration')
except ImportError:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device=torch.device('cpu')
print(Fore.GREEN + f'Using device: {device}')
hidden_size = 512
num_hidden_layers = 8
use_moe = False
top_p = 0.85
tokenizer = AutoTokenizer.from_pretrained('./model/')
ckp = f'./out/full_sft_{hidden_size}.pth'
model = MiniMindForCausalLM(MiniMindConfig(
            hidden_size=hidden_size,
            num_hidden_layers=num_hidden_layers,
            use_moe=use_moe
        ))
model.load_state_dict(torch.load(ckp, map_location=device), strict=True)
apply_lora(model)
load_lora(model, f'./out/lora/lora_N_{hidden_size}.pth')
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

model=model.to(device)
model.eval()

def predict(prompt):
    global model, tokenizer, streamer
    messages = [{"role": "user", "content": prompt}]
    new_prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
    inputs = tokenizer(
            new_prompt,
            return_tensors="pt",
            truncation=True
        ).to(device)
    
    generated_ids = model.generate(
            inputs["input_ids"],
            max_new_tokens=340,
            num_return_sequences=1,
            do_sample=True,
            attention_mask=inputs["attention_mask"],
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            streamer=streamer,
            top_p=top_p,
            temperature=.8
        )
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


def predict2(prompt):
    global model, tokenizer, streamer
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

# if __name__ == '__main__':
#     print(predict2("Hello, how are you?"))

import flask
import json
app = flask.Flask(__name__)

@app.route('/<modelName>/<question>', methods=['POST'])
def get_answer(modelName, question):
    print(modelName, question)
    answer = predict2(question)
    print(Fore.GREEN , answer, Fore.RESET)
    dt=json.dumps({'question':question,'answer':answer})
    with open('replyHistory.txt','a') as f:
        f.write(dt)
    return flask.jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)