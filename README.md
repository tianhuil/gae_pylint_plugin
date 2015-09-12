# GAE-Pylint-Plugin
Based on @SpainTrain's https://gist.github.com/SpainTrain/b5d4689156f0190700ef

## Installation
To install, run
```
pip install git+https://github.com/tianhuil/gae_pylint_plugin.git#egg=gae_pylint_plugin
```

## Execution
Either add the following line to `pylintrc`:
```
load-plugins=gae_pylint_plugin
```
or append the following option to `pylint`:
```
pylint --load-plugins gae_pylint_plugin
```

## Changes
- more extensive list of GAE Property Definitions.
- pip installable

## Changes
- recognize repeated properties (e.g. `Instance of 'KeyProperty' has no 'append' memberE1`)
- recognize json members (e.g. `Instance of 'JsonProperty' has no 'get' member`)
