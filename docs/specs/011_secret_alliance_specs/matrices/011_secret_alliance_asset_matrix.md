# Event 011 Secret Alliance asset matrix

## Static gameplay assets

| Asset | Type | Size | Source mode | Direction | Suggested sprite |
| --- | --- | --- | --- | --- | --- |
| Dossier category icon | Decision category icon | Existing category pattern | Generated icon | Sealed file, wax mark, faint diplomatic cords, no text | `GFX_decision_category_secret_alliance_dossier` |
| Trace pouches | Decision icon | 32x32 | Generated icon | Small diplomatic pouch with magnifier | `GFX_decision_secret_alliance_trace_pouches` |
| Turn courier | Decision icon | 32x32 | Generated icon | Hand passing folded paper in shadow | `GFX_decision_secret_alliance_turn_courier` |
| Break radio net | Decision icon | 32x32 | Generated icon | Broken radio signal coil | `GFX_decision_secret_alliance_radio_net` |
| Guard rail nodes | Decision icon | 32x32 | Generated icon | Rail switch with guard post | `GFX_decision_secret_alliance_guard_rail` |
| Harden plants | Decision icon | 32x32 | Generated icon | Factory with shield and rivets | `GFX_decision_secret_alliance_harden_plants` |
| Quiet talks | Decision icon | 32x32 | Generated icon | Two dark chairs and table lamp | `GFX_decision_secret_alliance_quiet_talks` |
| Face-saving exit | Decision icon | 32x32 | Generated icon | Open door behind treaty page | `GFX_decision_secret_alliance_exit_offer` |
| Border safehouses | Decision icon | 32x32 | Generated icon | Border post and hidden key | `GFX_decision_secret_alliance_safehouses` |
| War case | Decision icon | 32x32 | Generated icon | File folder over crossed bayonets | `GFX_decision_secret_alliance_war_case` |
| Unexplained diplomatic coldness | Idea icon | 64x64 | Generated icon | Frosted diplomatic seal and dim flagpoles | `GFX_idea_secret_alliance_coldness` |
| Foreign subversion | Idea icon | 64x64 | Generated icon | Shadow hand over rail and factory | `GFX_idea_secret_alliance_subversion` |
| Counter-conspiracy office | Idea icon | 64x64 | Generated icon | Lamp over files and string board | `GFX_idea_secret_alliance_counter_office` |
| Pact public hostility | Idea icon | 64x64 | Generated icon | Broken treaty and ring of foreign seals | `GFX_idea_secret_alliance_public_hostility` |
| Pact emblem | Faction emblem or UI emblem | Existing pattern | Generated symbolic emblem | Closed ring of three seals around a blank target marker, no text | `GFX_secret_alliance_pact_emblem` |

## Event images

| Asset | Type | Size | Source mode | Direction | Suggested sprite |
| --- | --- | --- | --- | --- | --- |
| Founding meeting report | Report event image | 210x176 | Generated documentary image | Period diplomatic room, three delegations with obscured faces, no readable text | `GFX_report_event_secret_alliance_meeting` |
| Courier captured report | Report event image | 210x176 | Generated documentary image | Railway platform or border office with seized pouch | `GFX_report_event_secret_alliance_courier` |
| Sabotage aftermath report | Report event image | 210x176 | Generated documentary image | Damaged factory floor or rail switch, period workers and soldiers | `GFX_report_event_secret_alliance_sabotage` |
| Public reveal news | News event image | 397x153 | Generated period news image | Delegations announcing a pact with target map blurred or symbolic | `GFX_news_event_secret_alliance_reveal` |
| Reveal super-event image | Super-event image | 457x328 | Generated image | Large shadowed diplomatic hall, public faction moment, target country implied through map shape without text | `GFX_super_event_secret_alliance_reveal` |

## Dossier Board UI assets

| Asset | Type | Source mode | State notes | Suggested sprite |
| --- | --- | --- | --- | --- |
| Board background | UI panel | Generated UI art | Static parchment and pinboard panel | `GFX_secret_alliance_board_bg` |
| Unknown member card | UI card | Generated UI art | Static | `GFX_secret_alliance_member_unknown` |
| Known member card | UI card | Generated UI art | Static | `GFX_secret_alliance_member_known` |
| Founder marker | UI badge | Generated icon | Static | `GFX_secret_alliance_founder_badge` |
| Patron marker | UI badge | Generated icon | Static | `GFX_secret_alliance_patron_badge` |
| Wavering marker | UI badge | Generated icon | Static | `GFX_secret_alliance_wavering_badge` |
| Evidence meter frame | UI meter | Generated UI art | Static with fill variants | `GFX_secret_alliance_evidence_meter` |
| Pressure meter frame | UI meter | Generated UI art | Static with fill variants | `GFX_secret_alliance_pressure_meter` |
| Preparedness meter frame | UI meter | Generated UI art | Static with fill variants | `GFX_secret_alliance_preparedness_meter` |

## Animated asset plan

| Asset | Target | Frames | Source mode | Motion state | Static fallback |
| --- | --- | ---: | --- | --- | --- |
| Radio pulse | Dossier Board alert | 8 | Generated frames | Vacuum-tube radio light pulsing when investigation available | `GFX_secret_alliance_radio_pulse_static` |
| Red thread glow | Dossier Board pressure state | 8 | Generated frames | Thread paths brighten as pressure rises | `GFX_secret_alliance_thread_glow_static` |
| Seal crack | Reveal-near warning | 10 | Generated frames | Wax seal develops cracks and faint light | `GFX_secret_alliance_seal_crack_static` |
| Border warning frame | Neighbor member card | 8 | Generated frames | Subtle border-card pulse when border operation available | `GFX_secret_alliance_border_warning_static` |

## Achievement icon motifs

Achievement icons should be 64x64 generated icons with completed, grey, and not-eligible variants if the achievement system requires them. See the achievement prompt for the full list.
