# scan-tumor-lite
This project covers the UI part of the scan-tumor ML platform provided by the
L, the S, the T and the J.
User will be able to upload a scanner image of a brain to know if there is a
tumor.

## Setup the project

cd ~/code/blarflelsouf \
git clone git@github.com:blarflelsouf/scan-tumor-lite.git \
cd scan-tumor-lite

## Setup virtual env
pyenv virtualenv 3.10.6 scan-tumor-lite \
pyenv local scan-tumor-lite

## How to test UI
\#Go to UI project repository and launch streamlit app via makefile instruction
cd ~/code/blarflelsouf/scan-tumor-lite
make streamlit

\# Go to main project repository and launch uvicorn web server
cd ~/code/blarflelsouf/Scan-tumor
uvicorn api.fastapi:app --reload
