# Capital-Bikeshare-Ride-Analysis

Capital Bikeshare (also abbreviated CaBi) is a bicycle-sharing system that serves Washington, D.C., and certain counties of the larger metropolitan area.

**Overview**: Exploratory Data Analysis (EDA) of ride-sharing data for the Capital Bikeshare system in Washington, D.C. The goal was to translate raw operational data into actionable intelligence on rider behavior, inventory management, and system efficiency.

This analysis is relevant for city planners and operational managers focused on logistics, supply-chain, and service delivery optimization.

---

## 🔑 Key Insights & Operational Recommendations

* **Usage Profile**: A clear division exists between `member` (commuter) and `casual` (tourist/leisure) riders. **Members** dominate weekday morning/evening rush hours, focusing on short, high-turnover trips, while **Casual** riders dominate weekend/holiday midday usage with longer average ride durations.
* **Peak Demand Window**: The network experiences its highest logistical strain on **Friday evenings (4:00 PM – 6:00 PM)**, indicating a peak in leisure travel combined with the commuter exodus. This window requires prioritized inventory rebalancing (trucking bikes to empty stations).
* **Inventory Management**: Analysis of station-level usage revealed the **Top 5 most popular start stations** that exhibit frequent periods of bike depletion, requiring predictive modeling for real-time fleet redistribution efforts.
* **Recommendation**: Implement a dynamic pricing model based on station inventory levels during peak commuting times to incentivize dropping bikes at depleted stations.

---

## 🛠️ Technical Stack & Project Components

* **Methodology**: Data cleaning, feature engineering (e.g., adding `day_of_week`, `hour_of_day`), time-series aggregation, and visualization of demand curves and spatial usage patterns.
* **Tools**: Python (Pandas for data transformation, Matplotlib/Seaborn for visualization, NumPy for data simulation).
* **Data**: ~20,000 simulated ride records spanning two months, mimicking the real-world operational schema.

| File / Folder | Description |
| :--- | :--- |
| `notebooks/` | Contains the core Jupyter Notebook (`David_Ortiz_M5_Capital_Bikeshare_Ride_Analysis.ipynb`). |
| `generate_data.py` | Python script to programmatically create the runnable CSV file (`bikeshare_trips_simulated.csv`), ensuring reproducibility. |
| `requirements.txt` | Lists all necessary Python dependencies (Pandas, Matplotlib, etc.). |

## ▶️ How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/capital-bikeshare-analysis.git](https://github.com/your-username/capital-bikeshare-analysis.git)
    cd capital-bikeshare-analysis
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Generate Data Files:**
    ```bash
    python generate_data.py
    ```
4.  **Launch Analysis:** Open the Jupyter Notebook in the `notebooks/` folder to view the full analysis.

---
