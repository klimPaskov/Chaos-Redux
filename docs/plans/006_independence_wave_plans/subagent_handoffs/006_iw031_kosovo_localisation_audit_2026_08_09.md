# IW-031 Kosovo localisation audit handoff

**Date:** 2026-08-09  
**Scope:** current IW-031 Kosovo localisation, visible decision and category text, national spirits, cosmetic identities, party identities, effect and cost tooltips, flag wording, and aligned package documentation.  
**Mode:** bounded localisation and documentation patch. No gameplay, asset, spreadsheet, attestation, promotion, or commit work.

## Outcome

The current Kosovo localisation file defines 97 package keys. All 97 keys required by the current party, cosmetic, idea, category, decision, mission, effect-tooltip, and custom-cost sources are present. None of those keys is duplicated in the English localisation tree.

The audit patched seven localisation keys and two package documentation files. It also corrected the shared FORM-09 documentation, which still described Kosovo as unavailable after the source added IW-031 and state 802 to the eligible-member and integration paths.

The package is not ready for a complete localisation claim because the three roster identifiers referenced by `events/006_independence_wave.txt` and the Kosovo package effects and triggers still have no character definitions or character localisation in the final audit state.

## Missing key list

No key is missing from the 97-key set currently defined by `localisation/english/006_independence_wave_kosovo_l_english.yml`.

The following intended character-name surfaces remain unresolved because the corresponding character definitions and localisation are absent:

- `KOS_independence_wave_ferhat_draga`
- `KOS_independence_wave_miladin_popovic`
- `KOS_independence_wave_shaban_polluzha`

The hidden roster event recruits all three identifiers, and the route tooltips name the same three men in prose. A final portrait handoff must add the definitions and character localisation together, then rerun the duplicate, encoding, and visible-name checks.

## Duplicate key list

None for the 97 current IW-031 keys. The scan checked every English `.yml` file under `localisation/english`.

## Scripted localisation issues

No IW-031 scripted-localisation block exists, and no current Kosovo key calls a missing scripted-localisation selector. The two public ledgers and every displayed threshold, gain, loss, and cost use direct dynamic variable or script-constant localisation.

## Dynamic text and exact-value review

- `independence_wave_kos_cantonal_compact_category_desc` displays Civic Concord and Municipal Reach with integer formatting, the exact 0 to 100 range, and the exact stability threshold of 60.
- `independence_wave_kos_project_failure_effect_tt` matches the one-shot failure effect: both public ledgers lose 10, Legitimacy loses 10, Recognition loses 5, State Capacity loses 10, Security loses 10, and Instability gains 15.
- `independence_wave_kos_assembly_effect_tt`, `independence_wave_kos_guards_effect_tt`, and `independence_wave_kos_communities_effect_tt` match the corresponding compact-value and shared Event 006 reward helpers.
- `independence_wave_kos_host_ledgers_effect_tt` preserves the two consecutive host-settlement bundles instead of hiding either set of deltas.
- The four government-route tooltips match the administrative, diplomatic, or security value bundle called after the government change.
- `independence_wave_kos_sovereignty_effect_tt` matches `independence_wave_kos_apply_major_settlement`.
- `independence_wave_kos_network_effect_tt` separately reports the corridor-opening rewards and the final corridor-accord rewards. This preserves every value change from both called effect families.
- The three Kosovo-specific custom cost strings match their triggers and payment effects. Administration costs show the exact Command Power, manpower, and one-factory commitments. The strategic cost shows Stability, War Support, Command Power, the convoy-or-train alternative, and the one-factory commitment.

No new scripted localisation was needed. A future character pass may use dynamic character-name localisation if the final character definitions require it, but the current fixed historical names do not justify inventing a selector before those definitions exist.

## Cross-surface alignment

### Corrected

- `docs/events/006_independence_wave/form09_balkan_federation.md` now lists Kosovo as an eligible sovereign member and includes state 802 among the staged anchors, matching `is_independence_wave_form09_eligible_member` and the FORM-09 integration effect.
- The socialist route now distinguishes the ruling `Kosovo Workers' Front` from the `Municipal Workers' Council` it convenes. The tooltip and Kosovo package document now agree with `set_party_name` and the route idea.
- The socialist and emergency tooltips now state that they retain the Yugoslav municipal standard, matching the opening cosmetic tag and the package document.
- The civic route continues to identify the Albanian civic standard. The federal route continues to identify the Yugoslav municipal standard.

### Confirmed

- Both cosmetic families have base, `_DEF`, `_ADJ`, and all four ideology-specific name sets.
- All opening and route party short and long names used by `set_party_name` are localised.
- All six national spirits have names and descriptions.
- The package document correctly states that no advisor, high-command, dossier, or small-portrait surface belongs to IW-031. No Kosovo advisor or woman-specific character surface was found in source or localisation.
- The Kosovo package document and the two flag handoffs consistently treat the Albanian civic flag as an Albanian-led route standard and the Yugoslav tricolour as a Yugoslav provisional municipal standard. None calls either asset a universal historical Kosovo flag.

## File encoding concerns

`localisation/english/006_independence_wave_kosovo_l_english.yml` begins with `EF BB BF`, contains no NUL bytes, and remains UTF-8 with BOM after the patch. No `:0` key suffixes or leading key indentation were found.

Future character localisation must also use UTF-8 with BOM.

