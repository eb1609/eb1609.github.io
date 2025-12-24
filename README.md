# The Risk Index of Albania in the 2010s
<img width="266" height="190" alt="image" src="https://github.com/user-attachments/assets/e668f152-fede-49cc-ad07-9c62b9839203" />
 
## Project Overview
This project constructs a composite economic risk index for Albania from 2010 to 2023, combining FX 

volatility, inflation changes, energy price shocks, and tourism trends. The index visualizes how 

these factors contributed to economic risk over time, highlighting key events such as the COVID-19 

pandemic.

## Features

- **Multi-Source Data Integration**: Combines foreign exchange rates, inflation (CPI), energy prices (oil), and tourism data into a unified dataset.
- **Risk Factor Engineering**: Computes returns, rolling volatility, and standardized (z-score) risk factors for each economic indicator.
- **Composite Risk Index**: Constructs an aggregate Albania Economic Risk Index by averaging normalized risk factors across sectors.
- **Time-Series Analysis**: Tracks economic risk trends from 2010 to 2023, enabling comparison across normal periods and crisis events (e.g., COVID-19).
- **Data Cleaning & Transformation**: Handles inconsistent formats, missing values, and mixed-frequency data using pandas and NumPy.
- **Visualization**: Generates clear time-series plots to illustrate shifts in economic risk over time.


1. This code loads the EUR/ALL exchange-rate data, cleans and converts the price and date columns, then computes returns, rolling volatility, and a standardized (z-score) FX risk factor to quantify exchange-rate risk over time.
<img width="517" height="161" alt="Screenshot 2025-12-23 at 9 58 27 PM" src="https://github.com/user-attachments/assets/824a5b59-01b5-48af-8045-c07f23328dc2" />


2. This code resamples each dataset to yearly frequency, calculates the annual volatility (standard deviation of returns), and then converts that volatility into standardized risk factors using z-scores so all risks are comparable on the same scale.
<img width="706" height="126" alt="Screenshot 2025-12-23 at 10 39 47 PM" src="https://github.com/user-attachments/assets/94822a95-932f-444e-bd8a-d271d238f078" />


3. This code merges the yearly FX, inflation, oil, and tourism risk factors into one table by year, converts the year into a date format, and then computes Albania’s overall Risk Index as the average of all four standardized risk factors.
<img width="652" height="156" alt="Screenshot 2025-12-23 at 10 40 46 PM" src="https://github.com/user-attachments/assets/0aa0f05c-c0fa-4cf0-bfab-63e2659172c7" />


4. This code creates a line chart of Albania’s Risk Index over time, marks the start of COVID in 2020 with a vertical line, labels and styles the plot, and sets the y-axis to move in 0.1 increments so small changes in risk are easier to see.
<img width="613" height="181" alt="Screenshot 2025-12-23 at 10 41 08 PM" src="https://github.com/user-attachments/assets/8811319e-f704-45bd-b31e-4ffad8348650" />


