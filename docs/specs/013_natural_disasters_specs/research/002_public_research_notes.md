# Public research notes for disaster design

These notes are not final player-facing text. They give the implementation and research agents factual anchors for hazard families, impact scaling, and recovery framing.

## Sources consulted

- EM-DAT disaster classification guidance, especially the grouping of natural hazards into geophysical, hydrological, meteorological, climatological, biological, and extra-terrestrial groups.
- UNDRR terminology on hazard, disaster, disaster impact, disaster risk, and disaster risk reduction.
- USGS earthquake hazard material on shaking, surface faulting, ground failure, tsunami links, building vulnerability, population density, and construction quality.
- World Bank and GFDRR disaster risk management material on resilient infrastructure, preparedness, financial resilience, and recovery.

## How the research shaped the design

The specification groups Event 013 families into practical in-game categories that map cleanly to disaster behavior: ground, water, weather, climate, fire, volcanic, space, and abnormal movement systems. The grouping is inspired by public hazard classification, but it is adapted for HOI4 gameplay rather than copied as a database schema.

Impact math should treat a disaster as a hazardous event that becomes deadly through exposure and vulnerability. That means the same earthquake, flood, storm, or heat wave kills more people and damages more buildings when it hits dense population, weak infrastructure, poor supply, existing devastation, low recovery capacity, war strain, and unresolved aftermath.

Recovery should not be a single flat repair button. It should combine emergency protection, transport clearing, evacuation, relief, disease control, food supply, reconstruction, and public order work. Strong countries can reduce losses before impact and clear aftermath faster. Weak, occupied, starving, or unstable countries can suffer chained deaths long after the first report.
