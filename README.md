# Animal Planet Dashboard - Setup Guide

## Prerequisites

Make sure you have Python installed on your system (Python 3.7 or higher recommended).

## Step 1: Install Required Packages

Open your terminal/command prompt and install the necessary packages:

```bash
pip install dash plotly pandas numpy
```

## Step 2: Prepare Your Data

1. Download the `animals_info.csv` file from the Kaggle dataset
2. Place it in the same directory as your Python script
3. Ensure your CSV has these columns (the app will adapt to your actual column names):
   - `name`: Animal name
   - `class`: Animal class (Mammalia, Aves, Reptilia, etc.)
   - `habitat`: Where the animal lives (Forest, Ocean, Desert, etc.)
   - `diet`: What the animal eats (Carnivore, Herbivore, Omnivore)
   - `order`: Taxonomic order
   - `population`: Population count (numeric)

## Step 3: Save the Code

1. Copy the Python code provided
2. Save it as `animal_dashboard.py` in the same directory as your CSV file

## Step 4: Run the Application

1. Open terminal/command prompt
2. Navigate to the directory containing your files:
   ```bash
   cd path/to/your/directory
   ```
3. Run the application:
   ```bash
   python animal_dashboard.py
   ```

## Step 5: View the Dashboard

1. After running the script, you'll see output like:
   ```
   Dash is running on http://127.0.0.1:8050/
   ```
2. Open your web browser and go to: `http://127.0.0.1:8050/`
3. You should see your interactive dashboard!

## Dashboard Features

### Four Main Visualizations:

1. **Animals by Class**: Bar chart showing count of animals in each taxonomic class
2. **Animals by Habitat**: Bar chart showing distribution across different habitats  
3. **Animals by Diet**: Bar chart showing dietary preferences distribution
4. **Population by Order**: Interactive chart that can switch between:
   - Pie chart showing population percentages by taxonomic order
   - Line chart showing population trends by order

### Interactive Features:
- Toggle between pie chart and line chart for population data
- Hover over charts to see detailed information
- Responsive design that works on different screen sizes

## Troubleshooting

### If CSV file is not found:
- The app includes sample data and will run even without the CSV file
- Make sure `animals_info.csv` is in the same directory as the Python script
- Check that the filename matches exactly (case-sensitive)

### If you get import errors:
- Make sure all packages are installed: `pip install dash plotly pandas numpy`
- Try upgrading pip: `pip install --upgrade pip`

### If the app doesn't start:
- Check that no other application is using port 8050
- You can specify a different port by modifying the last line:
  ```python
  app.run_server(debug=True, port=8051)
  ```

### Column Name Issues:
If your CSV has different column names, modify the column references in the code:
- Replace `'class'` with your class column name
- Replace `'habitat'` with your habitat column name
- Replace `'diet'` with your diet column name
- Replace `'order'` with your order column name
- Replace `'population'` with your population column name

## Customization Options

### Change Colors:
- Modify `color_continuous_scale` parameters in the bar charts
- Options include: 'Viridis', 'Plasma', 'Inferno', 'Magma', 'Cividis'

### Adjust Chart Heights:
- Change the `height=400` parameter in the `update_layout()` calls

### Add More Chart Types:
- The population chart already demonstrates how to switch between chart types
- You can extend this pattern to other visualizations

## File Structure
```
your_project_folder/
├── animals_info.csv        # Your data file
├── animal_dashboard.py     # The dashboard code
└── README.md              # Optional: documentation
```

## Next Steps

Once you have the basic dashboard running, you can:
1. Add more chart types and visualizations
2. Include filtering capabilities
3. Add data summary statistics
4. Export charts as images
5. Deploy to a web server for sharing

The dashboard is designed to be simple yet comprehensive, similar to Streamlit but with the power and flexibility of Dash/Plotly!