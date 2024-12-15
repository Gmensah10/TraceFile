# TraceFile
TraceFile is a digital forensics and incident response (DFIR) tool that enables you to quickly generate, analyze, and visualize forensic timelines from file system metadata.

This project simplifies file metadata collection, including creation, modification, and access timestamps, providing a user-friendly way to create forensic timelines.

# What is TraceFile?
TraceFile is a Python-based forensic timeline generator designed to assist in analyzing file metadata from the specified directory.

**The following features are supported by TraceFile:**

Collect file metadata including creation time, modification time, last access time
Filter out data based on date and file type in order to target only the relevant files
Save this timeline in a CSV format for more detailed analysis
Visualize this timeline as a scatter plot for fast insight into active files

**How TraceFile Works:**

TraceFile scans a directory and collects metadata about its files, including timestamps, to produce a detailed timeline.

**With one command, you can:**

Generate a CSV timeline file for offline review.
Visualize the timeline in a graphical format for presentations or investigations.

# Why Use TaceFile?
TraceFile automates digital forensic investigation by generating and visualizing timelines, saving hours of manually doing so. 

**It's helpful for the following:**

Incident Response: Quickly identify file activity during a breach window.
Forensic Analysis: Building detailed timelines for evidence presentation.
Research: File system behavior analysis for experiments or audits.

# Why Use TraceFile 
TraceFile streamlines digital forensic investigations by automating timeline generation and visualization, saving hours of manual effort. It is particularly useful for:

Incident Response: Quickly identifying file activity during a breach window.
Forensic Analysis: Building detailed timelines for evidence presentation.
Research: Analyzing file system behavior for experiments or audits.

# Features
**Timeline Generation:** Collects file creation, modification, and access timestamps.
**Date Filtering:** Filters files by creation date for targeted timelines.
**File Type Filtering:** Includes or excludes specific file types for precision.
**CSV Export:* Saves the timeline in CSV format for offline analysis.
**Visualization:** Creates an intuitive scatter plot of file activity.

# Installaion
TraceFile requires Python and is easy to install and set up.

**Step 1: Install Matplotlb**
```bash
pip install matplotlib
```
# Usage
You can start using TraceFile with this argument for example:
```bash
python tracefile.py test_data output.csv --start_date 2024-01-01 --end_date 2024-12-31 --file_types .txt
```

# Requirements
Python
Libraries: os, csv, argparse, matplotlib, and datetime.

# Contributing
Contributions are welcome! If you'd like to improve this tool, please fork the repository, make changes, and submit a pull request. For major changes, please open an issue to discuss what you'd like to change.

# License
This project is licensed under the MIT License.

# Acknowledgements
TraceFile was inspired by the need for efficient and user-friendly forensic timeline generation. Special thanks to the open-source community for their tools and resources.
