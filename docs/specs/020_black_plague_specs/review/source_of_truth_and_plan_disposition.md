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
| Dedicated Black Plague decision category | rejected as duplicate UI ownership |
| One bespoke tree per base rat tag | rejected in favor of one deep shared tree with origin archetypes |
| Ordinary human-rat diplomacy | rejected because it weakens the hostile nonhuman role |
| Defeat aftermath super-event | implemented statically with an explicit duration/peak/deaths/major-participant gate, slot-087 art/text/audio/sprite/sound wiring, and runtime resolver dispatch; live validation and release attribution remain open |
| 2026-08-01 consequence, hierarchy, and aftermath addendum | core tranche implemented statically: RTA hierarchy graph and `.45` acknowledgement, RTA Hunger/Coherence/Disease Dominion meters with staged Fractured Instinct and `.46` crisis handling, RTX crises `.57-.59`, Crown Strike `.64-.65`, seven route-specific RTA/RTX operations, scoped defeat participant hooks/metrics, resolver-owned `.72`, `.71/.73-.75` aftermath, 50-focus RTA depth, 70-focus RTX depth, and catalog alignment are present; native-mission API review, dedicated crisis/Doctor Wu/route art, rights attribution, and live validation remain queued |

## Future addenda

A new planning addendum is justified only when live implementation reveals an engine limitation, a registry conflict, or a missing design question that cannot be resolved from this pack. Do not create another broad improvement layer while this source spec remains unimplemented.
