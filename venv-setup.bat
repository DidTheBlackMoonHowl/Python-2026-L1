python -m venv .venv

call venv-active.bat

pip3 install --upgrade pip
:: pip install jupyterlab
:: pip install notebook
pip install numpy
pip install pandas
pip install windows-curses

call venv-deactive.bat