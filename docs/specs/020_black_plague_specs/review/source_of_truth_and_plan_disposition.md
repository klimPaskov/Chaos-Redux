# Source of Truth and Plan Disposition

## Source-of-truth status

After user acceptance, the files under this `020_black_plague_specs` folder should become the Event 20 design source of truth.

The obsolete catalog rows remain historical records. The live implementation registers Event 20 in the Diseases cluster (`8`) and the triggerable scenario as `SCN-012`; the workbook and exported snapshots carry those accepted identifiers.

## Spec hierarchy

1. Main event specs in `specs/`
2. Detailed matrices in `matrices/`
3. Focus architecture guides in `focus_graphs/`
4. Production and implementation prompts in `prompts/`
5. Research evidence in `research/`
6. Manual planning reviews and limitations in `review/`

When two files appear to conflict, the later user corrections and Part 9 control the triggerable scenario. The detailed matrices control implementation detail unless a main spec states a stronger rule.

The 2026-07-29 two-tag correction supersedes every earlier multi-tag Rat Nation pool: `RTA` is the only reusable Rat Nation carrier, `RTX` is the separate Rat King, and additional broods are state-level markers, infestation, mass, and pulse state inside `RTA`.

The current static runtime ledger records 52 RTA focus nodes and 71 RTX focus nodes, native `activate_mission`/`days_mission_timeout` declarations for Hold the Line, Secure the Refuge, Crown Strike, and Seal Royal Burrows, five paid post-defeat recovery, inspection, condemnation, population, and memorial projects, the dedicated weapon-delivery icon, promoted source-frame Rat King, Royal Burrows, Severe/Collapsed crisis seal, and Rat King terminal-readiness seal packages, and three 44.1 kHz Event 020 WAVs. One shared rat ground-unit model/entity package is promoted for six RTA/RTX subunits and five locked division templates; no per-subtype or separate Rat King model is authorized. Sound-definition wiring, counter review, live playback, scenario rollback, mission, balance, rights, and whole-spec validation remain open.

## Plan disposition

| Item | Disposition |
| --- | --- |
| State-based origin and disease lifecycle | promoted into main spec |
| Shared crisis board and existing disease mapmode | promoted into main spec |
| Black base colour for established Black Plague states | promoted into Part 2, matrices, prompts, and acceptance criteria |
| Black fog | optional engine-dependent enhancement with explicit blocker rule |
| Dynamic shared containment decisions | promoted into main spec and matrix |
| Black Plague-specific decisions inside the shared disease category | promoted into Part 2, decision matrix, prompts, and acceptance criteria |
| Rat Infestation selected-state value | promoted into main spec and matrices |
| Countermeasure and Doctor Wu bridge | promoted into main spec |
| Long weaponization project | promoted into main spec and prompts |
| Five evolutions | promoted into main spec and matrix |
| Rat Nation country package | promoted into main spec and matrices |
| Rat King country package | promoted into main spec and matrices |
| World-end path and terminal scenario | promoted into main spec and focus architecture |
| Instant-chaos triggerable scenario | promoted into Part 9, scenario matrix, prompts, AI, catalog draft, and acceptance criteria |
| Triggerable scenario forcing Evolutions I through IV | accepted as a scoped manual bootstrap exception |
| Triggerable scenario automatically setting Evolution V or world end | rejected so terminal victory remains earned |
| Dedicated Black Plague national-response category | accepted by the 2026-08-09 correction; owns cure, logistics, cooperation, knowledge, and recovery while shared selected-state containment remains intact |
| One bespoke tree per base rat tag | rejected in favor of one deep shared tree with origin archetypes |
| Ordinary human-rat diplomacy | rejected because it weakens the hostile nonhuman role |
| Defeat aftermath super-event | implemented statically with an explicit duration/peak/deaths/major-participant gate, slot-087 art/text/audio/sprite/sound wiring, and runtime resolver dispatch; live validation and release attribution remain open |
| 2026-08-01 consequence, hierarchy, and aftermath addendum | core tranche implemented statically: RTA hierarchy graph and `.45` acknowledgement, RTA Hunger/Coherence/Disease Dominion meters with staged Fractured Instinct and `.46` crisis handling, RTX crises `.57-.59`, Crown Strike `.64-.65`, ten route-specific RTA/RTX operations including the three hierarchy actions, scoped defeat participant hooks/metrics, resolver-owned `.72`, `.71/.73-.75` aftermath, 51-focus RTA depth, 71-focus RTX depth, and catalog alignment are present; native last-response and Crown/Seal mission declarations, dedicated weapon-delivery icon, source-frame Rat King/Royal Burrows/Severe-Crisis/terminal-readiness seal packages, and three 44.1 kHz WAVs are promoted; dedicated crisis report, Doctor Wu, route art, rights attribution, and live validation remain queued |
| Hold the Line and Secure the Refuge | implemented statically as native `activate_mission`/`days_mission_timeout` missions in `common/decisions/020_black_plague_shared_response_decisions.txt`; live outcome and timeout validation remain open |
| Crown Strike and Seal Royal Burrows | implemented as state-selected zero-day launchers plus native `activate_mission`/`days_mission_timeout` missions with explicit state markers, factory reservation, cancellation, shared-action resolution, and terminal cleanup; live outcome, timeout, and factory validation remain open |
| Dedicated weapon-delivery icon | promoted and wired as `GFX_decision_black_plague_weapon_delivery`; no Military Acceleration alias remains the active contract |
| Source-frame Rat King portrait and Royal Burrows seal | promoted and wired through their manifests and GFX entries; static fallbacks remain registered where documented |
| Severe/Collapsed crisis seal and Rat King terminal-readiness seal packages | promoted and wired through `interface/020_black_plague_rat_identity.gfx`; the crisis pair is gated by the shared-board Severe/Collapsed trigger and tooltip, while the terminal pair is consumed by the RTX final-order decision; no separate terminal-readiness scripted-GUI panel is present |
| Event 020 audio | three promoted WAVs (IDs 101, 102, and 103) are 44.1 kHz stereo; release attribution and live playback remain open |
| Shared rat ground-unit model package | promoted from `rat_ground_unit_shared_3d_model_brief.md` and the 2026-08-05 worker handoff; one `black_plague_rat_mesh`/`black_plague_rat_entity` package serves six RTA/RTX subunits and five locked templates, while per-subtype and separate Rat King models remain rejected | Parent-owned sound-definition wiring, counter visual review, and live in-game consumer validation remain open |

## Future addenda

A new planning addendum is justified only when live implementation reveals an engine limitation, a registry conflict, or a missing design question that cannot be resolved from this pack. Do not create another broad improvement layer while this source spec remains the accepted authority and the current implementation tranche remains incomplete.
