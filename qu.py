from sys import argv
class modelnameandpklfile:
    name=''
    pklfile=''


import time


import torch
import numpy as np
#from modelscope import snapshot_download, AutoTokenizer
from peft import LoraConfig, TaskType, get_peft_model
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
import os
import pandas as pd
import json
import pandas as pd
import torch
from datasets import Dataset
#from modelscope import AutoTokenizer
from peft import LoraConfig, TaskType, get_peft_model
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
import torch.nn as nn
import torch.quantization

import os

from datasets import Dataset
import dill as pickle

print(torch.cuda.is_available())

model=pickle.load(open('2.pkl', 'rb'))
tokenizer=pickle.load(open('tokeniser.pkl', 'rb'))

model.train()
quantized_model = torch.quantization.quantize_dynamic(model, {nn.Linear}, dtype=torch.qint8)


def predict(messages, model, tokenizer):
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


#have a try
messages = ["Hello, how are you?"]
print(predict(messages, quantized_model, tokenizer))
