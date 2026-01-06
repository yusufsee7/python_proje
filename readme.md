<!-- Project Description -->

In this project, the 24-hour passenger density of the M7 metro line is analyzed.
The goal is to understand passenger density during the day, find peak hours, and detect unusual situations using simple data analysis methods.

<!-- Dataset -->

The dataset is in CSV format and represents hourly passenger counts for the M7 metro line.

<!-- Columns -->
• hour: Hour of the day (0–23)
• route: Metro line name (M7)
• passenger_count: Estimated number of passengers per hour

The data is created in a realistic way:

• Morning (07–09) and evening (17–19) hours are crowded
• Night hours have low passenger density

<!-- Web Data Collection and Cleaning -->

The dataset is assumed to be collected from a public transportation website.

The following steps were applied to prepare the data:

• Web data was converted into CSV format.
• Missing passenger values were removed.
• Non-numeric values were converted to numeric values.
• Hour values were standardized between 0 and 23.
• Only M7 metro line data was used in the analysis.

<!-- Data Analysis -->

The following simple analyses were performed:

• Average passenger count
• Hour with the highest passenger density
• Maximum passenger count
• Statistical summary (minimum, maximum, mean, quartiles)

These analyses help understand daily passenger patterns on the M7 metro line.

<!-- Anomaly Detection -->

Anomaly detection was performed using the IQR (Interquartile Range) method.

• Q1 and Q3 values were calculated.
• Passenger counts outside the normal range were marked as anomalies.

This helps identify unusual passenger density at certain hours.

<!-- Visualization -->

The project uses Matplotlib and Seaborn for visualization.

The following charts were created:

• Bar chart showing passenger density by hour
• Boxplot showing passenger count distribution and anomalies

<!-- Technologies Used -->

• Python
• Pandas
• Matplotlib
• Seaborn

<!-- How to Run the Project -->

Open the terminal in the project folder and run:

• python3 m7_24hours_density.py


<!-- Results -->

• The results show that:
• Passenger density is highest during morning and evening hours
• Passenger count is low during night hours
• Some hours show unusual (anomalous) passenger density