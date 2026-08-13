# Event 015 Localisation Completion Handoff

Date: 2026-07-15  
Owner: `chaosx_localisation_worker`  
Scope: Event 015 English localisation only  
Commit: not created, by parent instruction

## Outcome

The current Event 015 decision, mission, category, event, custom-cost, custom-effect-tooltip, and custom-trigger-tooltip surface has complete English localisation. The final live-source inventory contains 1,287 unique required keys and zero missing keys.

The player-facing Ledger vocabulary now uses Need, Plenty, Concord, and Choice versus Assignment. Retired metric language was rewritten where live and removed where it belonged only to the deleted decision package.

## Missing-key inventory

### Initial audit

The first inventory contained 1,281 unique required keys and 539 missing keys:

| Requirement | Missing |
| --- | ---: |
| Decision category names | 6 |
| Decision category descriptions | 6 |
| Custom-cost base strings | 61 |
| Custom-cost blocked strings | 62 |
| Custom-cost tooltip strings | 62 |
| Decision and mission names | 112 |
| Decision and mission descriptions | 112 |
| Event title, description, or option strings | 9 |
| Custom effect or trigger tooltip strings | 109 |
| **Total** | **539** |

### Concurrent pre-fire tranche

While localisation was in progress, the new pre-fire decision and event tranche added 52 further missing requirements:

| Requirement | Added missing |
| --- | ---: |
| Four decision or mission name/description pairs | 8 |
| One custom-cost base/blocked/tooltip set | 3 |
| Decision and mission outcome tooltips | 3 |
| Event 105-109 and 117 title, description, and option strings | 31 |
| Event 106, 109, and 117 effect tooltips | 7 |
| **Total** | **52** |

The working source changed while this pass was active, so the final required-set size is not the arithmetic sum of the two snapshots. Across both snapshots, 591 missing requirements were encountered and supplied. The final current-source result is:

- unique required keys: 1,287
- missing keys: 0
- decision and mission definitions covered: 164, each with name and description
- decision categories covered: 9, each with name and description
- unique custom-cost bases covered: 92, each with base, `_blocked`, and `_tooltip`
- unique decision custom effect or trigger tooltips covered: 163
- unique event localisation references covered: 502, including 36 event effect tooltips

## Files changed

- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`
  - New UTF-8 BOM file containing the missing category, decision, mission, custom-cost, outcome-tooltip, dynamic-cost, route, target, cancellation, and cleanup strings.
  - Includes the late pre-fire deadlines and domestic shore repair decision package.
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
  - Added events 105-109, 117, 206, and 207.
  - Event 109 discloses the initial Plenty and Assignment changes, the 30-day store-planning credit, Sponsored Law selection, and all route-resolved support consequences.
  - Event 117 explains that the selected Perfect Island interpretation is recorded for later compatible route consumption.
- `localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml`
  - Replaced retired Ledger terminology in every live evolution option and obligation tooltip.
- `localisation/english/015_utopia_manifesto_l_english.yml`
  - Completed the emergency levy extension cost triplet with its exact material and stability costs.
  - Updated the Ledger subtitle and active band/status wording.
  - Removed the unreferenced legacy decision/mission package from `decision_utopia_household_census` through `mission_utopia_renunciation_vote`, its matching legacy tooltip block, and the dead `utopia_open_stores_cost_text` triplet.
- `localisation/english/015_utopia_manifesto_country_package_l_english.yml`
  - Removed retired meter readings from live character and achievement prose while preserving current route and achievement names.
- `localisation/english/015_utopia_manifesto_focus_l_english.yml`
  - Reworded material-surplus prose as full stores or material excess. Current Consent of Households route names remain intact.
- `localisation/english/015_utopia_manifesto_ideas_l_english.yml`
  - Replaced the retired Surplus-branded idea name and ambiguous civic uses while preserving current route identity.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/localisation_completion_handoff_2026_07_15.md`
  - This handoff.

No gameplay, interface, asset, spreadsheet, or other-event file was changed by this worker.

