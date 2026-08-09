# Chaos Warfare Division Command Spirit

## Contaminant Fire Coordination

`chemical_division_contamination_command_spirit` becomes available after Combat Support mastery two. It grants 35% artillery attack and 25% reliability to every mapped chemical payload-cylinder model, making artillery-heavy chemical formations and their logistics materially stronger without creating a separate release or consequence path.

The spirit is defined in `common/ideas/cbw_spirits.txt`. Its shared tuning lives under `cbrn_doctrine_spirit.contaminant_fire_coordination` in `common/script_constants/cbrn_doctrine_constants.txt`. Player-facing text is in `localisation/english/chaosx_ideas_l_english.yml`, and `GFX_idea_chemical_division_contamination_command_spirit` in `interface/cbrn_doctrine.gfx` uses `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/contaminant_fire_coordination.dds`.

The spirit does not run a hidden profile helper. Exact-state routes still use the shared chemical pipeline for payload debit, protection, disruption, deaths, contamination, medical saturation, evidence, attribution, history, treaty response, and Condemnation.

## Other division-command postures

`cbrn_mask_discipline_spirit` rewards a protective formation route with 20% army organization, 20% less organization loss while moving, and reduced military mask consumption in the protection ledger.

`cbrn_hazard_assault_cadres_spirit` rewards the Chaos Battalion and hazard-pioneer route with 10% special-forces capacity, 25% army experience gain, and 30% attack and defense for both mapped sub-units.

These postures are mutually exclusive officer-corps choices. Their large visible bonuses make the selected formation doctrine meaningful, while the shared equipment and exposure systems retain authority over consumable use and CBRN consequences.
