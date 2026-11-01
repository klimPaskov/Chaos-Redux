---
description: Use when designing, implementing, tuning, auditing, or debugging Chaos Redux country AI behaviour: common/ai_strategy blocks and CBRN country profiles, add_ai_strategy, AI strategy plans, AI focuses and scorers, ai_will_do and ai_chance weights, AI templates, equipment production AI, AI peace desires, and AI research or diplomacy weighting.
---

### In Other AI systems of references/other-ai-systems.md

`GAME` is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. (Chaos Redux wording differs from the kit)

### In AI strategy token catalog of references/strategy-token-catalog.md

Primary source: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/_documentation.md` (updated 2024-11), cross-checked against `paradox_wiki/ai_modding.md` and the usage counts in vanilla `common/ai_strategy/*.txt`. (Chaos Redux wording differs from the kit)

### In Chaos Redux AI Strategies

Guidance for steering the Hearts of Iron IV country AI from Chaos Redux script. (Chaos Redux wording differs from the kit)

### In Contents

- Chaos Redux specifics

### In Source map

`GAME` means `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. (Chaos Redux wording differs from the kit)

### In Debugging and verification

1. Read the actual block and compute representative cases by hand. For `ai_will_do`, `ai_chance`, strategy plans and MTTH-backed weights prefer `hoi4_probability_inspect` (adapters: `event_option_ai_chance`, `decision_ai_will_do`, `mission_ai_will_do`, `national_focus_ai_will_do`, `technology_ai_will_do`, `doctrine_ai_will_do`, `ai_strategy_factor`, `random_list`, `direct_random`, `custom_weighted_pool`, `event_mean_time_to_happen`), then `hoi4_probability_inspect` or `hoi4_probability_analyze` (`analysis = compare`) with explicit named scenarios (country, date, flags, government, factory counts). (Chaos Redux wording differs from the kit)

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, and localisation rules apply and are not repeated here. Two AI-specific consequences: world-iterating hooks (`on_daily`, `on_weekly`, `on_monthly`) are not a way to implement AI behaviour, so gate behaviour in the `enable` block of an `ai_strategy` (the engine already evaluates it) or use `on_daily_TAG` for a named country; and a flag trigger in a player-visible block shows its raw identifier unless localised, so AI-only gating belongs in `ai_will_do` or `enable`. (Chaos Redux wording differs from the kit)

**Where Chaos Redux AI lives**

- `common/ai_strategy/` has one file per owner, named by event number or system. The CBRN set is `cbrn_country_profiles.txt` (differentiated research, medical, delivery, and biological-response priorities per major and secondary country), `chemical_warfare_research.txt`, `chemical_warfare_cylinders.txt`, `chemical_warfare_livens.txt`, `chemical_warfare_tank_shells.txt`, `cbrn_protection_production.txt`, `cbrn_regimental_support.txt`, and `biological_warfare_production.txt` (native `equipment_production_surplus_management` with exact equipment models).
- Companion folders: `common/ai_strategy_plans/` (focus plans per event), `common/ai_templates/` (division templates per unit family), `common/ai_focuses/chaosx_ai_focuses.txt`, `common/scorers/country/` (outbreak and target scorers), and `common/mtth/` (weights shared through `chaos-redux-mtth`).
- Special-project selection is weighted inside the project definitions (`common/special_projects/projects/biowarfare_main_projects.txt` enforces the Tularemia, Anthrax, Plague, Smallpox ladder), not in a strategy file.

**Rules that recur**

1. Constants: the CBRN profile file keeps its values as file-scoped `@` constants because `ai_strategy` values do not parse shared `script_constants`. Verify the field before using `constant:category.key` in a new strategy file.
2. Gate on real posture, never on a country tag. CBRN AI conditions go through `common/scripted_triggers/cbrn_ai_posture_triggers.txt` (authorization, designated-arsenal risk, protection, containment technology, supply). The AI never receives free equipment, never researches a locked project-output technology directly, and never treats missing data as safe (`docs/systems/cbrn_warfare/cbrn_biological_ai.md`).
3. Special Chaos countries are excluded from the humanitarian systems (`humanitarian_country_is_valid`) and nonhuman outbreak countries from the military industrial organizations; check that a target country exists (`exists = yes`, `country_exists`) before steering at it.
4. Strategy values stack across every active block of the same type and target, so a Chaos override of a vanilla strategy must exclude the vanilla block's countries or add a compensating value. (Chaos Redux wording differs from the kit)
5. Every changed weighted surface (`ai_will_do`, `ai_chance`, MTTH-backed scores, random lists, strategy factors, special-project weights) goes through `chaosx_ai_probability_auditor`. Keep the before-state: audits store theirs under `docs/testing/<date>_<topic>_before/`. Report score separately from probability, and state any assumption the analyzer could not model.
6. Event firing weights (the dynamic major-event pool) are documented in `docs/systems/event_system/dynamic_major_event_weights.md`; they are not AI strategy.
