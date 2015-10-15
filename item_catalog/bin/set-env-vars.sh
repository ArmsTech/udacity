#!/bin/bash
#
# Set all environment variables (using defaults)
# Use `source` to run this script

ENV_FILE="./.env"

for env in $(cat "${ENV_FILE}"); do
  export "${env}"
done
