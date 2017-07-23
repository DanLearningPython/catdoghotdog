Cat, Dog, or HotDog?

Model: v1.2 - 07/17/2017

Created with a CNN using 37,923 images in 10 epochs (79.93% accuracy). Training data consisted mostly of well-lit images. Does not perform well when picture taken with hardwood background.

Copy catvdogvhotdog/settings_secret.py.dist to a new file catvdogvhotdog/settings_secret.py and fill in the parameters.

Create virtual environment for django and install dependencies.
```
virtualenv catdoghotdog_env
source catdoghotdog_env/bin/activate
python --version
pip install tflearn
pip install tensorflow
pip install django
pip install opencv-python

```
