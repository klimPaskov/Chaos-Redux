# 018 Resources Found release review, 2026-10-05

Status: source repairs implemented; release sign-off remains incomplete because required current-source MCP and live evidence is unavailable.

## Accepted decisions and implementation

- Accepted under the user's G3-G6 authority: concise discovery and enrichment reports, concrete compact cost profiles, and three core field values plus one contextual value.
- Implemented: the four opening postures remain, with plain descriptions of field ownership and development.
- Implemented: .90 explains unsuccessful manual survey preparation.
- Implemented: eleven project profiles retain their dynamic country, field and war scaling while using at most four spendable resource types.
- Factory counts in these profiles are non-debited requirements, rather than native factory reservations.
- Implemented: native rows show at most three resource amounts and full tooltips show every actual charge and the project duration.
- Implemented: Yield, Depth and Safety are core values; Breach takes priority over Disturbance in the fourth slot, with Foreign Pressure otherwise.
- Intentional presentation simplification: Foreign Pressure's number is not simultaneously displayed with a revealed underground threat.
- Implemented: four native focus navigation shortcuts retain the existing zoom and route logic.
- Existing resource rolls, the concentration cap, field lifecycle, cave routes, super-events and achievement conditions were retained.
- The scoped ImageGen reference is review material only; runtime sprites and models were reused.

## Owned files and surfaces

- `events/018_random_resource.txt`
- `common/scripted_effects/018_resources_found_prefire_effects.txt`
- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/script_constants/018_resources_found_decision_constants.txt`
- `common/national_focus/018_resources_found_cave_focus_tree.txt`
- `common/scripted_guis/018_resources_found_scripted_gui.txt`
- `interface/018_resources_found.gui`
- `localisation/english/018_random_resource_l_english.yml`
- `localisation/english/018_resources_found_decisions_l_english.yml`
- `localisation/english/018_resources_found_system_l_english.yml`
- `docs/events/018_resources_found/overview.md`
- `docs/events/018_resources_found/assets.md`
- `.tools/test_event018_field_value_slots.py`

## Evidence and limits

- Live baseline: evt018_pop00.png shows the four-posture Florida aluminium discovery with one event-owned popup.
- Cost handoff: subagent_handoffs/decision_costs_2026-10-05.md traces profiles, preview keys, affordability and debit.
- GUI handoff: subagent_handoffs/gui_audit_2026-10-05.md records exact before/after sources, the accepted reference and failed native render calls.
- Source tests execute the production fourth-slot predicates across active/history, reveal and suspension combinations, including empty and inactive-history gates.
- The current GFX audit resolves the scoped runtime assets; 67 focus nodes retain their unique registered icons.
- Current-source production GUI renders and focus/probability evidence remain blocked by 600-second route timeouts.
- The retained models_3d reconstruction workspace requires live model/audio acceptance and archive reconciliation; it is not deleted while evidence remains open.

## Exact orchestrator checks

- Load qa_001_fresh_head as USA and force Event 018: expect one Rich Deposits Found popup, four concise posture choices, and one selected field.
- Open the field category, inspect ordinary, disturbance, breach, suspended and closed-history states at 1920x1080 and 1366x768, UI scale 1: expect three core values and exactly one contextual fourth row.
- Inspect representative survey, industry, security, containment, sealing and anti-cave projects: expect at most three inline amounts and every actual charge in the tooltip.
- Use a zero, exactly sufficient, and just-insufficient reserve for a retained cost: exact equality should be affordable, and the debit should match the quote once.
- Complete and cancel anti-cave aid: confirm shipment quantities match the captured payment and no shipment is delivered after cancellation.
- Activate DHO through the existing cave scenario: check all four focus shortcuts, five brood models, movement/attack/death actions, sounds, counters and the retained terminal/defeat presentations.

## Catalog and assets

The catalog workbook and exports were not edited.
Catalog alignment notes are in catalog_changes_pending.md.
Existing runtime art, sound, flags, portraits and models were reused.
No live HOI4 session or desktop window was opened by this task.

## Required reference evidence

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:117-150`, local source SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-328`, local source SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2943-2967`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:5053-5074`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3624-3640`, local source SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:146-167`, local source SHA-256 `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/germany.txt:42-80`, local source SHA-256 `4cfd72972e19bcc560684dfc2f170e62ce786153ee01cf06ee7acc9609996095`.

Reference context/search/read routes returned some citations; failed and omitted sections were read locally.
Context inventories do not establish rule or engine coverage.
The connected service version and standalone viewer availability were not independently confirmed.
No repository-wide state-flow or helper-expansion query was used.
