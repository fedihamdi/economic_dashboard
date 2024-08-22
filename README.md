# Economic Dashboard

This project retrieves economic data, stores it in a SQLite database, and visualizes it using a Dash dashboard.

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