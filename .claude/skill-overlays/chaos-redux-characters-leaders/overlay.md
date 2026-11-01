---
description: Use when defining, recruiting, promoting, retiring, scripting, or auditing Chaos Redux characters and roles (country leaders, advisors, field marshals, corps commanders, admirals, scientists), the historical CBRN scientist roster, leader and scientist traits, ideologies and parties, or character portrait references and localisation. Covers the character database, the effects and triggers, and the silent failures.
---

### In Contents

- Chaos Redux specifics

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here. Scope iterations to one country; a character hook that runs for every country needs permission. (Chaos Redux wording differs from the kit)

**Where Chaos Redux characters live**

- `common/characters/` has one file per owner (`<event>_characters.txt`, `cbrn_historical_scientists.txt`, `cbrn_historical_specialists.txt`, `chaosx_test_country_characters.txt`, plus country files such as `DTH.txt`). Character ids are unique across all files.
- Traits: scientist traits in `common/scientist_traits/`, unit leader traits in `common/unit_leader/` (`cbrn_hq_traits.txt`, `chaosx_traits.txt`, event files). Portrait sprites live in `interface/*.gfx` with art under `gfx/leaders/<owner>/`.
- Startup recruitment: the 67-person historical CBRN roster (15 dual-role specialists, 52 scientist-only) is recruited directly into its home countries by `history/general/chaosx_startup_character_recruitment.txt`; country grants apply the persistent `chaosx_scientist_*` identity flags. Scientist skills and traits follow `docs/systems/cbrn_warfare/cbrn_historical_scientists.md`. The dated CSH transfer contract is historical and superseded.

**Rules that recur**

1. Every portrait goes through `chaosx_portrait_creator` and `chaos-redux-event-assets`, for grounded and fictional subjects alike. A sourced placeholder is documented as pending until the user supplies the HOI4-style final, and agents never operate RunPod. This skill only covers how a character references a portrait. (Chaos Redux wording differs from the kit)
2. Historical scientist skill uses the installed 1 to 4 scale (inexperienced, skilled, experienced, expert) and never 5. Skill 4 is for field authorities who established a method; administration alone does not earn it. Traits use the vanilla scientist vocabulary plus `scientist_trait_inhumane` and `scientist_trait_inhumane_cw`, which describe conduct, not stature (`docs/systems/cbrn_warfare/cbrn_historical_scientists.md`).
3. Earned commander traits are appended rows that leave vanilla rows unchanged, and are credited once per completed order (`docs/systems/cbrn_warfare/cbrn_commander_progression.md`).
4. Advisor cards, scientist cards, and leader cards that the CBRN systems use are listed in `docs/systems/cbrn_warfare/cbrn_historical_advisors.md` and `cbrn_defensive_advisor_cards_manifest_2026-09-27.md`.
5. Keep a docs file for the mechanic with its portrait sprite names, `.gfx` file, and icons. (Chaos Redux wording differs from the kit)
