# Weather Data Visualization

This is a Flask-based web application that visualizes weather data (Rainfall, Temperature, Wind, etc.) from a CSV file (`final_cleaned_data.csv`) using Matplotlib and Pandas. The app extracts and processes data by year and month to generate multiple interactive graphs rendered in a web interface.

---

## Features

- Parses a CSV with weather data including Date, Rainfall, Temperature, Evaporation, Sunshine, and Wind Speed.
- Generates bar charts for:
  - Rainfall over 2008, 2009, and 2010.
  - Monthly Min/Max temperatures for 2008, 2009, 2010.
  - Evaporation, Sunshine, Wind Gust Speed, and Wind Speed (9 AM) for 2008.
- Uses Flask to serve graphs as base64-encoded images in an HTML template.
- Automatically extracts **months** from the Date column for group-wise analysis.

---

## Technologies Used

- **Python**
- **Flask**
- **Pandas**
- **Matplotlib**
- **HTML (Jinja templates)**

---

## File Structure

```
.
├── app.py                  # Main Flask app
├── cleaned_data.csv        # CSV file with weather data
├── templates/
│   └── index.html          # HTML page that displays graphs
└── static/                 # (Optional) For styling or custom scripts
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install flask pandas matplotlib
```

### 2. Make sure you have the `final_cleaned_data.csv` file in the project directory.

### 3. Run the App
```bash
python app.py
```

### 4. Open in Browser
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the visualizations.

---

## Sample Visualizations

- Rainfall over the years  
- Monthly Min and Max Temperatures  
- Wind and Evaporation Metrics  

---

## Note

- Ensure your `Date` column in the CSV file is in the format: `dd-mm-yy`.  
- You can customize the graphs and years in `app.py`.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---