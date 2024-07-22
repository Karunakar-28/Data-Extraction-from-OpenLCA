# Data Extraction from OpenLCA

This tool is designed to extract input and output data of all processes from an OpenLCA database. 

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Instructions](#instructions)

## Introduction

This OpenLCA Exchange Data Extraction tool addresses the challenge of extracting input and output data for all processes from an OpenLCA database. While OpenLCA software provides an export option to access this data in Excel workbooks, manually exporting data for each process and organizing the files into their respective categories can be time-consuming and tedious. This tool automates the process, quickly gathering the input and output data and saving it into appropriately categorized folders, significantly reducing the time and effort required.

## Requirements

To use the this data extractor, ensure you have the following tools and libraries installed:

- **OpenLCA**: The primary software for life cycle assessment.
- **Code Editor**: Visual Studio Code (VSCode) is preferred for editing and running the code.
- **Python 3.x**: The programming language used for the script.
- **pandas**: For data manipulation and analysis.
- **openpyxl**: For Excel file operations.
- **os**: For file path operations.
- **olca_ipc (v2.0.2)**: For inter-process communication with OpenLCA.
- **olca_schema (v0.0.12)**: For working with OpenLCA data schemas.


## Instructions   

1. Open OpenLCA and Start the IPC Server

    * Open OpenLCA and ensure your desired database is open.
    * Navigate to Tools > Developer Tools, then click on **"IPC server"**.
    * A pop-up window will appear displaying a port number. Ensure this port number matches the one specified in the code.
    * Click the green button in the pop-up window to start the server.
    * Important: Do not close the pop-up window; simply minimize it.  
      
2. First-Time Setup

    * Ensure Python is installed on your system. You can download it from the official Python website.
    * Open the Visual Studio Code (VSCode) editor and open the folder containing the code files (named DatafromOpenLCA).
    * Open the terminal by clicking Terminal in the menu bar and then selecting New Terminal.
    * In the terminal, type the following command and press Enter:
    ```sh
    pip install -r requirements.txt
    ```
    This command will install all the necessary Python libraries required to run the program.

3. Running the Program

    * Every time you need to run the program, open the terminal in VSCode.
    * Navigate to the folder containing the code files (DatafromOpenLCA).
    * In the terminal, type the following command and press Enter:
    ```sh
    python main.py
    ```
   *  If the program runs successfully, you will see a message saying "Data collection completed..." in the terminal.
   * A new folder named **Processes** will be created in the same location as the folder containing the code files (DatafromOpenLCA).  

4. Viewing the Results

    * Open the Processes folder created by the tool to view the Excel files containing the input and output data for each process.
    * Each file will be named according to its respective category, making it easy to find the data you need.










































