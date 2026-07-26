# Event 006 AGX conference cost localisation post-repair audit

Date: 2026-07-26  
Scope: the repaired North Sea Coastal Conference decision cost surface, its base/tooltip/blocked localisation keys, civilian-factory gate, dynamic constant references, BOM, duplicate keys, and scripted-localisation references.  
Repair commit audited: `187115bd1` (`fix(event006): close AGX conference lifecycle gate`). The shared workspace is now at `13c4eb38b`, which adds an unrelated catalog commit on top; no scoped source file changed after the repair.

## Bounded disposition

The AGX conference cost surface is PASS after the repair. The decision uses `independence_wave_cost_agx_coastal_conference`, its tooltip and blocked-state keys, and `civilian_factory_major` (3). The available and custom-cost gates still call the shared strategic trigger, but that trigger uses the strict integer comparison `num_of_civilian_factories_available_for_projects > civilian_factory_standard` (2), which requires at least 3 available factories and therefore matches the three-factory reservation. No remaining AGX cost underreporting was found.

One low-priority wording gap remains outside the cost strings: the AGX decision description names the secure waterline, recognition, and network prerequisites but does not explicitly mention the authorization mandate or Low Countries candidacy that are also visible gates. This does not make the repaired cost surface incorrect, but it should be considered in a future wording pass.

## Missing key list

None. All three keys selected by `custom_cost_text = independence_wave_cost_agx_coastal_conference` are present in `localisation/english/006_independence_wave_decisions_l_english.yml`:

- `independence_wave_cost_agx_coastal_conference`
- `independence_wave_cost_agx_coastal_conference_tooltip`
- `independence_wave_cost_agx_coastal_conference_blocked`

## Duplicate key list

None in the audited localisation files. The decision localisation file has 223 parsed keys and the Wallonia/Frisia event localisation file has 178 parsed keys; neither contains a duplicate key. The three AGX cost keys occur only once across the localisation tree.

## Scripted localisation issue list

None. The three AGX cost strings use ordinary formatted constant tokens (`[?constant:...|...]`) and are not defined or consumed through `common/scripted_localisation/`. Every referenced constant exists in `common/script_constants/006_independence_wave_decision_constants.txt`.

## Cost, tooltip, and gate alignment

| Surface | Source | Result |
| --- | --- | --- |
| Decision cost key | `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:590-596` | PASS: `custom_cost_text` uses the dedicated AGX base key and the modifier reserves `civilian_factory_major`. |
| Available gate | `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:590-594` and `common/scripted_triggers/006_independence_wave_decision_triggers.txt:264-269` | PASS in effective terms: `civilian_factory_standard = 2` is used with strict `>`, so an integer factory count must be at least 3. The gate is therefore sufficient for the three reserved factories. |
| Base cost string | `localisation/english/006_independence_wave_decisions_l_english.yml:34` | PASS: 10% Stability, 5% War Support, 20 Command Power, 10 convoys or trains, and 3 spare civilian factories are formatted from the shared constants. |
| Tooltip string | `localisation/english/006_independence_wave_decisions_l_english.yml:79` | PASS: exact same five cost components and the major factory constant. |
| Blocked-state string | `localisation/english/006_independence_wave_decisions_l_english.yml:80` | PASS: exact same cost values with the expected `Unavailable:` prefix. |
| Payment effect | `common/scripted_effects/006_independence_wave_decision_effects.txt:291-295` and `:180-195` | PASS: the strategic payment subtracts the same 10% Stability, 5% War Support, and diplomatic-standard 20 Command Power plus 10 convoy-or-train reserve represented by the strings. |

The token name in the shared gate remains `civilian_factory_standard`, not `civilian_factory_major`, but changing it to `> civilian_factory_major` would raise the effective requirement to four factories. The current strict-greater-than pattern is what makes the standard floor of 2 express a three-factory minimum, so this is not a remaining functional or display mismatch.

## Dynamic text opportunities

- No dynamic localisation repair is required for the AGX cost strings. They already read all values from `independence_wave_decision_cost` constants, so tuning stays synchronized with the decision effect and modifier.
- The AGX decision description (`localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:117`) could mention the authorization mandate from the water-board government and the Low Countries candidacy. The visible gate also checks `independence_wave_agx_north_sea_conference_authorized` and `independence_wave_low_countries_federation_candidate` (`common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:581-589`). The mandate focus tooltip already explains that it authorizes the project, so this is a clarity improvement rather than a hidden cost.
- The adjacent AFX Meuse conference still uses the generic `independence_wave_cost_strategic` key with a major factory modifier (`common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:284-290`). That out-of-scope analogue displays the standard factory token even though its effective strict gate also requires three; it should receive a separate localisation audit if the whole Event 006 decision family is being normalized.

## Cross-surface mismatch notes

1. **AGX cost alignment: PASS.** The repaired base, tooltip, blocked-state strings, major modifier, and effective three-factory gate agree.
2. **AGX decision description: low-priority wording gap.** The description does not enumerate the authorization mandate or candidacy gate. This is not a cost-string failure and no source patch was made under the requested audit scope.
3. **Lifecycle gate: PASS for the repaired surface.** The multiline `cancel_trigger` in `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:597-610` mirrors the visible package, waterline, recognition, network, candidacy, authorization, route-lock, and capital-control conditions. Its text is not separately exposed in the cost localisation.
4. **GUI/scripted GUI: PASS.** The decision remains a regular decision-category entry. No AGX scripted GUI key or interface localisation reference was introduced.

## File encoding concerns

Both `localisation/english/006_independence_wave_decisions_l_english.yml` and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml` begin with UTF-8 BOM bytes `239,187,191`. No `:0` keys, leading key whitespace, em dash, semicolon, raw `§`, or raw `£` characters were found in the scoped cost strings.

## Recommended fixes

- No AGX cost localisation or gate fix is required after `187115bd1`.
- Consider a later wording-only update to `independence_wave_agx_convene_north_sea_coastal_conference_desc` that adds the mandate and candidacy prerequisites, using the AFX conference description as the nearest style precedent.
- If Event 006 cost strings are normalized globally, audit the AFX conference's generic `independence_wave_cost_strategic` use separately; do not change it as part of this bounded AGX handoff.

## Required handoff fields

- Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_conference_cost_localisation_reaudit_2026-07-26.md` only.
- Changed keys: none. This was an audit-only handoff; no gameplay or localisation source file was edited.
- Dynamic localisation added or fixed: none.
- Behavior or display before and after: source behavior is unchanged. After `187115bd1`, AGX displays 3 spare civilian factories in the base, tooltip, and blocked-state strings, and the strict integer gate permits the same three-factory minimum required by the modifier.
- Meaningful validation: PowerShell parsed both scoped YAML files, confirmed UTF-8 BOM bytes, counted keys, found no duplicates or `:0` keys, checked all three AGX cost keys, verified every constant token, and searched for scripted-localisation or GUI references. Targeted source comparison covered the decision, strategic trigger, constants, payment effect, and repair diff.
- Skipped meaningful validation and why: no in-game launch or live-save validation was run because repository instructions reserve live validation for the user. No GUI render was run because the repaired surface uses the regular decision UI and adds no scripted GUI.
- Unresolved wording decisions: whether to append the authorization and candidacy prerequisites to the AGX decision description, and whether to normalize the adjacent AFX conference cost string in a separate task.
- Plan handoff path: this file.

