import runpy
from pathlib import Path

current_path = Path(__file__).resolve()
base_dir = current_path.parent

print("여기" , base_dir)

print("Running user_profile.py ...")
runpy.run_path(str(base_dir /"user_profile.py"))

print("Running analysis.py ...")
runpy.run_path(str(base_dir /"analysis.py"))

print("Running report_mk.py ...")
runpy.run_path(str(base_dir /"report_mk.py"))

print("✅ All scripts executed successfully.")
