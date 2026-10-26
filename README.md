# Global Olympic Sports Performance Analysis (1992–2026)

Tableau dashboards and Story analyzing Olympic medal trends, athlete participation, regional conversion efficiency, host-nation advantages, and sports investment economics.

## Repository Structure

```
Olympics/
├── data/
│   ├── cleaned_olympic_data.csv     # 914 Olympic records with calculated metrics (1992–2026)
│   ├── athletes.csv                 # Athlete participation per country, sport, and year
│   └── medal_results.csv            # Detailed medal distributions & host nation flags
├── tableau/
│   ├── olympics_analysis.twb        # Tableau workbook XML linking 7 charts, 2 dashboards, and 1 story
│   └── olympics_analysis.twbx       # Self-contained packaged workbook with embedded data
├── scripts/
│   ├── clean_data.py                # Python/pandas data validation script
│   └── generate_data.ps1            # Dataset generation script
├── TABLEAU_BUILD_GUIDE.md           # Step-by-step build spec & formulas (Charts 1–7)
├── INSIGHTS_SUMMARY.md              # Insights for Priya, Carlos, and William Robert
└── README.md                        # Documentation
```

## Key Findings
- **High-Yield Disciplines:** Rowing (6.916) and Shooting (6.731) produce the highest medals per athlete.
- **Top All-Time Nations (Sampled 1992–2026):** United States (735 medals) and China (696 medals).
- **Efficiency Leaders:** Slovakia, Georgia, and Ethiopia deliver outsized medal performance relative to sports funding.
- **Regional Efficiency:** South America leads at 49.64%, followed by Europe/Asia at 45.98%.
- **Host Nation Advantage:** Japan (105 in 2020), USA (100 in 1996), China (93 in 2008).

## Persona Scenarios
1. **Priya (NOC Strategist):** Focuses on high-conversion sports categories.
2. **Carlos (Funding Agency Analyst):** Allocates grants based on investment-to-medal efficiency.
3. **William Robert (Broadcast Journalist):** Explores host-nation medal booms and historical expansion.

## How to Open in Tableau
Open `tableau/olympics_analysis.twbx` directly in Tableau Desktop or Tableau Public.
