# Foreign reactions

After an Independence Wave report, the governments with a real stake in the new states each answer once: neighbors decide their frontier posture, regional powers weigh guarantees, mediation and investment, great powers set a precedent, and earlier-wave states choose solidarity or rivalry.

## Accepted design

Acceptance basis: the accepted contract `docs/specs/006_independence_wave_specs/specs/006_foreign_reactions_and_remnant_petitions_contract.md` (user selections of 2026-09-27 and the 2026-10-03 continuation instruction), implemented under the agent decisions recorded in `docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md` (D2, D3 and D4).

## Flow

1. The public report `chaosx.nr6.2` raises the report/reset barrier, the country openings resolve, and every former host answers through the host response (`host_response.md`).
2. The final host-response callback, `independence_wave_host_response_finish_plan`, calls `independence_wave_foreign_reaction_build_queue` before it clears its own receipts.
3. The builder freezes the committed Event 006 cohort in report row order and collects candidate governments only from bounded sources: each target's registered package contacts (`package_contacts.md`), gathered first so the actor cap never drops them, then its neighbors, its recorded patrons and the governments that already recognized it, the allies of its living former host (faction members, overlord and subjects), and the active Event 006 countries of earlier waves.
4. A candidate must be living and sovereign, must not belong to the cohort, and must not be a host answering this wave through its own host response. A pair is invalid when the candidate is the target, its former host, or at war with it.
5. Each pair is scored once per interest family: direct stake 4, recorded relationship 3, strategic fit 2, political fit 1, and one conflict penalty of -3, with a floor of 0.
6. Each actor keeps its highest-scoring target; an equal score keeps the earlier report row. An actor at 6 or more receives one receipt for this wave.
7. Hidden router `.64` reaches each actor one day after the previous one, starting one day after the host phase. It re-checks the receipt and the live score, sends a human the profile event, and resolves an AI actor through deterministic policy.
8. A human actor has 13 days to answer; the first option, the noncommittal stance, is chosen when the window closes.
9. A patron offer leaves the actor's receipt open until the released country answers through `.71` (human, 13 days, refusal by default) or the router (AI).
10. The last receipt closes the queue and releases the report/reset barrier. A deadline event `.72` on every target closes a queue whose receipts outlived every answer. Each target stores the date from which its queue may close, so a deadline left over from an earlier queue cannot close a newer queue on the same target, and `on_annex` consumes the receipt or open offer of an annexed country.

No daily, weekly or monthly hook and no world scan is used. The opening of the queue never depends on a random roll.

## Interest families

| Family | Points | Facts |
| --- | --- | --- |
| Direct stake | 4 | Shared frontier; a claim on a state the target owns; an existing guarantee of the target |
| Recorded relationship | 3 | A registered package contact of the target; a patron channel with the target; an earlier recognition of it; Independence Network membership; an alliance with the target; an alliance with its former host |
| Strategic fit | 2 | Military access in either direction; a border with the former host but not with the target; an earlier-wave state in the same Event 006 region |
| Political fit | 1 | Both governments in the same ideology group |
| Conflict | -3 | The actor is at war; or it has already recognized and guaranteed the target |

Major status alone adds nothing: a great power must first enter the pool through a package contact, neighbor, patron, recognition, alliance or earlier-wave source, and its continental reach is not a scoring fact.

## Profiles and stances

The profile follows the contract's priority: an active Event 006 country uses the earlier-wave profile, then a great power with an actual contact (a recorded relationship, which includes a registered package contact), then a regional stakeholder (a registered package contact, strategic fit, or no shared frontier), then a local neighbor. A great power without a contact takes the profile its other facts give it.

| Event | Stance | Cost | Result |
| --- | --- | --- | --- |
| `.65` neighbor | Watch the frontier | None | No change |
| `.65` neighbor | Recognize and open a liaison office | Light diplomatic, free when it settles the target's own recognition mission | Shared recognition receipt; Legitimacy and Recognition; host hostility and pressure rise; public history |
| `.65` neighbor | Sponsor border talks | Standard diplomatic | Bilateral ledger moves toward settlement; Legitimacy up, Instability down; public history |
| `.65` neighbor | Stand with the former host | Light diplomatic | Recognition down, Instability, hostility, pressure and reconquest fear up; host goodwill; public history; no war |
| `.66` regional | Withhold support | None | No change |
| `.66` regional | Guarantee its independence | Standard diplomatic, free when it settles the target's own request; needs ten divisions and reach | Real guarantee and the DM-13 award, once |
| `.66` regional | Offer to mediate | Standard diplomatic | As border talks |
| `.66` regional | Invest in the transit corridor | Standard diplomatic | Corridor offer: on consent, capital infrastructure and Capacity with a trade channel |
| `.67` great power | Abstain | None | No change |
| `.67` great power | Extend recognition and limited aid | Light diplomatic plus infantry equipment from stock | Recognition as above plus Security |
| `.67` great power | Offer an arms channel | Standard diplomatic | Arms offer: on consent, equipment from stock and an arms channel |
| `.67` great power | Organize containment | Standard diplomatic | As standing with the former host |
| `.68` earlier wave | Stand aside | None | No change |
| `.68` earlier wave | Recognize it and share institutions | Light diplomatic | Recognition plus Capacity and network standing for both |
| `.68` earlier wave | Send aid | Light command power plus equipment from stock | Security (more at war or under severe threat), Instability down, network standing for both; public history |
| `.68` earlier wave | Contest its standing | Light diplomatic; needs a claim on its land | Legitimacy and Recognition down, Instability up; private |

A stance that stops qualifying between the popup and the click resolves as the noncommittal stance, so no cost is ever paid without its effect.

