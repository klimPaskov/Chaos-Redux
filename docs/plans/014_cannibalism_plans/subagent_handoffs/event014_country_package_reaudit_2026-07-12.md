# Event 014 country-package final re-audit — 2026-07-12

## Verdict

Read-only final re-audit of the live Event 014 country-package implementation.

**Verdict: completion-ready for the country-package surface.**

- P0: 0
- P1: 0
- P2: 0
- P3: 0

All five P1 and three P2 findings from `event014_country_package_audit_2026-07-12.md` are closed in the current worktree. The additional defects found during this re-audit were repaired and rechecked before this verdict. No gameplay, localisation, asset, spreadsheet, skill, or existing documentation file was edited by this auditor. This report is the only auditor-created file, and no commit was created.

## Scope and references

The re-audit covered all eight reusable warlord slots, their origin territory and incarnation lifecycle, CBL creation and inheritance, the in-place original-ZZZ transformation, player-control safety, population and Larder accounting, technology continuity, units and recruitment, AI, characters, localisation, flags, and pre-reveal secrecy.

Required repository guidance was read first: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, and `hoi4-focus-trees`.

The offline `paradox_wiki/` snapshot was used rather than the online Paradox wiki. The core Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding pages were consulted together with the country, technology, division, portrait, equipment, and national-focus pages. Vanilla documentation under the installed HOI4 `documentation/` directory was also consulted, including effects, triggers, modifiers, dynamic variables, script concepts, script constants, AI strategy, and special-project documentation. Vanilla country-release, inheritance, character-role, dynamic-country, and AI-profile implementations were used as precedents.

## Closure of the prior audit

| Prior finding | Live result | Evidence |
|---|---|---|
| P1 — absorbed CBA–CBH slots were stranded | Closed | `cannibalism_prepare_current_warlord_slot_for_unification` keeps the incarnation and in-use markers until annexation, moves origin-state cores to the real CBL/ZZZ destination, removes the source core and state slot metadata, and leaves final release to `on_annex`. `cannibalism_begin_current_warlord_slot_release` performs the canonical reset, while `cannibalism_finalize_current_warlord_slot_release` alone clears the global in-use flag after the reference audit and establishes the 45-day quarantine. The release queue covers CBA through CBH. |
| P1 — starting divisions received free fill in addition to population-backed reserves | Closed | `cannibalism_warlord_creation.starting_equipment_factor` and `.starting_manpower_factor` are both zero. Every starting `create_unit` receives those values. Manpower and stockpile grants remain derived from the exact formation population receipt and calculated unit count. |
| P1 — CBL had no research slots and lost later donor technology | Closed | Runtime CBL creation assigns three research slots. `union_compatible_researched_technologies_from_donor` adds missing donor technologies before annexation at exactly three sites: the opening CBL donor, later ordinary absorption, and the primary Wendigo donor. The helper preserves the recipient's mutually exclusive flexible/streamlined and concentrated/dispersed industry choice. |
| P1 — route, origin, personality, and character inheritance was partial | Closed | The opening hierarchy, Larder route, network route, origin, name, slot, region, personality, Larder, Frenzy, alignment, and population ledger are captured and applied. Unified operational profiles consume the route flags. Later donors accumulate route and origin knowledge. Retained and host dispositions create named commanders with origin and personality traits; surrender creates the bound-servant variant. Four separate paid origin-specialist decisions remain available for every learned origin. |
| P1 — transformed original ZZZ lost its daily zombie mechanics | Closed | The existing Event 2 `on_daily` still processes controlled-state decay, weaponized hostility/merge/expansion, original-ZZZ threat and rejoin pressure, dynamic-outbreak annexation, coring, capital relocation, and USA war continuity. Only the generic leader refresh is excluded for the transformed identity. No second Event 14 whole-world daily iterator was added. |
| P2 — March Host could form below the intended weak package and tiered Larder tuning was dead | Closed | Island, Siege, March, and Prison origin triggers all require the shared 250K weak-population floor. Formation Larder and starting-force capacity come from the same exact population transaction; the unused tiered starting-Larder table is gone. At the weak floor, the 5% receipt is large enough for the documented three-unit weak package under the four-thousand-person unit-capacity rule. |
| P2 — all origins shared one persistent AI profile | Closed | `common/ai_strategy/014_cannibalism_warlords.txt` contains one common profile and four origin-gated profiles. All five use `abort_when_not_enabled = yes`. Island prioritises convoys, screens, and naval bases; Siege prioritises artillery, bunkers, and arms factories; March prioritises motorisation, infrastructure, and spare attack units; Prison prioritises support equipment, bunkers, garrisons, and intelligence capacity. Origin flags are cleared during release. |
| P2 — CBL logistics were only a host score | Closed | `cannibalism_is_viable_unification_host` now hard-requires a controlled, cored, usable capital with a supply node, naval base, railway, or infrastructure above the critical threshold. Human preference remains a score bonus only after this viability gate. |

