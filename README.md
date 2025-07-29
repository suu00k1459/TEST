Folder Structure  
UNICEF/  
├── analysis_code                # code  
│   ├── user_profile.py         # environment setting  
│   ├── analysis.py             # analysis of data  
│   ├── report_mk.py            # generate report HTML  
│   └── run_project.py          # overall project execution details  
│  
├── raw_data/                   # raw_data from GitHub  
│   └── 01.rawdata/  
│       ├── On-track and off-track countries.xlsx  
│       ├── WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.xlsx  
│       └── GLOBAL_DATAFLOW_2018-2022.xlsx  
│  
├── results/                    # result documents  
│   ├── coverage_report.html    # report view  
│   └── image/                  # visualization images  
│       └── coverage_comparison.png  
│  
└── README.md  

How to run  
Run the file named `run_project.py` at:  
`UNICEF/analysis_code/`

How to view  
Check the file named `coverage_report.html` at:  
`UNICEF/results/`
