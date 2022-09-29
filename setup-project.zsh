#! /usr/bin/env zsh

# Use all or just some of the below commands as needed.
# It is not guaranteed you can just run this script as is.
# You need Pyenv and Pyenv Virtualenv and need to be inside the project root.
# Then you might be able to use this entire script as is.
# I'm sure you will figure it out. :)

# 1. install latest Python 3. I'm using 3.10.6.
pyenv install 3.10.6

# 2. create the virtual environment using the name : ve.textblob
pyenv virtualenv 3.10.6 ve.textblob

# And now the ve.textblob virtual env should be active if all was done correctly.
# pip/python are now those within the VE.

# Always upgrade pip and setuptools in a fresh virtual environment. They always need it.
pip install --upgrade pip
pip install --upgrade setuptools

# Now we can install the modules we will need
pip install -r requirements.txt

# At this point, the textblob module should be in place, so we can use it to download the corpora.
python -m textblob.download_corpora lite

# TODO: Find out where it puts the stuff.

