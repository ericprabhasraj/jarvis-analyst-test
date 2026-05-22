import pandas as pd

loaded_data = {}
current_file = None

def load_file(filepath):
    global current_file
    try:
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
            df = pd.read_excel(filepath)
        else:
            return "Unsupported file type. Use CSV or Excel."
        
        current_file = filepath
        loaded_data['df'] = df
        return f"File loaded successfully. {df.shape[0]} rows and {df.shape[1]} columns found."
    except Exception as e:
        return f"Error loading file: {str(e)}"

def get_data_summary():
    if 'df' not in loaded_data:
        return "No file loaded yet."
    
    df = loaded_data['df']
    summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}
Column Names: {', '.join(df.columns.tolist())}
Missing Values: {df.isnull().sum().sum()}
Numeric Columns Summary:
{df.describe().to_string()}
"""
    return summary

def get_context_for_ai():
    if 'df' not in loaded_data:
        return "No data loaded."
    
    df = loaded_data['df']
    sample = df.head(5).to_string()
    summary = get_data_summary()
    return f"Sample Data:\n{sample}\n\nSummary:\n{summary}"