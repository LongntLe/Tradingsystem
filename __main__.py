from __future__ import absolute_import
import logging.config, yaml
from src.trading import main

with open('logging.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)

main()