## Stale-vocabulary audit

| Retired wording | Liveness result | Action |
| --- | --- | --- |
| Consent as a Ledger value | Live evolution and decision text still used it; the old decision package also contained dead uses | Rewrote live meter consequences as Concord and, where appropriate, movement toward Choice. Removed the dead package. |
| Surplus as a Ledger value | Live evolution, band, idea, aid, event, focus, and achievement text still exposed it | Rewrote the Ledger value as Plenty and rephrased genuine material excess as full stores, excess stores, or material aid. |
| Overreach | Survived only as retired meter language or ambiguous assignment wording | Rewrote live consequences as movement toward Assignment or coercive assignment. Removed dead legacy uses. |
| Vocation Balance | Survived in live evolution text and the dead decision package | Rewrote live consequences as Choice versus Assignment moving toward Choice. Removed dead legacy uses. |
| Foreign Suspicion | Found only in the unreferenced legacy decision and tooltip package | Removed with that package. |
| League Confidence | No live English value occurrence was present | No replacement required. Live League cohesion wording remains because cohesion is a separate implemented League system, not a Ledger value. |
| contradiction meter | No live English value occurrence was present | No replacement required. |

The final English value scan has zero occurrences of Surplus, Overreach, Vocation Balance, Foreign Suspicion, League Confidence, or contradiction meter. Hidden script/localisation identifiers containing tokens such as `_surplus_` were not renamed because they are stable engine-facing identifiers, not player-facing wording.

Thirteen player-facing uses of `Consent` remain intentionally. They are current proper names for the Consent of Households route, route-specific focuses, the `Consent of the Governed` achievement, or explicit route comparisons. None describes a Ledger scalar or says that Consent rises, falls, is high, or is low.

## Accuracy notes

- Fixed custom costs state the consumed material values and the separately displayed Political Power cost.
- Shared case-conversion cost text explicitly distinguishes lease and joint-administration material profiles.
- Dynamic military and institutional tooltips display the live initialized cost variables used by the corresponding payment effects.
- Timed outcomes disclose prepared durations when the duration is player-visible, including the emergency levy, pre-fire domestic repair range, and 30-day foreign-support planning credit.
- Targeted decisions identify transferred equipment, recipient consequences, territory-control rules, route selection, mission cancellation, and cleanup behavior where those consequences are implemented.

## Validation

- Rebuilt the required-key set from all three Event 015 decision files, the Event 015 decision-category file, and `events/015_utopia_manifesto.txt`: 1,287 required, 0 missing.
- Checked all nine `015_utopia_manifesto*.yml` files: 9 of 9 have a UTF-8 BOM.
- Exact case-sensitive duplicate localisation keys: 0.
- Localisation lines with leading key whitespace: 0.
- Versioned `:0` keys: 0.
- Malformed one-line localisation entries: 0.
- Retired metric phrases in player-facing values: 0, subject to the intentional Consent proper-name classification above.

## Risks and parent review notes

- Event 015 source was changing concurrently. The parent should retain the final source-to-localisation inventory check after all other Event 015 workers finish, because a later gameplay edit can introduce a new key after this handoff.
- `utopia_manifesto_cost_case_conversion` is intentionally shared by two decisions and therefore describes both exact alternatives in one tooltip.
- Dynamic formation and institutional strings depend on the existing cost-preparation effects initializing their displayed country variables before the decision tooltip is evaluated.
- Case-only key pairs such as the uppercase cosmetic-country identity and lowercase idea identity are intentional distinct localisation keys. The exact case-sensitive duplicate count is zero.

## Simplifications, omissions, and blockers

None. Every key referenced by the current scoped gameplay surface is localised, and no fallback text or placeholder was used.

## Skills and references used

- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- Required offline Paradox wiki pages, including Localisation, Decision Modding, Event Modding, Triggers, Effects, Scopes, and Data Structures
- Vanilla localisation formatting, scripted object, script concept, and custom tooltip documentation and precedents
