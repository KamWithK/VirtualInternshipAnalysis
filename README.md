# VirtualInternshipAnalysis
## Instalation and Environment
To simplify running code in a stable and consistant environment, we provide an `environment.yaml` file.
This file contains a list of essential packages (which certain version and channel specifications).
It is easiest to use the environment with Anaconda (or Miniconda for a smaller and more streamlined environment).


To install and use `environment.yaml` do the following:
1. Install Anaconda or Miniconda
2. Create a new environemtn from the file `conda env create -f environment.yaml`
3. When packages need to be added or modified update the `environment.yaml` file and run `conda env update -f environment.yaml --prune`
4. Once satisfied activate the new environment through `conda activate ct` and (optionally) deactivate/close afterwards with `conda deactivate`

*For an update the above isn't necessary - simply run `conda update --all` for packages and `conda update -n base -c defaults conda` for conda itself!*

## Developer Instructions
### Training Spacy Models
Run `python -m spacy train config/model.cfg` (where `model` is replaced by its name, like `tok2vec` or `transformer`)

### Tracking Experiments with Weights and Biases
To log your experiments to Weights and Biases, log into your account through the command `wandb login` using an [API key](https://app.wandb.ai/authorize).
Once you've done this you're ready to run your code.
Make sure to fill in all the information on the experiment (within the `config.json` file's `experiment_args` criteria):
* `name` - the name of the experiment (short and sweet)
* `id` - a unique string to represent the run (for resumability)
* `tags` - a list (like `["first tag", "second tag", "third tag"]`) of tags (stay consistant, so filtering and visualising works)
* `group` - a string to group multiple runs together
* `log_model` - whether to upload the model itself (can be slow post-run, so avoid whilst debugging)

**To resume a previous experiment, make sure to specify the `id` and model checkpoints path**!
You can find a previous run's id by looking at its url - *https://app.wandb.ai/kamwithk/ct-facial-reconstruction/runs/***ID**.
Remember that you can always add/modify any properties on the [Weights and Biases Dashboard](https://app.wandb.ai/monash-deep-neuron/ct-facial-reconstruction) during and after a run.
