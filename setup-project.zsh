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
# As of Sep 2022, this was about 82 MB total. 4 different data packages downloaded.
# This will create a directory in the user's home directory: ~/nltk_data
python -m textblob.download_corpora lite

# ** Be sure to set the correct project interpreter in your IDE. I use PyCharm and it has just a little bit of
# trouble automatically finding the right interpreter, but after a little fiddling I can manually set it.
# IntelliJ IDE teams, please make your amazing IDEs I use and love so much full compatible with Pyenv and
# Pyenv Virtualenv. :)
# This is the path I set it to on my Mac. It took a few tries because the IDE even unhelpfully translated
# the final symlink, which was incorrect, but on the second try it accepted the path I entered:
# /Users/your_username/.pyenv/versions/ve.textblob/bin/python

