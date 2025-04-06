
# BabyAI 1.1

BabyAI is a platform used to study the sample efficiency of grounded language acquisition, created at [Mila](https://mila.quebec/en/).

The master branch of this repository is updated frequently.  If you are looking to replicate or compare against the [baseline results](http://arxiv.org/abs/2007.12770), we recommend you use the [BabyAI 1.1 branch](https://github.com/mila-iqia/babyai/tree/dyth-v1.1-and-baselines) and cite both:

## Installation

### Conda 

```
git clone https://github.com/mila-iqia/babyai.git
cd babyai
conda env create -f environment.yaml
source activate babyai
```

The last command installs the repository in editable mode. Move back to the `babyai` repository and install that in editable mode as well.

```
cd ../babyai
pip install --editable .
pip install minigrid
