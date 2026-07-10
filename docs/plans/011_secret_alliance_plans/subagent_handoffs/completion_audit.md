# Event 011 Secret Alliance final completion audit

Date: 2026-07-10

## Verdict and evidence boundary

**Final static completion verdict: FINAL CLEAN.**

Event 011 engine-compatible gameplay is frozen in commit `407b9a05eb7024dd1728c4092fba2f1162efde9c`, atop high-impact balance commit `1c87d923`, documentation reconciliation `02decf32`, lifecycle closure `a1f47c0c`, callback isolation `7563648f`, and wording and catalog reconciliation `97a2da80`. The decision and mission audit findings DM-15 through DM-20 are closed. Completion findings CA-01 through CA-13 are closed. The final localisation and workbook audit is FINAL CLEAN.

This report is the holistic verdict owner named by the Event 011 documentation map. It compiles source, audit, localisation, workbook, asset, audio, achievement, and plan-disposition evidence. It does not claim an in-engine playtest.

## Frozen evidence

| Surface | SHA-256 |
| --- | --- |
| `common/script_constants/011_secret_alliance_constants.txt` | `2A635EE58242229ABC9D265991A74E52B25B88188719C1AB87DC31B239BEEF21` |
| `common/scripted_effects/011_secret_alliance_effects.txt` | `10B03E949BC56497065C8BCDAB8D025D2D601C1C9AD604F4D954D637FAB4FFF1` |
| `common/decisions/011_secret_alliance_decisions.txt` | `B22CC92AAF15F13860A9FDEB56520B03F6E78D479EE6F5F62DFC07221CA5B921` |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | `A228DC3BBB7D7AABDE115B30D01F3B983D9FAF4C47019D46E3C7C534CA164087` |
| `common/ideas/011_secret_alliance_ideas.txt` | `D9C0C4D8128896E04AAD9D61445A81378F4F35F0A12135090851653B7B652D02` |
| `common/mtth/011_secret_alliance_mtth.txt` | `8CE980BF54FCF404BA643555C02DA2799CAF2BDC533925507CA2DD918538BA8A` |
| `events/011_secret_alliance.txt` | `02046301A3157FF36A46147E7C058E63A8A5D7ACB27018BEEAF49C2388938904` |
| `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` | `51F25FE38E06E6787AB38B975AC2D64C00F5260BB159A3ABD30B9989D6CC2980` |
| `common/scripted_guis/011_secret_alliance_scripted_gui.txt` | `C07907E21CBC30B267C1AC4D2112F494E9748FC44B936C9081B5F4E044B699FA` |
| `localisation/english/011_secret_alliance_l_english.yml` | `6A42CEFE3DBAD7EFD2A3C7DD615F0F32E4DB9C3B2E768A11CBFB3E7FCC42434F` |
| `localisation/english/chaosx_achievements_l_english.yml` | `6EE16E2B3E81C1292595F3F285C209C13F24C6F41D2FC073D72381D643244C4D` |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `597E71A1307958135BA1B34A8E60741320CD9E2753FA2EBDDBC1ED83403E1D59` |

## Implemented event contract

- Event 011 remains Minor Fire-Once, begins from three valid AI minor founders, prefers factionless candidates, fixes the human target for the run, and is not part of a cluster.
- The concealed pact uses durable member, founder, sponsor, suspect, confirmed, turned, and public-member state. Recruitment preserves human consent and the dynamic safe-pool ceiling.
- Baseline progression and Evolutions I through III are distinct. Evolution II adds sponsor and counter-network play. Evolution III resolves controlled, player-forced, fractured, weakened, preemptive, or hostile-war public routes through one guarded reveal transaction.
- Six stored operation families, source-aware Evidence, six independent clue classes, suspect corroboration, maintained Preparedness, exact protected states, and factual Coalition Resolve are implemented.
- Seven named investigation missions have final timeouts of 150, 135, 190, 150, 190, 100, and 140 days. Their full, partial, failure, cancellation, expiry, slot, state, and suspect cleanup paths are covered by the final decision audit.
- Live family caps are two investigations, one protection, one diplomacy, one offensive action, one border action, and one emergency action.
- Public reveal creates the real dynamic Anti-[target] faction, applies route-aware leadership, performs guarded member calls, preserves planned exits where appropriate, and rolls back failed creation or mandatory hostile-war calls.
- Event Log history is automatic-origin only. Scenario, debug, forced, and AI-test origins do not manufacture normal history or normal-route achievement credit.
- Counted `.50` through `.53` callbacks and pending `.190`, `.201`, and `.202` state must drain before relaunch. Invitations, sponsors, delayed notices, scenario presentation, and reveal presentation are target and phase safe.
- SCN-009 Coalition Unmasked has five AI-only compositions and Low, Medium, High, and Maximum intensities with viable-pool checks, immutable composition snapshots, and explicit abort rather than substitution.

## Final balance contract

