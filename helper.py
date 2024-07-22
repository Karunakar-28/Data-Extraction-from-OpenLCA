import olca_schema as o
import pandas as pd
import os


#******************************  get_all_process_id   **********************************************

def get_all_process_ids(client):
    """ Gets all process id's

    : param client: connection object to openLCA
    : return : list of all process id's
    """
    # Finding all the processes
    process_descriptor = client.get_descriptors(o.Process)

    # To store id's of all processes
    process_id_list = [process.id for process in process_descriptor] 

    return process_id_list


#******************************  extract_exchange_data   *****************************************

def extract_exchange_data(exchange):
    """ Returns a dataframe of values for a given exchange
    
    : param exchange: exchange object 
    : return : dataframe with values from exchange object
    """
    return pd.DataFrame({
                'Flow': [exchange.flow.name],
                'Category':[exchange.flow.category],
                'Amount': [exchange.amount],
                'Unit': [exchange.unit.name],
                'Costs/Revenues': [exchange.cost_value],
                'Cost Formula': [exchange.cost_formula],
                'Currency':[exchange.currency],
                'Uncertainity':[exchange.uncertainty],
                'Is avoided?' : [exchange.is_avoided_product],
                'Provider': [exchange.default_provider],
                'Data quality entry': [exchange.dq_entry],
                'Location': [exchange.location],
                'Description': [exchange.description]
            })


#******************************    createDF      ***************************************************

def createDF():
    """ Returns a empty dataframe with the header"""
    return pd.DataFrame({
                'Flow': [''],
                'Category':[''],
                'Amount': [''],
                'Unit': [''],
                'Costs/Revenues': [''],
                'Cost Formula': [''],
                'Currency':[''],
                'Uncertainity':[''],
                'Is avoided?':[''],
                'Provider': [''],
                'Data quality entry': [''],
                'Location': [''],
                'Description':[''] 
            })


#*******************************  create_path     ***************************************************

def create_path(path):
    """ Creates the path if it doesnot exist or ensures it exists if its already present
    
    : param path: directory path as string
    """

    try:
        os.makedirs(path, exist_ok=True)

    except Exception as e:
        print(f"An error occurred while path creation: {e}")


#******************************  get_all_data       *************************************************

def get_all_data(client, ids_list):
    """ Gets data from all process and stores them into excel sheets in respective folder
    
    : param client: connection object to openLCA
    : param ids_list: list of ids of all processes
    """
    # Directory to store the data
    path = '../Processes/'

    for process_id in ids_list:

        process = client.get(o.Process, process_id)

        exchanges = process.exchanges

        input_df = createDF()
        
        output_df = createDF()

        for exchange in exchanges:

            if exchange.is_input:
                #print(f"Input exchange containing process: {process.name}")
                input_df = pd.concat([input_df,extract_exchange_data(exchange)])
            else:
                output_df = pd.concat([output_df, extract_exchange_data(exchange)])

        # Path to the excel file
        total_path = path + process.category

        create_path(total_path)

        # Name of the excel file
        file_name = process.name + ".xlsx"


        try:
            create_excel_sheets(total_path, file_name, input_df, output_df)
        except Exception as e:
            print(f"Exception: Error while creating excel file {e}")

    

#******************************  create_excel_sheets   *******************************************


def create_excel_sheets(path, file_name, input_df, output_df):
    """ Creates an Excel file with input and output sheets respectively
    
    : param path: output path to the excel file
    : param file_name: name of the excel file
    : param input_df: inputs data of the process
    : param output_df: outputs data of the process
    """

    file_name = file_name.replace('\\','_')
    file_name = file_name.replace('/','_')

    excel_file_path = os.path.join(path,file_name)

    try:
        # Create ExcelWriter object
        with pd.ExcelWriter(excel_file_path) as writer:
            # Writing each DataFrame to a separate sheet
            input_df.to_excel(writer, sheet_name='Inputs', index=False)
            output_df.to_excel(writer, sheet_name='Outputs', index=False)
        
    except Exception as e:
        print(f"Exception occured while try to save file at :\n{excel_file_path}\n")
        print(f"Exception is : {e}")
        print(f"Is the path length below 260 characters: {within_path_limit(excel_file_path)}")
           

#******************************  check_path_limit   *******************************************

def within_path_limit(path):
    """Checks if the path exceeds the windows path limit
    
    : param path: relative path of the excel file
    : return : true if within limit, false if not 
    """

    cwd_path = os.getcwd()
    full_path = cwd_path + path

    path_length = len(full_path)

    if path_length >= 260:
        return False
    
    else:
        return True

       
            