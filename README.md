# Economic Dashboard

This project retrieves economic data, stores it in a SQLite database, and visualizes it using a Dash dashboard.

# Motivation

My motivation behind this project is to deploy the CBL-Index (Conference Board Leading Index) in a more engaging way, allowing me to track the economic health of various countries. Additionally, I aim to identify investment opportunities in niche markets amidst fears of an impending recession in the coming months. However, if the US Federal Reserve decides to lower interest rates, this project might not come to fruition.

* The majority of the calculations will be based on the following article: [Comprehensive Benchmark Revisions for The Conference Board Leading Economic Index® for the United States]( https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1979803)
* The use-cases will be :  Sweden, Mexico, New Zealand and Thailand

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run Application
    ```bash
   python app.py

> The dashboard will be available at http://127.0.0.1:8050.


### Explanation

- **`app.py`** integrates the different components.
- **`fetch_data.py`** retrieves economic data using an API.
- **`database.py`** stores the data in a SQLite database.
- **`trend_analysis.py`** performs basic trend analysis and generates comments.
- **`dashboard.py`** creates a Dash-based dashboard with data visualizations.
- **`update_scheduler.py`** uses the `schedule` library to automate data updates.

This project provides a dynamic way to track economic indicators with periodic updates, storage, and visual analysis.

### Project Structure
```commandline
economic_dashboard/
│
├── app.py                   # Main application
├── data/
│   └── fetch_data.py        # Script to fetch and process data from API
├── db/
│   ├── database.py          # SQLite connection and data storage
│   └── economy_data.db      # SQLite database
├── analysis/
│   └── trend_analysis.py    # Script to analyze trends and generate comments
├── visualization/
│   └── dashboard.py         # Dash app to visualize data
├── scheduler/
│   └── update_scheduler.py  # Script for scheduled data updates
├── requirements.txt         # Required Python packages
└── README.md                # Project description and setup instructions

```
