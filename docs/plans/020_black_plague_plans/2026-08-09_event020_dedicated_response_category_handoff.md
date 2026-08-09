# Event 020 Dedicated Black Plague Response Category Handoff

Date: 2026-08-09

## Accepted correction

Event 020 uses one dedicated national cure and strategic-management decision category in addition to the existing shared disease-containment category. The later correction is recorded in `docs/specs/020_black_plague_specs/corrections/2026-08-09_dedicated_response_category.md` and supersedes the historical single-category rule.

## Runtime ownership

`black_plague_response_category` is defined in `common/decisions/categories/020_black_plague_response_categories.txt`. It is visible through `black_plague_strategic_response_category_is_visible`, remains independent of the disease selected on the shared board, stays visible when temporarily empty, uses priority 101 beside the shared category's priority 100, and adds no scripted GUI.

The dedicated category owns fifteen existing actions without duplicating their IDs or effects:

- Medical Reserve production.
- Establishing the 0–100 countermeasure/cure programme.
- Doctor Wu protocol activation and foreign-access requests.
- Emergency Countermeasure Drive.
- Publishing, exchanging, hoarding, or stealing findings.
- International Medical Mission.
- Reconstruction Vigilance, International Inspection Compact, condemnation of future weaponization, Population Recovery Programme, and Memorial and Biosecurity Charter.

`chaosx_disease_containment_category` remains intact and retains the forty-seven Event 020 selected-state, prepared/exposed, containment, recovery, anti-rat, Royal Node, Crown, burrow-sealing, and terminal-response entries. Human state targets remain tied to the Black Plague selection and selected state on the shared board; AI countries retain their all-eligible-controlled-state route.

All sixty-two response decision IDs are unchanged and unique. No effect, cost, duration, mission owner, cooldown, state lane, progress variable, or cleanup resolver was copied. The dedicated category calls the existing countermeasure progress producer, which clamps at 100, reduces mortality and spread through the existing runtime, and unlocks cure-capable cleanup without directly removing an active outbreak.

## Standard category status display

`black_plague_response_category_desc` shows:

- deaths recorded for the viewing country;
- worldwide Black Plague deaths;
- cure-programme state through `GetBlackPlagueCountermeasureStatus`;
- current cure progress against the existing completion constant;
- Medical Reserve and capacity;
- remaining and total Response Capacity;
- international cooperation state through `GetBlackPlagueInternationalResponseStatus`.

The description directs selected-state quarantine, hospitals, rat clearance, cordons, treatment, and cleanup to the shared Disease Containment board. It states that completing the cure programme unlocks cure-capable cleanup and never removes an active outbreak by itself.

## Category picture

`GFX_decision_cat_picture_black_plague_response` is registered in `interface/020_black_plague_response.gfx` and consumed by the dedicated category. The runtime DDS is `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds`.

The final picture is a 114×101 static fictional period treatment scene showing two protected plague doctors tending a patient. The asset has no readable text, gore, modern medical equipment, simulated buttons, meters, or interface borders. Source, exact ImageGen prompt, processed PNG, contact sheet, DDS round-trip, header QA, and wiring notes are retained in `docs/assets/020_black_plague/decision_category_picture_black_plague_response/`. The legacy uncompressed BGRA DDS is 46,184 bytes and its decoded pixel data matches the processed PNG exactly.

## AI and MCP evidence

Every dedicated action retains its original availability gate, material/capacity checks, duration, and `ai_will_do` block. A source comparison against `HEAD` before the category move found no changed AI base or factor line and no changed decision ID. All fifteen dedicated actions have visibility or activation gates, availability gates, explicit cost text, a duration, and AI willingness.

The installed HOI4 MCP was used for probability and standard-category GUI evidence. Canonical Event 020 probability inspection remains tool-blocked:

- response ordinary decisions: `INTERNAL_ERROR`, `Unexpected internal error`, no artifact;
- shared ordinary decisions: `PROBABILITY_SURFACE_EMPTY`, `No weighted blocks matched this request`, no artifact;
- Emergency Countermeasure Drive mission: `INTERNAL_ERROR`, `Unexpected internal error`, no artifact.

The previous Event 020 audit also has no artifact-backed probability baseline, so no valid `hoi4.probability_compare` receipt can be produced. The probability handoff does not convert willingness scores into click probabilities or make unsupported balance claims. A diagnostic flat-source probe parsed the shared score blocks, but it is explicitly not treated as canonical engine evidence.

The standard decision category has no named scripted-GUI window. The generic GUI MCP route emitted a standard-category artifact but also returned `GUI_WINDOW_MISSING`, `GUI_SCRIPTED_CONTEXT_INVALID`, and a truncated validation response. This is recorded as a tool coverage limitation rather than a reason to add the scripted GUI the user rejected.

Detailed evidence is in:

- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_dedicated_category_decision_audit.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_dedicated_category_localisation_audit.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_dedicated_category_probability_audit.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_black_plague_category_picture_handoff.md`

## Validation and disposition

- Brace-aware checks pass for the category, decision, trigger, scripted-localisation, and GFX files.
- The dedicated/shared ownership scan resolves fifteen dedicated actions and forty-seven shared actions with no duplicate child ID.
- All 231 player-facing references in the two Event 020 response decision files resolve to English localisation keys with no duplicate referenced key.
- The localisation file retains its UTF-8 BOM.
- The category picture sprite, texture path, DDS dimensions, byte length, and round-trip are verified.
- No Event 020 event, evolution, cluster, or scenario-catalog wording changed, so the event-catalog workbook did not require an update.

No gameplay simplification, fallback, placeholder, duplicate category, duplicate cure system, instant cure, political-power store, or hidden scripted GUI was introduced. Live Hearts of Iron IV category rendering and gameplay behavior remain user-owned validation. The only unresolved evidence limitations are the exact MCP adapter blockers recorded above.
