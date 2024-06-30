# Simple ai chat bot (work in progress)

This repository contains the code for a simple AI-based chat bot built using the Ollama framework and the LLaMA model. The chat bot leverages the capabilities of large language models to engage in natural language conversations, providing responses that are contextually relevant and coherent.

## Features
- **Interactive Chat Interface**: Communicate with the AI chat bot through a user-friendly interface.
- **Advanced Language Understanding**: Utilizes the LLaMA model for sophisticated language comprehension and generation.
- **Customizable Responses**: Modify the bot’s behavior and responses by adjusting model parameters and training data.
- **Scalable Architecture**: Built to handle multiple users and concurrent conversations efficiently.

## Note
This code requires some modules:
- `ollama`
- `llama3`
- CUDA (for NVIDIA GPUs)

### Installation Guide for Windows:
1. Download and install Ollama from [here](https://ollama.com/download/windows).
2. Wait for the process to complete.
3. Open Windows PowerShell and paste the command:
    ```shell
    ollama run llama3
    ```
4. Wait for the process to complete.

Note: For any additional models using Ollama, only the command for Windows PowerShell needs to change. For example, to use the Mistral model, the PowerShell command would be:
  ```shell
  ollama run mistral
  ```
The Python code will also need to be modified accordingly to use Mistral instead of LLaMA3. This process is similar for models that interpret images, like LLaVA.

4. Install CUDA from [here](https://developer.nvidia.com/cuda-downloads) and follow the instructions.

## Important
These models have significant GPU demands, and not all GPUs are supported by Ollama. Please refer to the [list of supported GPUs](https://github.com/ollama/ollama/blob/main/docs/gpu.md).

Feel free to fork this repository and adapt it to your needs. Happy chatting!

