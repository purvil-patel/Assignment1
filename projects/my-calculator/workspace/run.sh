python3 -m venv myenv

source myenv/bin/activate

pip install -r requirements.txt

python controller.py

pytest test_calculator.py
