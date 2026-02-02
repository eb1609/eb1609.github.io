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
events such as the COVID-19 pandemic. This is particularly relevant given Albania's objective to join the 
European Union by 2030. To achieve this feat, the EU requires consistent economic stability with low 
inflation risk, and the ability for a country's economy to absorb most external shocks. Hence, by quantifying 
economic risk across multiple factors, the index provides insight into Albania's progress for their goals.

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


  2) This code manipulates each dataset to yearly frequency, calculates the standard deviation of returns (volatility), and then converts that volatility into standardized risk factors so all risks are comparable on the same scale. Tourism uses a different method because two different sources were used and merged.
   
<img width="706" height="126" alt="Screenshot 2025-12-23 at 10 39 47 PM" src="https://github.com/user-attachments/assets/94822a95-932f-444e-bd8a-d271d238f078" />


  3) This code merges the yearly FX, inflation, oil, and tourism risk factors into one table by year and computes Albania’s  Risk Index as the average of all four factors.

<img width="652" height="156" alt="Screenshot 2025-12-23 at 10 40 46 PM" src="https://github.com/user-attachments/assets/0aa0f05c-c0fa-4cf0-bfab-63e2659172c7" />


  4) This code creates a line chart of Albania’s Risk Index over time, marks the start of COVID in 2020 with a vertical line, and sets the y-axis to move in 0.1 increments so small changes in risk are easier to see.


<img width="1200" height="600" alt="Overall" src="https://github.com/user-attachments/assets/98439924-9f1a-4629-9201-33412a9371fe" />

 
<div style="
  display: flex;
  gap: 40px;
  align-items: flex-start;
  margin-top: 40px;
">

  <!-- LEFT: YEARLY CONCLUSIONS -->
  <div style="flex: 2;">

    <h3>2010–2012: Gradual Decline</h3>
    <p style="margin-bottom: 80px;">
  
      FX: Stable Euro/Albanian Lek exchange rate with low volatility<br>
      
      Oil: No major energy price shocks<br>
      
      Inflation: Moderate and predictable<br>
      
      Tourism: Stable growth
    </p>

    <h3>2013–2014:</h3>
    <p style="margin-bottom: 120px;">

      FX & Inflation: Increase in volatility<br>
      
      Oil: Stable but increasing prices<br>
      
      Tourism: Consistent increase
    </p>

    <h3>2015:</h3>
    <p style="margin-bottom: 150px;">

      FX: Increased volatility due to oil prices and the Greek Debt Crisis<br>
      
      Oil: Global oil price collapse increases energy volatility<br>
      
      Inflation: Deflationary pressures raise uncertainty<br>
      
      Tourism: Still stable which partially offset the risk index against the others
      
    </p>

    <h3>2016–2017:</h3>
    <p style="margin-bottom: 50px;">

      FX, Oil & Inflation: Prices stabilize and volatility is reduced<br>
      
      Tourism: Strong growth
    </p>

    <h3>2018–2019:</h3>
    <p style="margin-bottom: 50px;">

      FX: Little volatility<br>
      
      Oil: Gradual price increase<br>
      
      Inflation: Contained<br>
      
      Tourism: Strong growth
    </p>

    <h3>2020:</h3>
    <p style="margin-bottom: 50px;">
 
      FX, Oil, & Inflation: Increased uncertainty due to Covid 19 and price volatility<br>
      
      Tourism: Collapse due to quarantine rules and border control
      
    </p>

    <h3>2021:</h3>
    <p style="margin-bottom: 50px;">

      FX: Partial recovery and lower volatility<br>
      
      Oil: Sharp rise in prices<br>
      
      Inflation: Increase across Europe<br>
      
      Tourism: Begins to rebound
      
    </p>

    <h3>2022:</h3>
    <p style="margin-bottom: 50px;">
   
      FX: Stable<br>
      
      Oil: Still high volatility due to the Russia-Ukraine War<br>
      
      Inflation: Peaks<br>
      
      Tourism: Strong recovery lowering the risk index
      
    </p>

    <h3>2023:</h3>
    <p style="margin-bottom: 35px;">
      FX: Little volatility<br>
      
      Oil: Uncertain due to geopolitical issues<br>
      
      Inflation: Significant decrease<br>
      
      Tourism: Strong performance
      
    </p>

  </div>

  <!-- RIGHT: VISUALIZATIONS -->
  <div style="flex: 3;">

    <img
      src="https://github.com/user-attachments/assets/67b04447-9598-4f01-8111-9f6445836aca"
      alt="2010–2012"
      style="width: 100%; border-radius: 10px; margin-bottom: 15px;"
    />

    <img
      src="https://github.com/user-attachments/assets/ee2ea3dd-f814-4f50-ab6a-5df1c47d54f3"
      alt="2013–2014"
      style="width: 100%; border-radius: 10px; margin-bottom: 15px;"
    />

    <img
      src=<img width="600" height="300" alt="152" src="https://github.com/user-attachments/assets/844222aa-5fd8-4845-bd27-c3390f93cd05" />

      alt="2015"
      style="width: 100%; border-radius: 10px; margin-bottom: 15px;"
    />

    <img
      src="https://github.com/user-attachments/assets/11a0d75b-f042-40db-98d5-65df781270c1"
      alt="2016–2017"
      style="width: 100%; border-radius: 10px;"
    />

    <img
      src="<img width="600" height="300" alt="18:19" src="https://github.com/user-attachments/assets/95850464-4e7c-4999-a4e3-ae181f1efa5b" />"
      alt="2018–2019"
      style="width: 100%; border-radius: 10px;"
    />

    <img
      src="<img width="600" height="300" alt="18:19" src="https://github.com/user-attachments/assets/95850464-4e7c-4999-a4e3-ae181f1efa5b" />"
      alt="2020"
      style="width: 100%; border-radius: 10px;"
    />
<img
      src=<img width="600" height="300" alt="21" src="https://github.com/user-attachments/assets/9bfba9c4-0d9b-4227-953d-c4c63bcfe540" />
      alt="2021"
      style="width: 100%; border-radius: 10px;"
    />

    <img
      src="<img width="600" height="300" alt="22" src="https://github.com/user-attachments/assets/a530ee27-6f33-43f7-8201-4c9c51755480" />"
      alt="2022"
      style="width: 100%; border-radius: 10px;"
    />

    <img
      src="<img width="600" height="300" alt="23" src="https://github.com/user-attachments/assets/856fe001-f1bf-43d5-81a2-6026cc2fc047" />"
      alt="2023"
      style="width: 100%; border-radius: 10px;"
    />

    
  </div>

</div>