## Additional live findings and remediation recheck

The following gaps were discovered during this final pass. Each was fixed in the live worktree and re-audited:

1. **Destination cores.** Absorption previously removed the reusable source's cores without adding CBL/ZZZ cores. The shared unification preparation now adds the saved migration destination as core owner on every matching source-incarnation state before removing the source core. All three absorption paths save the destination first. Conquered non-origin territory is still not granted automatic cores.
2. **Transformed-ZZZ ordinary inheritance.** The transformed host now retains both paid recruitment families required by the specification. The inherited warlord category exposes paid Scavenger Warbands and Network Cadres; the unified war-machine category exposes paid Feast Cohorts, Bone Guards, and one separate decision for each inherited origin specialist. The original paid Wendigo Pack path remains available independently.
3. **Character registration.** The scripted-effect and on-action `recruit_character` calls were removed. CBL Hannibal and Wendigo Hannibal are recruited roleless in their custom-tag history, remain without a public role before reveal, and receive/promote their country-leader roles only after `cannibalism_reveal_complete`. The Event 2 profile refresh restores the transformed public name and portrait without recruiting a character.
4. **Country and party localisation.** CBA–CBH and CBL now have all four ideology name/DEF/ADJ triplets plus runtime neutrality party short and long names. The eight warlords resolve their party wording from origin-aware scripted localisation. A direct key-set check found all 126 required country/party keys.
5. **Inherited recruitment slot metadata.** The shared warlord recruitment transaction initially attempted to register CBL/ZZZ recruitment states as reusable-slot warlord states. The registration call is now gated to an actual reusable warlord country, so CBL/ZZZ cannot recreate slot flags, indices, generations, or reference counts. Their exact Deaths receipt, empty unit, manpower conversion, counter, and state cooldown remain intact.
6. **Inherited recruitment Larder ceiling.** CBL/ZZZ inherited recruitment now delegates Larder spending to `cannibalism_unified_pay_current_larder_cost`, preserving the larger global-Larder ceiling and synchronising `global.cannibalism_global_larder`. Ordinary reusable warlords retain the local Larder ceiling.

No replacement P0–P2 issue was found in those repaired paths.

## Passing country-package evidence

### Eight reusable slots, origin territory, and reincarnation safety

- `common/country_tags/014_cannibalism_countries.txt` registers CBA/CBB for Island, CBC/CBD for Siege, CBE/CBF for March, CBG/CBH for Prison, and CBL for ordinary unification. Matching country and dormant history files exist for all nine tags.
- Allocation remains inside each origin's two-slot pool. Formation transfers the origin plus at most two directly adjacent same-controller active-cell states, then cores and annotates those exact states for the allocated incarnation.
- Unsupported regions do not receive a generic identity. The region/name/portrait system covers Europe, Asia, Africa, Middle East, North America, South America, and Oceania.
- Release clears focus contracts, route/origin flags, ideas, templates, modifiers, actor and spread references, state cores, state slot variables, node-source references, and scheduled callbacks before reuse. Finalisation waits for the dead-country/reference audit and quarantine.
- The reincarnation reset clears inherited recruitment flags and the transformed-only recruitment counter as well as the existing warlord route and decision state. Origin AI profiles stop automatically when their origin flag disappears.

### Forces, population, Deaths, Larder, and recruitment

- All nine ordinary cannibal templates are created once, locked against editing, and force-blocked from normal queue recruitment. CBL and transformed ZZZ therefore use scripted paid recruitment rather than free ordinary recruitment.
- Starting warlord divisions, ongoing warlord units, CBL units, inherited CBL/ZZZ Scavenger/Network units, origin specialists, and additional Wendigo Packs use zero starting equipment and zero starting manpower.
- Warlord creation and every paid recruitment route use `cannibalism_prepare_consumption_context`, which receives an exact state-population request and accepts only an exact applied receipt. Population is removed once through the shared Deaths-aware helper before Larder or manpower is credited.
- Recruitment is bounded by per-family caps, controlled/usable-state checks, minimum remaining population, state cooldowns, Larder, and current equipment reserves. The exact receipt supplies the configured manpower pool; the empty divisions reinforce from that pool and existing stockpiles.
- No dead starting-Larder value, duplicate population receipt, or free scripted fill remains in the audited Event 14 country paths.

