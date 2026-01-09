# The Risk Index of Albania in the 2010s
<img width="266" height="190" alt="image" src="https://github.com/user-attachments/assets/e668f152-fede-49cc-ad07-9c62b9839203" />
 
## Project Overview
This project constructs a composite economic risk index for Albania from 2010 to 2023, combining FX 

volatility, inflation changes, energy price shocks, and tourism trends. The index visualizes how 

these factors contributed to economic risk over time, highlighting key events such as the COVID-19 

pandemic.

<div style="display: flex; gap: 40px; align-items: flex-start; margin-top: 30px;">

  <!-- LEFT: Main project content -->
  <div style="flex: 2;">

    <h2>Features</h2>
    <ul>
      <li><strong>Multi-Source Data Integration:</strong> FX, inflation, oil, and tourism data</li>
      <li><strong>Risk Factor Engineering:</strong> Returns, volatility, and z-scores</li>
      <li><strong>Composite Risk Index:</strong> Equal-weighted standardized risks</li>
      <li><strong>Time-Series Analysis:</strong> 2010–2023 trend comparison</li>
      <li><strong>Visualization:</strong> Clear risk dynamics over time</li>
    </ul>

  </div>

  <!-- RIGHT: Context panel -->
  <div style="
    flex: 1;
    background: #f7f7f7;
    padding: 20px;
    border-radius: 10px;
    line-height: 1.6;
  ">

    <h3>Why This Risk Index Matters</h3>
    <p>
      Albania is a small open economy exposed to external shocks such as energy prices,
      exchange-rate movements, and tourism demand. A composite index captures how
      these risks interact rather than viewing them in isolation.
    </p>

    <h3 style="margin-top: 20px;">Methodology Summary</h3>
    <p>
      Each indicator is converted into a volatility-based risk measure and standardized
      using z-scores so all risks are comparable on the same scale.
    </p>

    <h3 style="margin-top: 20px;">Limitations</h3>
    <ul>
      <li>Equal weighting assumes identical risk importance</li>
      <li>Annual data smooths short-term shocks</li>
      <li>Structural risks are not included</li>
    </ul>

  </div>

</div>

1. This code loads the EUR/ALL exchange-rate data, cleans and converts the price and date columns, then computes returns, rolling volatility, and a standardized (z-score) FX risk factor to quantify exchange-rate risk over time.
<img width="517" height="161" alt="Screenshot 2025-12-23 at 9 58 27 PM" src="https://github.com/user-attachments/assets/824a5b59-01b5-48af-8045-c07f23328dc2" />


2. This code resamples each dataset to yearly frequency, calculates the annual volatility (standard deviation of returns), and then converts that volatility into standardized risk factors using z-scores so all risks are comparable on the same scale.
<img width="706" height="126" alt="Screenshot 2025-12-23 at 10 39 47 PM" src="https://github.com/user-attachments/assets/94822a95-932f-444e-bd8a-d271d238f078" />


3. This code merges the yearly FX, inflation, oil, and tourism risk factors into one table by year, converts the year into a date format, and then computes Albania’s overall Risk Index as the average of all four standardized risk factors.
<img width="652" height="156" alt="Screenshot 2025-12-23 at 10 40 46 PM" src="https://github.com/user-attachments/assets/0aa0f05c-c0fa-4cf0-bfab-63e2659172c7" />


4. This code creates a line chart of Albania’s Risk Index over time, marks the start of COVID in 2020 with a vertical line, labels and styles the plot, and sets the y-axis to move in 0.1 increments so small changes in risk are easier to see.
<img width="613" height="181" alt="Screenshot 2025-12-23 at 10 41 08 PM" src="https://github.com/user-attachments/assets/8811319e-f704-45bd-b31e-4ffad8348650" />

## Index Risk Graph
<img width="1200" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/2d6f96c1-b6cc-488a-bfd4-bc9e38475280" />
- 2010-2012: Gradual Decline
  
     FX: Stable Euro/Albanian Lek exchange rate with low volatility
  
     Oil: No major energy price shocks
  
     Inflation: Moderate and predictable
  
     Tourism: Stable growth
  
- 2013-2014:
  
     FX & Inflation: Increase in volatility
  
     Oil: Stable but increasing prices
  
     Tourism: Consistent increase
  
- 2015:
  
     FX: Increased volatility due to oil prices and the Greek Debt Crisis
  
     Oil: Global oil price collapse increases energy volatility
  
     Inflation: Deflationary pressures raise uncertainty
  
     Tourism: Still stable which partially offset the risk index against the others
  
- 2016-2017:
  
     FX, Oil & Inflation: Prices stabilize and volatility is reduced
  
     Tourism: Strong growth
  
- 2018-2019:
  
     FX: Little volatility
  
     Oil: Gradual price increase
  
     Inflation: Contained
  
     Tourism: Strong growth
  
- 2020:
  
     FX, Oil, & Inflation: Increased uncertainty due to Covid 19 and price volatility
  
     Tourism: Collapse due to quarantine rules and border control
  
- 2021:
  
     FX: Partial recovery and lower volatility
  
     Oil: Sharp rise in prices
  
     Inflation: Increase across Europe
  
     Tourism: Begins to rebound
  
- 2022:
  
     FX: Stable
  
     Oil: Still high volatility due to the Russia-Ukraine War
  
     Inflation: Peaks
  
     Tourism: Strong recovery lwoering the risk index
  
- 2023:
  
     FX: Little volatility
  
     Oil: Uncertain due to geopolitical issues
  
     Inflation: Significant decrease
  
     Tourism: Strong performance



