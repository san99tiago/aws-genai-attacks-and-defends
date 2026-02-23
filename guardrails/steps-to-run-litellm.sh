#!/bin/bash

# Last example is with LiteLLM... Here are the steps to replicate.

# 1) Install the python dependencies
# (at the root of the repo)
pip install -r requirements.txt

# 2) Terminal 1 / Initialize the LiteLLM Proxy
export LITELLM_MASTER_KEY=santi-1234
litellm --config guardrails/config.yaml --detailed_debug

