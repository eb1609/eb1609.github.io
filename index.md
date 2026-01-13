<div style="text-align: center; margin-bottom: 30px;">
  <h1>The Risk Index of Albania in the 2010s</h1>

  <img
    src="https://github.com/user-attachments/assets/e668f152-fede-49cc-ad07-9c62b9839203"
    alt="Albania Flag"
    style="
      width: 220px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
      margin-top: 12px;
    "
  />
</div>

## Project Overview
This project constructs a composite economic risk index for Albania from 2010 to 2023, combining the 
foreign exchange of the Euro and the Albanian Lek, inflation changes, energy price shocks, and tourism 
trends. The index visualizes how these factors contributed to economic risk over time, highlighting key
events such as the COVID-19 pandemic.

<div style="display: flex; gap: 40px; align-items: flex-start; margin-top: 30px;">

  <!-- LEFT: Main project content --> 
  <div style="flex: 2;">

    <h2>Features</h2>
    <ul>
      <li><strong>Multi-Source Data Integration:</strong> Integrated macroeconomic data from multiple sources and aligned all datasets together in frequency, scale, and formatting. </li>
      <li><strong>Risk Factor Engineering:</strong> These raw indicators were converted into relevant measures rather than used individually. Computed returns and changes are reflected as fluctuations shown in the graph and analysis. </li>
      <li><strong>Composite Risk Index:</strong> Individual risk factors are standardized using z-scores to allow direct comparison across variables. </li>
      <li><strong>Time-Series Analysis:</strong> The comparison spans from 2010 - 2023 showing periods of stability and crisis portraying the scale of major world events like the global oil price collapse or the the Covid 19 pandemic. </li>
      <li><strong>Visualization:</strong> Clear risk dynamics over time with appropriate scaling to communicate changes through the period. </li>
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
      Albania is a small economy highly exposed to external shocks such as oil prices,
      exchange-rate movements, and tourism demand. I created a composite index to capture 
      the scale of these risks interact and their interactions as a whole.
    </p>

    <h3 style="margin-top: 20px;">Methodology Summary</h3>
    <p>
      Each indicator is weighed the same and converted to 
      a z-score so all risks are comparable on the same scale.
    </p>

    <h3 style="margin-top: 20px;">Limitations</h3>
    <ul>
      <li>Equal weighting assumes identical risk importance</li>
      <li>Annual data ignores short-term shocks</li>
      <li>Structural risks are not included</li>
    </ul>

  </div>

</div>

  1) This code loads the EUR/ALL exchange rate data, cleans and converts the price and date columns, then computes returns, rolling volatility, and a standardized z-score to quantify exchange rate risk over time.
   
<img width="517" height="161" alt="Screenshot 2025-12-23 at 9 58 27 PM" src="https://github.com/user-attachments/assets/824a5b59-01b5-48af-8045-c07f23328dc2" />


  2) This code manipolates each dataset to yearly frequency, calculates the standard deviation of returns (volatility), and then converts that volatility into standardized risk factors so all risks are comparable on the same scale. Tourism uses a different method because two different sources were used and merged.
   
<img width="706" height="126" alt="Screenshot 2025-12-23 at 10 39 47 PM" src="https://github.com/user-attachments/assets/94822a95-932f-444e-bd8a-d271d238f078" />


  3) This code merges the yearly FX, inflation, oil, and tourism risk factors into one table by year and computes Albania’s  Risk Index as the average of all four factors.

<img width="652" height="156" alt="Screenshot 2025-12-23 at 10 40 46 PM" src="https://github.com/user-attachments/assets/0aa0f05c-c0fa-4cf0-bfab-63e2659172c7" />


  4) This code creates a line chart of Albania’s Risk Index over time, marks the start of COVID in 2020 with a vertical line, and sets the y-axis to move in 0.1 increments so small changes in risk are easier to see.

<img width="613" height="181" alt="Screenshot 2025-12-23 at 10 41 08 PM" src="https://github.com/user-attachments/assets/8811319e-f704-45bd-b31e-4ffad8348650" />

## Index Risk Graph
<img width="1200" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/2d6f96c1-b6cc-488a-bfd4-bc9e38475280" />
- ##### 2010-2012: Gradual Decline
  
     FX: Stable Euro/Albanian Lek exchange rate with low volatility
  
     Oil: No major energy price shocks
  
     Inflation: Moderate and predictable
  
     Tourism: Stable growth
  
- ##### 2013-2014:
  
     FX & Inflation: Increase in volatility
  
     Oil: Stable but increasing prices
  
     Tourism: Consistent increase
  
- ##### 2015:
  
     FX: Increased volatility due to oil prices and the Greek Debt Crisis
  
     Oil: Global oil price collapse increases energy volatility
  
     Inflation: Deflationary pressures raise uncertainty
  
     Tourism: Still stable which partially offset the risk index against the others
  
- ##### 2016-2017:
  
     FX, Oil & Inflation: Prices stabilize and volatility is reduced
  
     Tourism: Strong growth
  
- ##### 2018-2019:
  
     FX: Little volatility
  
     Oil: Gradual price increase
  
     Inflation: Contained
  
     Tourism: Strong growth
  
- ##### 2020:
  
     FX, Oil, & Inflation: Increased uncertainty due to Covid 19 and price volatility
  
     Tourism: Collapse due to quarantine rules and border control
  
- ##### 2021:
  
     FX: Partial recovery and lower volatility
  
     Oil: Sharp rise in prices
  
     Inflation: Increase across Europe
  
     Tourism: Begins to rebound
  
- ##### 2022:
  
     FX: Stable
  
     Oil: Still high volatility due to the Russia-Ukraine War
  
     Inflation: Peaks
  
     Tourism: Strong recovery lowering the risk index
  
- ##### 2023:
  
     FX: Little volatility
  
     Oil: Uncertain due to geopolitical issues
  
     Inflation: Significant decrease
  
     Tourism: Strong performance



