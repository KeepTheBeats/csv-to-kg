# What is this repository?
This is the Assignment of AAU PhD course Knowledge Graphs in the era of Large Language Models, the "Option A: A system for Tabular Data to KG Matching" in the file `phd-course-kgs-aalborg-lab-session-3-matching.pdf`. 

# How to run this system?
1. Git clone this repository.
2. Create a Python venv, and activate it.
4. Execute `python -m pip install --upgrade pip setuptools wheel`.
5. Execute `python -m pip install -r requirements.txt` in the root path of this repository (using the `requirements.txt` in this repository).
5. Comment or uncomment the No. 86 and No. 87 lines in the file `csv_to_kg.py`, to specify the input csv file.
4. Execute `python -u csv_to_kg.py` in the root path of this repository, and the results (CEA and CTA) will be generated in the path `data/output`.

