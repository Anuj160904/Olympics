# Global Olympic Sports Performance Analysis – Tableau Build Guide

Step-by-step specifications, formulas, dashboard layouts, and Tableau Story setup for Olympic data (1992–2026).

---

## 1. Datasets & Calculated Fields
- **Data Source**: `data/cleaned_olympic_data.csv` (or relational join between `athletes.csv` and `medal_results.csv` on `RecordID`).
- **Calculated Fields**:
  1. **Avg Medals Per Athlete**:
     ```tableau
     SUM([TotalMedals]) / SUM([AthletesCount])
     ```
  2. **Cost Per Medal ($M)**:
     ```tableau
     SUM([SportsInvestmentMillions]) / SUM([TotalMedals])
     ```
  3. **Medal Efficiency %**:
     ```tableau
     AVG([MedalEfficiencyPct])
     ```

---

## 2. Worksheets Setup (7 Charts)

### Chart 1: Avg Medals per Athlete by Sport Category
- **Sheet Name**: `1_Medals_Per_Athlete_by_Category`
- **Rows**: `SportCategory` (Sorted descending by `Avg Medals Per Athlete`).
- **Columns**: `[Avg Medals Per Athlete]` (Rowing ~6.916, Shooting ~6.731 top).
- **Color**: `[Avg Medals Per Athlete]` (Blue gradient).
- **Mark**: Horizontal Bar.

### Chart 2: Global Performance Metrics by Country
- **Sheet Name**: `2_Global_Performance_by_Country`
- **Rows**: `Country` (Sorted descending by Total Medals: USA ~735, China ~696).
- **Columns**: `SUM(TotalMedals)`
- **Color**: `Region`
- **Mark**: Horizontal Bar with Medals breakdown on Tooltip (`GoldMedals`, `SilverMedals`, `BronzeMedals`).

### Chart 3: Trend of Total Medals Awarded Over the Years
- **Sheet Name**: `3_Trend_Total_Medals_Over_Years`
- **Columns**: `Year` (1992–2026).
- **Rows**: `SUM(TotalMedals)` (Low ~305 in 2000, peak ~363 in 2020, ~334 in 2026).
- **Color**: `Season` (Summer vs Winter).
- **Mark**: Line with circles at data points.

### Chart 4: Global Sports Investment vs. Medal Performance
- **Sheet Name**: `4_Investment_vs_Medal_Performance`
- **Columns**: `SUM(SportsInvestmentMillions)` (X-axis).
- **Rows**: `SUM(TotalMedals)` (Y-axis).
- **Detail**: `Country`
- **Color**: `Region`
- **Size**: `[Avg Medals Per Athlete]`
- **Mark**: Circle / Bubble.
- **Reference Lines**: Average Investment & Average Medals to isolate overperformers (Slovakia, Georgia, Ethiopia in upper-left quadrant).

### Chart 5: Average Medal Efficiency % by Region
- **Sheet Name**: `5_Medal_Efficiency_by_Region`
- **Angle**: `AVG(MedalEfficiencyPct)` (South America 49.64%, Europe/Asia 45.98%).
- **Color**: `Region`
- **Mark**: Pie / Donut chart.
- **Label**: `Region` + `AVG(MedalEfficiencyPct)`.

### Chart 6: Comparing Medal Totals Across Olympic Hosts
- **Sheet Name**: `6_Medal_Totals_Across_Olympic_Hosts`
- **Filter**: `IsHostNation = 'Yes'` or `HostNation` populated.
- **Columns**: `SUM(TotalMedals)` (Japan 105, USA 100, China 93).
- **Rows**: `HostNation`
- **Color**: Host country indicator.
- **Mark**: Bar chart.

### Chart 7: Regional Medal Efficiency & Distribution by Sport
- **Sheet Name**: `7_Regional_Medal_Distribution_by_Sport`
- **Rows**: `Region`
- **Columns**: `SUM(TotalMedals)`
- **Color**: `SportCategory`
- **Mark**: Stacked horizontal bar / Treemap showing Europe and Asia leading broad disciplines.

---

## 3. Dashboards Layout

### Dashboard 1 – Olympic Performance
- **Header**: "Global Olympic Performance (1992–2026)"
- **Global Filters Bar**: `Year`, `Season`, `Region`, `SportCategory`.
- **Top Left**: Chart 1 (`Avg Medals per Athlete by Sport Category`).
- **Top Right**: Chart 2 (`Global Performance Metrics by Country`).
- **Bottom**: Chart 3 (`Trend of Total Medals Awarded Over the Years`).

### Dashboard 2 – Olympic Performance & Regional Efficiency
- **Header**: "Investment Economics & Regional Medal Efficiency"
- **Global Filters Bar**: `Region`, `SportCategory`, `Year`.
- **Top Left**: Chart 4 (`Investment vs Medal Performance Bubble`).
- **Top Right**: Chart 5 (`Average Medal Efficiency % by Region`).
- **Bottom Left**: Chart 6 (`Comparing Medal Totals Across Olympic Hosts`).
- **Bottom Right**: Chart 7 (`Regional Medal Distribution by Sport`).

---

## 4. Tableau Story Architecture (3 Scenarios)
Create a new **Story** in Tableau and add 3 story points:

1. **Story Point 1: Priya – NOC Performance Strategist**
   - **Content**: Dashboard 1 filtered to high-yield disciplines (Rowing, Shooting).
   - **Story Caption**: "Targeted Sport Investment: Identifying high-yield categories (Rowing 6.9, Shooting 6.7 medals/athlete) to maximize podium conversions."

2. **Story Point 2: Carlos – Sports Investment Analyst**
   - **Content**: Dashboard 2 highlighting Chart 4 and Chart 5.
   - **Story Caption**: "Funding Efficiency: Spotlighting overperforming, under-invested nations (Slovakia, Georgia, Ethiopia) to guide regional grant allocation."

3. **Story Point 3: William Robert – Broadcast Data Journalist**
   - **Content**: Dashboard 1 (Chart 3) + Dashboard 2 (Chart 6 & 7).
   - **Story Caption**: "The Olympic Narrative Arc: Host nation medal surges (Japan 105, USA 100) and regional dominance patterns for documentary storytelling."
