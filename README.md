# Phi-2 Module: A Guide for Lilypad Integration

This documentation provides detailed instructions on how to integrate and use the Phi-2 module with Lilypad technology. The Phi-2 module, as an example, can be explored further on [Hugging Face](https://huggingface.co/amgadhasan/phi-2).

A practical demonstration of this module is available in a demo video on [YouTube](https://x.com/Lilypad_Tech/status/1737685808860274820?s=20).

## Steps to Replicate on Lilypad

### Preparing the Environment
1. **Clone the Repository**: Ensure that you are in the project directory after cloning the repository from GitHub.
2. **Set Up Private Key**: Export your private key using the following command: 
   ```bash
   export WEB3_PRIVATE_KEY="YOUR-PRIVATE-KEY"
3. **Docker Setup:** With Docker installed and the image available locally, you can run the model on your machine.
4. **Running the Module Locally** Use the following command to run the model locally:

5. ```bash
   docker run --gpus all -t clone-phi2 "what is the acceleration of earth's gravity?" 
You can use your own prompt of course

   ![Screenshot from 2024-01-08 23-37-14](https://github.com/Lilypad-Tech/module-phi2/assets/30084404/929da04b-549a-49d1-ae50-59b126c4906f)

## Running on Lilypad

To execute the module using Lilypad, follow these instructions:

6. **Module Configuration**: Configure the module with the following command:
```bash
lilypad run --module-repo "http://github.com/noryev/clone-phi2" --module-hash ae7b9f267287045cb81b59bae767cfb92e43c7d7 --module-path ./lilypad_module.json.tmpl -i Prompt="what is the acceleration of gravity on earth?"
```
### Execution Result:

After running the below command, you will receive the output. Below is a screenshot demonstrating this step:
Running on Lilypad

![Screenshot from 2024-01-08 23-33-50](https://github.com/Lilypad-Tech/module-phi2/assets/30084404/969194ce-0680-4b7d-a8cb-7f71b7954c00)