### CBL technology, identity, AI, and playable inheritance

- CBL receives three research slots and the compatible technology union before each donor disappears. Later donors cannot erase recipient technologies or switch CBL's existing industry branch.
- The opening host's completed hierarchy, Larder, and network routes immediately affect unified authority, Larder/Frenzy, mobility/resources, alignment, hostility, and terminal progress. Later donors add their completed-route and origin knowledge without replacing the opening route.
- Integrated commanders preserve regional portrait, generated name, origin trait, and one of six personality traits. Dispositions remain mechanically distinct: retain, surrender/bound servant, autonomy/governor, resistance, challenge, and purge are not collapsed into one annex result.
- Paid recruitment is available through Scavenger, Network, Feast/Bone, and four independently selected specialist families. AI weights exist on the visible decisions and every payment path retains exact population/resource checks.
- Human host selection still passes the hard logistics gate, then receives player preference. CBL joins the host's wars before annexation, transfers its troops, and uses `change_tag_from` for player continuity. A second human warlord cannot be silently submitted because submission requires either source or destination to be AI.

### In-place original-ZZZ preservation

- The merge host is the existing live original-ZZZ dynamic, independent, weaponized Wendigo country. Event 14 does not create a replacement country, reload an OOB, reset politics, reset research slots, delete units, delete the Wendigo Pack, remove technologies, or clear weaponized profile variables and flags.
- Existing territory, units, templates, equipment, convoys, technologies, research state, ideas, project consequences, zombie flags, profile variables, recruitment identity, AI profile, and Event 2 daily mechanics remain on the same country scope.
- Event 14 adds donor technologies through the compatible union; it does not replace original ZZZ technology. It adds locked cannibal templates and paid cannibal decisions while preserving the original force-allowed Wendigo Pack and its separately paid training path.
- The original `ZZZ_unit_production` strategy remains enabled by `original_tag = ZZZ`. Event 14 focus rewards add route-specific priorities without removing that identity.
- Generic leader-refresh and generic Event 2 Wendigo world-end entry are explicitly excluded after transformation, preventing them from overwriting Hannibal or bypassing the Event 14 anchor/countdown route. Other daily outbreak operations continue.
- The terminal removal of `weaponized_zombie_counterstrain_exposed` is deliberate only after the irreversible Event 14 lock. Before lock, counterstrain and anchor destruction remain valid counterplay.

### Localisation, flags, characters, and secrecy

- CBA–CBH and CBL have all required base and ideology-specific localisation, with origin-aware party wording for the reusable warlords. Hannibal, origin, personality, commander, decision, and tooltip keys used by these paths resolve in the Event 14 localisation/scripted-localisation files.
- A direct asset check found all 135 required CBA–CBH/CBL base-and-ideology flag files across regular, medium, and small sizes. All 45 files for the three CBL route cosmetic tags and all 15 files for `ZZZ_CANNIBALISM_HANNIBAL` are also present.
- Static and animated-fallback portraits for CBL Hannibal and transformed-ZZZ Hannibal are registered in `interface/014_cannibalism.gfx` and backed by existing DDS files.
- The reveal flag precedes CBL/ZZZ public names, cosmetics, leaders, focuses, decisions, events, news, reports, achievements, and super-event surfaces. The two Hannibal characters are roleless before that point. No pre-reveal player-facing identity leak was found.

## Intentional non-defects

- The technology union preserves the recipient's mutually exclusive industry branch instead of combining both branches.
- Special-project facilities, prototypes, and facility-scoped state from an absorbed donor are not transferred. The technology union is a researched-technology contract, not a project-state merger.
- The original live ZZZ country's own project and research state remains in place because the country is transformed in situ.
- Ordinary conquered territory is not automatically cored during unification; only the absorbed warlord incarnation's origin territory receives the destination core.

## Simplifications, omissions, and blockers

None within the audited country-package scope. No fallback, placeholder, skipped route, missing AI path, missing localisation family, missing required flag family, free-fill substitute, or unreported simplification was found.

This verdict is limited to the Event 014 country-package surface described above; it does not replace the separate focus-tree, decision/mission, localisation, asset, spreadsheet, super-event, or full event-completion audits.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-focus-trees`
