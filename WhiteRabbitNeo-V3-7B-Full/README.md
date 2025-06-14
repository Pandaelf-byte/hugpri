---
license: apache-2.0
base_model: Qwen/Qwen2.5-Coder-7B
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- code
- qwen-coder
- cybersecurity
- devops
---

<br>

# WhiteRabbitNeo

<br>

![WhiteRabbitNeo](https://huggingface.co/WhiteRabbitNeo/WhiteRabbitNeo-V3-7B/resolve/main/whiterabbitneo-logo-defcon.png)

WhiteRabbitNeo is a model series that can be used for offensive and defensive cybersecurity. Access at [whiterabbitneo.com](https://www.whiterabbitneo.com/) or go to [Kindo.ai](https://www.kindo.ai/) to create agents.

# Community

Join us on [Discord](https://discord.gg/8Ynkrcbk92)


# Technical Overview

WhiteRabbitNeo is a finetune of [Qwen2.5-Coder-7B](https://huggingface.co/Qwen/Qwen2.5-Coder-7B/), and inherits the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 7.61B
- Number of Paramaters (Non-Embedding): 6.53B
- Number of Layers: 28
- Number of Attention Heads (GQA): 28 for Q and 4 for KV
- Context Length: Full 131,072 tokens
  - Please refer to [this section](#processing-long-texts) for detailed instructions on how to deploy Qwen2.5 for handling long texts.


## Requirements

We advise you to use the latest version of `transformers`.

With `transformers<4.37.0`, you will encounter the following error:
```
KeyError: 'qwen2'
```

## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "WhiteRabbitNeo/WhiteRabbitNeo-V3-7B"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "write a quick sort algorithm."
messages = [
    {"role": "system", "content": "You are WhiteRabbitNeo, created by Kindo.ai. You are a helpful assistant that is an expert in Cybersecurity and DevOps."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

### Processing Long Texts

The current `config.json` is set for context length up to 32,768 tokens.
To handle extensive inputs exceeding 32,768 tokens, we utilize [YaRN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.

For supported frameworks, you could add the following to `config.json` to enable YaRN:
```json
{
  ...,
  "rope_scaling": {
    "factor": 4.0,
    "original_max_position_embeddings": 32768,
    "type": "yarn"
  }
}
```

# License 

Apache-2.0 + WhiteRabbitNeo Extended Version

## WhiteRabbitNeo Extension to Apache-2.0 Licence: Usage Restrictions

```


# Terms of Use

By accessing and using this Artificial Intelligence (AI) model, you, the user, acknowledge and agree that you are solely responsible for your use of the model and its outcomes. You hereby agree to indemnify, defend, and hold harmless the creators, developers, and any affiliated persons or entities of this AI model from and against any and all claims, liabilities, damages, losses, costs, expenses, fees (including reasonable attorneys' fees and court costs) that may arise, directly or indirectly, from your use of the AI model.

This AI model is provided "as is" and "as available" without any warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The creators make no warranty that the AI model will meet your requirements or be available on an uninterrupted, secure, or error-free basis.

Your use of the AI model is at your own risk and discretion, and you will be solely responsible for any damage to computer systems or loss of data that results from the use of the AI model.

This disclaimer constitutes part of the agreement between you and the creators of the AI model regarding your use of the model, superseding any prior agreements between you and the creators regarding your use of this AI model.