- Dynamic base packages are 24 Command Power, 15 Army Experience, 300 support equipment, 30 trains, 200 trucks, 20 convoys, 1,000 fuel, 7,500 manpower, and 75 Political Power.
- Small and large industry, army, and territory checks are mutually exclusive within each dimension. The maximum live mixed profile scales by `2.2425`. Its rounded 168 PP maximum is covered by the 170 PP AI planning hint.
- Repeated use does not apply a separate cost multiplier. Long cooldowns, slot occupancy, timed burdens, and resource costs control reuse.
- Preemption requires 65 percent War Support and spends 15, 10, or 6 percent according to Evidence. A false case also costs 8 percent Stability.
- Protection, Turn Member, and wartime direct-AI cooldowns are 120, 180, and 120 days.
- Diplomacy, offensive, and emergency commitments occupy their slots for 90, 120, and 180 days. Retained counterintelligence scales with preserved Preparedness and is capped at 730 days.

## Audit closure

| Audit range | Final disposition |
| --- | --- |
| DM-15 through DM-20 | Closed. Public-war-start gating, mission-aware phase cleanup, suspect-bound border pairs, valid envoy objectives, revealed cost refresh, and exact AI protection-state selection are present. |
| CA-01 through CA-13 | Closed. Route-aware leadership and exits, exact border transactions, repeat-turn prevention, preemption preservation, explicit fractured wording, lifecycle-safe pending transactions, delayed-event gates, origin-safe achievements and Event Log history, durable reveal presentation, per-run Sponsor Accountability, and callback draining are present. |
| Engine compatibility | Closed. Eight calls use documented `has_added_tension_amount`, all idea modifiers use 39 defined file-local constants, and the former unsupported script-constant entries were removed without changing their values. |
| Localisation and workbook | FINAL CLEAN. Event 011 localisation matches final balance values, all six achievement tooltips resolve, Event 011 and SCN-009 are `Implemented`, and no formula error cells or formula error tokens remain. |

## Presentation, assets, audio, and achievements

- Super-event slot `73` has hostile-war, pact-controlled, player-forced, fractured, and weakened descriptions. Durable presentation target, leader, route, member count, and faction-name grammar last through the 14-day slot and are cleared on day 15.
- Audio ID `43` uses `Revelation` by William Paris Chambers, performed by the United States Marine Band under Col. John R. Bourgeois. Composition and federal-government recording rights are documented separately. The final OGG and WAV are both `86.101746` seconds at 44.1 kHz.
- The validated visual package contains 57 runtime DDS targets, 38 transparent assets, 17 unique decision sources, seven unique idea sources, eight authored confrontation-emblem source frames, eight processed frames, one still fallback, and six achievement triplets. The final balance commit changes no asset or audio path.
- The Empty Chair, Every Thread, Their Man in the Room, Divide the Table, Surrounded, Not Buried, and Two Giants, One Grave use durable origin, evidence, membership, capital, fracture, scenario, and outcome facts. Forced/debug origins are disqualified, the relevant scenario restrictions are explicit, and every tooltip requires the player not to capitulate.

## Documentation and workbook closure

- `docs/events/011_secret_alliance.md` is the canonical mechanic and registration overview.
- `docs/specs/011_secret_alliance_specs/` is retained as implemented source design. Its prompts and planning handoffs are marked fulfilled or historical so they cannot be mistaken for open work.
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_resolution.md` closes every accepted implementation-improvement tranche and acceptance scenario.
- `docs/assets/011_secret_alliance/`, `docs/super_events/011_secret_alliance_super_event_research.md`, and `docs/achievements/011_secret_alliance_achievements.md` retain the verified asset, presentation, audio, and achievement facts.
- Workbook hash is `597E71A1...`. `Events!M12` and `Scenarios!F9` are `Implemented` with no formula errors recorded by the final spreadsheet audit.

## Plan and handoff disposition

| Material | Disposition |
| --- | --- |
| Five-part source specification and matrices | Promoted and implemented. Retained as historical source design. |
| `011_secret_alliance_implementation_improvement_addendum.md` | Implemented and fully disposed through the improvement resolution. |
| `011_secret_alliance_high_impact_balance.md` | Implemented and frozen at `1c87d923`. |
| Super-event text and audio handoffs | Promoted and implemented. Early Luke and Hamlet candidate material is superseded. |
| Asset production and routing handoffs | Promoted and implemented. No asset remains blocked or unwired. |
| Original coding, decision, achievement, asset, super-event, and goal prompts | Fulfilled and retained only as historical work orders. |
| Early no-manual-scenario direction | Rejected and superseded by implemented SCN-009. |
| New focus tree, country package, formable, world-end branch, second super-event, and additional animated UI | Rejected or excluded by the accepted anti-bloat boundary. They are not accepted omissions. |
| Optional country-specific incidents, later cross-event hooks, and postwar flavour | Queued only as optional future ideas. They are outside the accepted completion boundary. |

## Simplifications, omissions, and blockers

No accepted route, evolution, decision family, mission, scenario type, scenario intensity, achievement, animation fallback, visual package, audio package, localisation surface, or workbook field is omitted or replaced by a fallback. No unapproved simplification is recorded.

Remaining blockers: none within the accepted Event 011 scope.

Validation boundary: this is static source and artifact evidence. No in-engine playtest is claimed.