## Prose-quality review

### Vagueness

The socialist government text previously blurred the ruling party and the council it creates. The revised tooltip and package document state who takes office and which institution it convenes.

### Bloat

The three Kosovo-specific cost strings previously described each commitment in full sentences. They now use the shared icon-first cost style while preserving every amount and the one-factory Kosovo override.

### Obvious explanation

The Kosovo package document previously described project serialization as an implementation gate. It now tells the reader directly that only one project can run at a time.

### Repetition

Repeated `Commits` phrasing was removed from the custom costs. The values and resource identities remain visible.

### Overcomplication

The host and corridor tooltips remain mechanically dense because each action calls two separate effect bundles and the audit requirement demands exact visible deltas. Their headings now describe in-world actions instead of implementation stages.

### Style-rule repair

`Package settlement` and `Project settlement` were removed as working labels. The emergency-route document no longer refers to avoiding a `free-unit loop`. No em dash, sentence semicolon, prompt fragment, update-history phrase, placeholder label, or staged contrast formula remains in the audited localisation file.

## Sourced quotation preservation

The flag research handoff contains attributed quotations from the 1931 Yugoslav constitution and the 1928 Albanian statute. This audit did not edit, shorten, modernize, or repunctuate either quotation. No player-facing IW-031 localisation key contains an attributed quotation.

## Changed files and keys

### Localisation

Changed `localisation/english/006_independence_wave_kosovo_l_english.yml`:

- `independence_wave_kos_host_ledgers_effect_tt`
- `independence_wave_kos_socialist_route_effect_tt`
- `independence_wave_kos_emergency_route_effect_tt`
- `independence_wave_kos_network_effect_tt`
- `independence_wave_kos_cost_administration_light`
- `independence_wave_kos_cost_administration_standard`
- `independence_wave_kos_cost_strategic`

No dynamic token, formatter, colour terminator, cost, requirement, threshold, name, or consequence was removed.

### Documentation

Changed `docs/events/006_independence_wave/kosovo_package.md` to clarify project concurrency, emergency supply responsibility, and the Workers' Front versus Workers' Council distinction.

Changed `docs/events/006_independence_wave/form09_balkan_federation.md` to admit Kosovo through IW-031 and state 802 and remove the obsolete future-admission statement.

## Display before and after

- Before, Kosovo-specific custom costs appeared as repeated prose sentences. After, they use concise icons and exact dynamic amounts.
- Before, socialist and emergency route outcomes did not explain which flag standard remained in use. After, both explicitly retain the Yugoslav municipal standard.
- Before, the socialist tooltip said the council itself took office even though the script installs the Kosovo Workers' Front as the ruling party. After, the Front takes office and convenes the council.
- Before, two long tooltips used internal stage labels. After, they describe the settlement, negotiations, corridor opening, and corridor accords directly.
- Before, FORM-09 documentation excluded Kosovo. After, it matches the implemented member trigger and state-802 integration branch.

## Validation and evidence

- A source-derived expected-key audit checked 51 category, idea, decision, mission, tooltip, and cost keys and 46 party and cosmetic keys. All 97 exist.
- A repository-wide English localisation scan found no duplicate definition for any of the 97 IW-031 keys.
- Every displayed ledger range, threshold, delta, and cost was compared with the exact script constant and called effect chain listed above.
- Cosmetic coverage was checked for both base identities and all ideology-specific `_DEF` and `_ADJ` variants.
- Party coverage was checked against every `set_party_name` call in the Kosovo package effects.
- The final portrait rerun still found only the three recruitment references in `events/006_independence_wave.txt`. No matching character definition or character localisation had appeared.
- The required read-only `hoi4.event_inspect` route was attempted for hidden roster event `chaosx.nr6.350`. A full trace remained running without a result for roughly three minutes and was terminated. A narrower cached lint returned `EVENT_INSPECTED_PARTIAL`, one artifact, and workspace `mod_chaos_redux_ea3b2d67c2c0`. The host timed out when asked to expose the artifact URI, so no useful artifact URI is available and the partial result is not treated as complete event evidence.

## Skipped meaningful validation

- No dedicated IW-031 scripted GUI, focus tree, map rewrite, or technology surface exists in this localisation scope, so no GUI, focus, map, or technology render was applicable. The installed Technology Tree Viewer is absent as documented by the agent contract.
- The default decision interface has no available decision-layout render route. Exact source coverage was checked, but live font overflow and default decision-panel wrapping remain consumer-side observations.
- No in-game validation was performed. Live consumer validation belongs to the user.

## Remaining issues and parent follow-up

1. Complete the three-character portrait package, definitions, and character localisation, then rerun the IW-031 name, duplicate, encoding, roster, and route-tooltip checks.
2. Review the partial MCP workspace only if the event inspection host later exposes its artifact URI. Do not treat this handoff as full MCP event-chain proof.
3. Keep central content attestation closed until the separate portrait, country-package, decision, AI, and completion audits are reconciled by the parent.

## Simplifications, omissions, and blockers

No gameplay or flag fallback was introduced. The character roster and its localisation remain incomplete in the audited repository state. Default decision-UI overflow could not be rendered with an available MCP route, and the event MCP returned only partial evidence.

No separate improvement plan was written because the findings were bounded localisation and documentation defects rather than a missing mechanic.
