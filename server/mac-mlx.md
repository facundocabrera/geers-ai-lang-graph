## Model Sources

### Important model sources

https://huggingface.co/nvidia
https://huggingface.co/mistralai
https://huggingface.co/microsoft
https://huggingface.co/meta-llama
https://huggingface.co/hugging-quants
https://huggingface.co/mlx-community

### Hugging Face CLI

To download models to experiment it is highly recommended to use the Hugging 
Face CLI.

```bash
brew install huggingface-cli
```

Or:

```bash
mkdir ai-models
cd ai-models
python3.10 -m venv .venv
source .venv/bin/activate
pip install huggingface-hub
```

```bash
huggingface-cli login
huggingface-cli download repo_id filenames
```

## MLX Server

Install the server:

```bash
pip install mlx mlx-lm
mlx_lm.server --model mlx-community/Llama-3.2-3B-Instruct-4bit
```

List available models on the server:

```bash
curl localhost:8080/v1/models -H "Content-Type: application/json"
```

Test the server:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="sk-xxx")

# replace the model with the name from the list of models to choose
response = client.chat.completions.create(
    model="mlx-community/Llama-3.2-3B-Instruct",
    # the messages format differ from langchain
    messages=[{"role": "user", "content": "Say this is a test!"}],
)

print(response)
```

```bash
python server/test-local-server.py
```