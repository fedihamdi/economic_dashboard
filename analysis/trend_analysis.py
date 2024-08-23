import pandas as pd

import pandas as pd


def analyze_trend(data):
    # Ensure that the 'Value' column is numeric
    data['Value'] = pd.to_numeric(data['Value'], errors='coerce')

    # Drop rows with NaN values in 'Value'
    data = data.dropna(subset=['Value'])

    if len(data) < 2:
        return "Not enough data to analyze."

    # Sort data by 'DateTime' to ensure the order is correct
    data = data.sort_values(by='DateTime')

    # Calculate the difference and mean difference
    data['diff'] = data['Value'].diff()

    # Drop NaN values that result from the diff operation
    data = data.dropna(subset=['diff'])

    trend = data['diff'].mean()

    return "positive" if trend > 0 else "negative"


def generate_comment(trend):
    if trend == "positive":
        return "The economic indicator is rising, indicating potential economic risks."
    elif trend == "negative":
        return "The economic indicator is decreasing, suggesting economic improvement."
    else:
        return "Unable to determine the trend."
