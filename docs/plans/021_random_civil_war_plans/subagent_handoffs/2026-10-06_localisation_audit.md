# Event 021 localisation audit handoff — 2026-10-06

Disposition: implemented audit; parent review required. This is a read-only localisation and presentation review. No gameplay or localisation files were edited.

## Evidence reviewed

- `localisation/english/021_random_civil_war_adaptation_l_english.yml`
- `localisation/english/021_random_civil_war_l_english.yml` and its current diff
- `common/scripted_localisation/021_random_civil_war_localisation.txt`
- `events/021_random_civil_war_adaptation_events.txt`
- `common/decisions/021_random_civil_war_adaptation_decisions.txt`
- `common/ideas/021_random_civil_war_adaptation_ideas.txt`
- `common/scripted_effects/021_random_civil_war_regional_response_effects.txt`
- `common/scripted_triggers/021_random_civil_war_adaptation_triggers.txt`
- `common/script_constants/021_random_civil_war_regional_constants.txt`
- Relevant category/status and history-summary layout in `common/scripted_localisation/021_random_civil_war_localisation.txt` and `interface/chaosx_events_log_popup.gui`.

`python .tools/report_colour_audit.py --event 021` returned `total keys with colour: 0`. This covers every visible report/news event title and description chain rooted in event files with the audit tool’s recursive scripted-localisation traversal. The adaptation report title and body themselves also contain no colour formatting.

## Findings

Parent verification: `£support_equipment_text_icon` is defined by the existing Chaos Redux sprite at `interface/chaosx_texticons.gfx:90`, using `gfx/texticons/support_equipment_text_icon.dds`.
Its attribution below as a vanilla-style token describes appearance rather than vanilla ownership.
The final intervention tooltip says relations recover gradually, consistent with the opinion modifier's monthly decay.
The compact history summary is the accepted D41 presentation choice, retaining outcome fields while keeping force bookkeeping in the immutable arrays.

- No blocking wording or mechanics mismatch found in the adaptation package. Decision cost displays and affordability gates match their debits: 15 army experience and 200 rifles for adaptation; 30 command power, 1,500 rifles, and 100 support equipment for mobilization; 25 political power and 50 support equipment for exposing intervention. The corresponding constants and spend values agree. Timed effect descriptions match the ideas’ modifiers and durations (90 days for adaptation and 60 days for mobilization). The mobilisation tooltip’s 2 percentage point recruitable-population claim matches `conscription = 0.02`; its stability and consumer-goods penalties match the idea.
- `£support_equipment_text_icon` is the established vanilla-style text-icon token spelling and is used in the newly added cost strings. It is consistently used for the support-equipment charges. This review did not establish standalone asset wiring is needed for that vanilla token.
- The exposure status line now shows the current stage (`Observed`, `Pressured`, `Penetrated`, or `Mobilizing`) and the named source. Its scripted selector reads the exposed country’s stage variable and falls back to `Observed`. `event021_country_can_manage_exposure` limits that status surface to an exposed country with a still-active source crisis, and the adjacent summary explains the real border effects. This is honest about the neighbor’s current stage; it does not imply the neighbor itself is at war.
- Border-monitoring and mediation tooltips now say they lower exposure by one stage and hold it there while active. That aligns with the relevant contain/refresh helpers and the exposed country’s visible stage. The prose stays player-facing; it does not expose internal meter names or variable identifiers.
- The intervention tooltip says the sponsor’s military commitment ends, opinion falls by 30 and recovers by one point per month, and already delivered arms remain. The effect clears the sponsor commitment receipt and installs the opinion modifier with value -30 and decay 1. No discrepancy found.
- Adaptation descriptions are short, direct prose. The event title/body avoid implementation jargon; option labels are clear. Decision and event text use sentence punctuation where they are full sentences, while option labels and cost rows are correctly kept as short labels/fragments.
- The shortened `event021_event_log_snapshot_summary` preserves claimant, route/cause, severity, capital, front count, settlement/obligation, sponsor/recipient, opening status, and scenario. The event row already carries its date, and the host is in the new heading, so removing the redundant date/host labels is reasonable. It no longer shows rival-authority archetype, connected-state count, opening stronghold, opening force/army/navy/air ratios, equipment band, priority front, or independence-package line. Those omissions reduce the campaign’s retrospective detail; parent should decide whether this compact summary is meant to be a concise result card or still a full crisis record.
- Source layout indicates the event-detail text sits in a 420 px content area inside a 440 px scroll viewport, with a 740 px content height and vertical scrolling. The new summary is six compact lines and should fit the intended narrow detail surface more readily than the prior dense snapshot. This is source-level width evidence only; no in-game render was performed, so actual wrapping and visual fit remain unverified.

## Parent follow-up

No localisation patch is requested by this audit. If the compact-history goal is to retain more operational detail, consider restoring only one compressed field row (for example, connected states, equipment band, and priority front) rather than bringing back the former full force-ratio block. Otherwise the summary’s retained fields are coherent for a concise event detail.

No simplifications were made by this auditor. Remaining limitation: static source inspection cannot certify the live HOI4 text wrapping or stage rendering.