### Shared bilateral receipts

Recognition and guarantees use the generation-matched receipts introduced for the paid diplomatic decisions (`independence_wave_record_recognition_receipt`, `independence_wave_apply_bilateral_guarantee`), so a foreign answer and a decision for the same pair never award Statehood progress twice.
When the released country already paid for a recognition mission or a guarantee request to the same government, the foreign answer settles that mission at no further cost and the decision later awards nothing.
An earlier-wave state with a recognition campaign running for the same member waits for that campaign instead of offering recognition again.

## AI policy

The AI is deterministic and uses the same availability triggers and costs as the player.

- Neighbor: contain when allied with the former host; recognize on shared ideology or alliance; otherwise mediate at peace; otherwise recognize.
- Regional: an ally of the former host mediates or withholds; otherwise guarantee at peace with shared ideology, a patron channel or an alliance; otherwise invest; otherwise mediate.
- Great power: contain when allied with the former host; otherwise offer arms on shared ideology; otherwise recognize with limited aid.
- Earlier wave: contest a claimed rival of a different ideology; aid a threatened or warring newcomer; otherwise share institutions; otherwise aid.
- Consent: accept while the strongest foreign influence is below the dominance warning, accept a smaller arrangement below dependency, refuse beyond it.

AI choices also add `befriend`, `protect`, `contain` or `antagonize` AI strategies toward the target, and `befriend` toward a host it backs.

## History and Event Details

Public outcomes write one Event 6 history row with the released country as the primary actor and the foreign government as the counterpart: recognition (payload 30), guarantee (31), mediation (32), containment (33) and aid (34).
The description entries live in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and the text in `localisation/english/006_independence_wave_foreign_reaction_l_english.yml`.
Patron bargaining, refusals and rivalry stay private.

## Assets and localisation

All windows reuse `GFX_report_event_006_asset_001_wave_summary` (registered in `interface/006_independence_wave_small_assets.gfx`).
No new art, icon or GUI is required.
Opinion modifiers are defined in `common/opinion_modifiers/006_independence_wave_opinion_modifiers.txt`.
Dynamic reason, host and cost text lives in `common/scripted_localisation/006_independence_wave_foreign_reaction_localisation.txt`.

## Implementation

- Events: `events/006_independence_wave_foreign_reaction_events.txt`.
- Effects and their reference: `common/scripted_effects/006_independence_wave_foreign_reaction_effects.txt` and `.md`.
- Triggers: `common/scripted_triggers/006_independence_wave_foreign_reaction_triggers.txt`.
- Constants: `common/script_constants/006_independence_wave_foreign_reaction_constants.txt`.
- Barrier hand-off: `independence_wave_host_response_finish_plan` and `independence_wave_host_response_release_report_barrier` in `common/scripted_effects/006_independence_wave_host_response_orchestration_effects.txt`.
- Annexation cleanup: the Event 006 `on_annex` block in `common/on_actions/006_independence_wave_on_actions_registry.txt`.

## Coverage limits

- No admitted package carries an authored foreign-contact profile yet, so the package-contact source contributes nothing; the bounded live sources above carry the queue.
- Engine guarantees given to the target's former host cannot be enumerated, so a guarantor of the host qualifies only through another source.
- Live verification of the hidden routing, the timeout defaults, and tag-targeted receipts inside the stance chain is required in game.

## Remnant petitions

A remnant former host that chose legal continuity (`.62` first option) or a regional charter (`.62` second option) may ask one foreign government to guarantee what is left of its territory.

1. The remnant host response consumes `independence_wave_host_response_outside_guarantee_opportunity_open` through `independence_wave_remnant_petition_open_window`.
2. If the host has not petitioned before in its current identity, the host's neighbors, then its allies, are ranked with the same 4/3/2/1 families against the host: frontier, alliance, access, shared ideology, and the -3 penalty for war or a claim on the host's land. The first highest-scoring government at 6 or more becomes the named recipient.
3. With a recipient, a 30-day window opens the decision "Petition [recipient] for a Guarantee" in the category "A Foreign Guarantee". The host pays the standard diplomatic cost. The AI takes it only under a real threat: war, or a neighbor holding or justifying a war goal against it.
4. The recipient answers in `.69` (13 days, declining by default) or, as AI, through the hidden router: it guarantees at peace when allied with the host or sharing its outlook and when it can pay the standard cost, has more than ten divisions and can reach the host.
5. Acceptance creates the real engine guarantee, and only then does the host grant the recipient military access, its promised concession. Declining or an invalid petition creates no protection. `.70` tells the host the result.
6. A recipient answers at most one petition per wave, a state released from the host is never asked, and a government that already guarantees the host is not asked again.
7. The host may petition once per country identity: the flag `independence_wave_remnant_petition_used` is cleared only when the country is annexed or released again. An unused window simply expires.

Petitions protect the host and never recognize or reward a released country. An accepted petition writes Event 6 history payload 35 with the host as the primary actor and the guarantor as the counterpart.

The petition reuses `GFX_report_event_006_asset_002_host_crisis` for `.69` and `.70`, the existing diplomacy category icon and recognition decision icon, and the opinion modifiers `independence_wave_remnant_petition_guarantor` and `independence_wave_remnant_petition_refused`.
Source: `common/decisions/006_independence_wave_foreign_reaction_decisions.txt`, `common/decisions/categories/006_independence_wave_foreign_reaction_categories.txt`, and the petition sections of the foreign reaction effects and triggers.

## Future plans

- Package-authored contact profiles for admitted packages (named sponsors, corridors, old claims) to feed the relationship and strategic families.
- A summary news item that groups low-interest attention by region.
