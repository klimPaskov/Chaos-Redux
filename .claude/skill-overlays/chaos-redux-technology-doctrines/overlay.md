---
description: Use when creating, changing, scripting, or auditing Chaos Redux technologies, technology folders and cards (chemical and biological), project-gated technologies, grant helpers, technology sharing, the Chaos Warfare grand doctrine and sub-doctrines, or the technology tree inspector and renderer. Also use when a technology or doctrine is invisible, unresearchable, unlocks nothing, or grants no bonus.
---

### In Technology sprites and localisation of references/technology-tree-gui.md

- The repository includes its own `chaosx_techtree.gfx` for local tiles.

### In Decision table

Chaos Redux wording differs from the kit:

| Goal | Mechanism |
| --- | --- |
| Understand or verify an existing tree | The `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_inspect` (`mode = compare`) tools |

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here.

**Where Chaos Redux research lives**

- `common/technologies/` has one file per owner. `chaosx_technologies.txt` owns the shared chemical and biological research nodes; `cbrn_project_equipment_technologies.txt` holds the project-gated equipment unlocks; `cbrn_hq_technologies.txt` and `cbrn_regimental_support_technologies.txt` own unit certifications that have no visible card; event files (`012_*`, `014_*`, `016_*`, `039_*`, `042_*`, `clone_*`, `zombie_*`) own their own technologies.
- `common/technology_tags/chaosx_tech_tags.txt` defines the folders and categories. `interface/countrytechtreeview.gui` and `.gfx` are full copies of the vanilla files with the Chaos folders added (re-merge vanilla changes after a game update). Local card tiles are in `interface/chaosx_techtree.gfx`. (Chaos Redux wording differs from the kit)
- Research costs in the CBRN folders use a 0.5 (basic utility), 0.75 (ordinary equipment and service), and 1 (advanced equipment and containment) scale of the 100-day baseline (`docs/systems/cbrn_warfare/cbrn_technology_progression.md`).

**Folder geometry (chemical_warfare_folder, biowarfare_folder)**

- Both folders use the vanilla grid: `format = "LEFT"`, `slotsize = { width = 70 height = 70 }`, one gridbox per branch row, branch gridboxes starting at x = 220 with rows 110 pixels apart, year columns three slots (210 pixels) apart, branch labels right-aligned in the left gutter, and every card chain drawn by `path` instead of invisible dependencies. Content fillers are sized to their content.
- Card size follows the vanilla rule, so do not set `force_use_small_tech_layout`: a technology that unlocks equipment draws the full-size named card (183x84 box), and every other technology draws the small 72x72 box without a name. Forcing the small box on every card hides the names.
- Schedule research years so each branch advances one column per step. The longest link in either folder is two columns (420 pixels), the longest link vanilla draws in its support folder; a branch that jumps many columns draws a long unreadable link.
- Before and after geometry for both layout passes is in `docs/plans/chaos_warfare_system_plans/2026-10-10_technology_folder_layout_repair.md`.

**Project-gated and hidden technologies**

- Capability technologies with no card are hidden and granted only by helpers: `chaosx_grant_conventional_technology_package`, `chaosx_grant_custom_operational_technology` (idempotent clone, paleogenetics, and xenobiology selectors), and `cbrn_grant_available_doctrine_technologies` (doctrine and certification grants). Call the helper instead of pasting `set_technology`, so repeated paths grant a package once.
- `union_compatible_researched_technologies_from_donor` in `chaosx_dynamic_effects.md` copies compatible researched technologies between countries.

**Doctrine**

- The Chaos Warfare grand doctrine is `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt` with land sub-doctrines in `common/doctrines/subdoctrines/land/`; behaviour is in `docs/systems/cbrn_warfare/chaos_warfare_doctrine.md`, and the doctrine workbook is edited through `chaos-redux-xlsx`.
- Doctrine, country, and technology bonus layers stack on the same unit. Budget a reward against the combined bound, not against one source (`docs/testing/2026-10-07_doctrine_reward_budget_source_tests.js` shows the method). Subunit bonus fields are fractions, not flat points.

**Test-country registration**

The test country scans `global.technology` dynamically (the only documented runtime database array), so a plain technology needs no registration. A special project, equipment type, sub-unit, or doctrine does: see `docs/testing/chaosx_test_country.md`.

