
from pathlib import Path

# images path
logo = r"images\unicef_logo.jpg "
ANC4_average = r"images\ANC4_coverage_comparison.png"
SBA_average = r"images\SBA_coverage_comparison.png"  

# html 
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Coverage Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #1CABE2;"}}
        img {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <div style="display: flex; align-items:  flex-center;">
        <img src={logo} style="height: 60px; margin-right: 10px;">
        <h1>Unicef test report</h1>
    </div>
    <h2>Data Sources</h2>
    <p> 1.Status of achieving under-five mortality targets as of 2022 </p> 
    <p> 2. UN World Population Prospects, 2022 </p> 
    <p> 3. Antenatal care (ANC4) and skilled birth attendance (SBA) data </p> 

    <h2> Number of Records </h2>
    <p> * ANC4: 86 records </p> 
    <p> * SBA: 149 records </p> 


    <h2> Overview of Analysis </h2>
    <p> This analysis examines the differences in antenatal care coverage and skilled birth attendance rates based on whether a country has achieved the under-five mortality target as of 2022.
Population-weighted averages were calculated using the projected number of births in 2022 as weights.</p>


    <h2> SBA & ANC4 Coverage Report</h2>
    <img src="{ANC4_average}" alt="Coverage Chart">
    <img src="{SBA_average}" alt="Coverage Chart">


    <h2> Key Findings</h2>
    <p> 1. In countries that achieved the under-five mortality target, the proportion of women aged 15–49 who received at least four antenatal care visits (ANC4) was approximately 17.47 %p higher than in countries that did not. </p>
    <p> 2. In the same comparison, the proportion of deliveries attended by skilled health personnel (SBA) was approximately 23.81 % p higher in countries that achieved the target. </p>
    <p> 3. While frequent antenatal care visits play an important role in reducing under-five mortality, the larger difference observed in SBA coverage suggests that the presence of skilled birth attendants may have a greater impact than antenatal care alone.</p>

    <h3> - end - </h3>
</body>
</html>
"""

current_path = Path(__file__).resolve()
base_dir = current_path.parent


with open(str(base_dir / "../output/coverage_report.html"), "w", encoding="utf-8") as f:
    f.write(html_code)
