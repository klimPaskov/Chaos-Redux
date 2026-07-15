# Event 006 FORM-01 through FORM-04 operational re-audit

Date: 2026-07-16
Mode: independent read-only source, data, localisation, and asset re-audit
Gameplay edit authority: none
Commit authority: none
Runtime-execution claim: none

## Executive verdict

The shared FORM transaction and the family-specific implementations now close the operational defects recorded in the 2026-07-15 audit. On static inspection, FORM-01, FORM-02, and FORM-04 satisfy their transaction, membership, territory, identity, cost, progression, AI, localisation, asset, cleanup, Event 5 isolation, and bounded-scan prerequisites. Their fail-closed readiness helpers can be promoted with the exact attestations listed below.

FORM-03's transaction, member policy, territory bounds, corrected processed-marker finalisation, identity, progression mechanics, AI, and runtime asset package also pass. FORM-03 must nevertheless remain fail-closed because two current non-runtime surfaces are not completion-clean:

1. player-facing FORM-03 localisation exposes implementation state numbers `34` and `36`; and
2. the dedicated report-scene submanifest still tells the parent to reconcile an already-reconciled system document.

These are FORM-03 promotion blockers under the repository's localisation and manifest-alignment requirements. They do not invalidate the shared transaction or block FORM-01, FORM-02, or FORM-04.

| Family | Static operational verdict | Readiness disposition |
|---|---|---|
| FORM-01 / KCX | Pass | Safe to restore its exact generic and FORM-01 attestations. |
| FORM-02 / NUX | Pass | Safe to restore its exact generic and FORM-02 attestations. |
| FORM-03 / LCX | Runtime and asset implementation pass; completion metadata/localisation fail | Keep all FORM-03 readiness flags cleared until both findings are corrected and rechecked. |
| FORM-04 / RLX | Pass | Safe to restore its exact generic and FORM-04 attestations. |

No fallback identity, substitute member, substitute state, simplified progression, placeholder asset, or widened scan is accepted by this verdict.

## Audit boundary and sources

This re-audit inspected the current repository state after the shared transaction repairs, FORM-03 processed-marker correction, FORM-03 report-art completion, KCX/NUX/RLX ideology-file aliases, and LCX colour registration. It did not alter gameplay, documentation outside this handoff, assets, skills, spreadsheets, readiness flags, or commits.

Required references consulted before the source audit:

- repository skills: `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-decisions-missions`, `hoi4-focus-trees`, and `chaos-redux-event-assets`;
- accepted Event 006 specifications, candidate matrices, progression addendum, identity research, implementation handoffs, and the preceding operational audit;
- offline wiki core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, and AI;
- offline wiki pages for country creation, cosmetic tags, focus trees, factions, autonomy, states, and map adjacency;
- vanilla official documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including script concepts/constants, effects, triggers, modifiers, localisation, and scopes;
- vanilla `common/script_constants/documentation.md`;
- vanilla formable precedent `common/decisions/formable_nation_decisions.txt`, including the United Netherlands formable and the Dutch Benelux proposal sequence; and
- vanilla precedents for adjacency, naval bases, bilateral relation removal, strength-ratio checks, cosmetic identities, and focus prerequisite layout.

The offline wiki snapshot, not the online Paradox wiki, was used. The audit makes no claim that the game was launched, that an event was fired in a live session, or that engine runtime behaviour was observed.

## Promotion-blocking FORM-03 findings

### F03-P1: player-facing localisation exposes implementation state IDs

`localisation/english/006_independence_wave_form03_l_english.yml` refers to `state 34` or `state 36` in visible descriptions and tooltips at lines 111, 140-144, 190, 194, 240, and 242. The affected strings include the works-board tooltip, both anchor-project descriptions and effects, both cost tooltips, and both dynamic-modifier descriptions.

The underlying gameplay bounds are correct, but numeric map IDs are implementation language. Replace these phrases with the in-world Walloon/Sambre-Meuse and Frisian/northern-waterway names already used by the surrounding prose, or with an established state-name localisation form. Preserve the dynamic cost, duration, and delta tokens.

This is a localisation-completion blocker, not a FORM-03 territory-mutation defect.

### F03-P2: the report-scene submanifest contains a stale merge instruction

`docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md:83-84` says that the package-root manifest was not edited and that `docs/systems/006_independence_wave_form03_progression.md` still claims there is no distinct art.

Both statements are stale in the current tree:

- `docs/assets/006_independence_wave/manifest.md:191-210` records ASSET-048, its runtime texture, sprite, and `.300-.308` consumers; and
- `docs/systems/006_independence_wave_form03_progression.md:98-110` documents the six focus icons, six ideas, six decision icons, dedicated report scene, registrations, and consumers.

Update the submanifest's merge notes to describe the completed reconciliation, then refresh any manifest checksum that intentionally covers the file. The runtime DDS and sprite are valid; the blocker is stale asset-package documentation.

## Shared transaction re-audit

### Explicit proposal ownership and frozen consent

The registry no longer consumes a free-floating family response:

- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:77-85` verifies member and invitation array alignment before proposal work proceeds.
- Lines 149-193 validate the exact invitation tuple: live carrier scope, carrier generation, invited member generation, selected family, and proposal sequence.
- Lines 195-218 distinguish pending, accepted, and withheld responses only through that exact tuple.
- Lines 222-260 validate an accepted response from the carrier scope and the frozen congress-consent row.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:744-879` stores and issues the invitation with carrier, generation, family, and sequence bindings. The carrier's self-row is explicit rather than implied.
- The response decisions in both FORM decision files require the invitation-bound response surface. Operational families do not infer consent from generic AI eligibility.

The generation binding is meaningful: Event 006 active packages carry their registry generation, the invitation freezes both carrier and member generation, and FORM-03's one external BEL delegation uses the documented zero-generation sentinel instead of pretending BEL is an Event 006 active-package row.

### Congress ledger alignment and freeze

The action-time ledger construction is bounded and internally aligned:

- the member country and consent arrays, and the parallel invitation-carrier, carrier-generation, member-generation, family, and sequence arrays are alignment-gated;
- the active registry pass is performed only when a player or AI invokes the congress workflow (`common/scripted_effects/006_independence_wave_formable_registry_effects.txt:989-1043`);
- recounting follows the bounded pass (`:1045` onward);
- each consenting row freezes the proposal tuple consumed by strict commit proof; and
- `can_independence_wave_formable_pass_congress_vote` (`common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:421-457`) tests the frozen ledger rather than discovering countries again during mutation.

FORM-03 extends that bounded ledger only with the exact sovereign BEL delegation. It does not register BEL as an Event 006 active country and does not search for an arbitrary Belgian replacement.

### Costs and strict revalidation

The formation decision at `common/decisions/006_independence_wave_decisions.txt:2965-2994` does all three required operations in the carrier scope:

1. rechecks `can_independence_wave_commit_selected_formable`;
2. rechecks the aggregate selected-method cost; and
3. pays that cost before requesting the commit transaction.

`common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:505-540` dispatches strict family proof and also requires the transaction to remain formation-ready, the frozen congress vote to pass, readiness to match the currently selected family, and no pending or already-active commit. Lines 542-568 gate payment.

`common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1264-1289` assembles the real strategic/diplomatic and administrative/security costs. The civic method's 40 command-power gate correctly covers its two 20-point component payments; the values are sourced from script constants rather than duplicated literals.

### Identity, integration, deterministic mutation, and close

The shared dispatch at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1327-1384` has the required order:

1. strict proof is re-evaluated;
2. `independence_wave_formable_mutation_prevalidated` is set;
3. the selected identity adapter runs;
4. the selected integration adapter runs only after identity commit;
5. success is declared only when both commit flags exist;
6. the outcome and family progression start; and
7. the proposal closes after the success or failure branch.

For the audited families, all mutable members and states are enumerated before that phase; the adapters contain no random list, random effect, chance branch, late diplomatic discovery, or new resource check. Identity and integration postconditions are synchronous flags set by the same bounded effects. Accordingly, the current source supports the requested deterministic, no-post-prevalidation-failure construction: after strict proof passes, there is no scripted late failure condition before the two commit flags. This is a source-level construction claim, not a live-engine execution claim.

The proposal-close effect at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:760-796` traverses the invited arrays plus the bounded Event 006 active registry and exact BEL extension. It clears a response only when carrier, generation, family, and proposal sequence still match, so closing one congress cannot erase a later or unrelated invitation.

### Origin and runtime cleanup

`independence_wave_formable_end_consenting_member_origin` (`common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1390-1426`) rechecks the frozen consenting row before calling the canonical `independence_wave_end_active_origin` with the `formable_absorption` path.

The canonical Event 006 helper at `common/scripted_effects/006_independence_wave_effects.txt:2437-2488` clears Event 006 package state, unregisters the country from Event 006 arrays, and dispatches package/formable cleanup. The formable cleanup then clears transaction, identity, progression, invitation, relation-ownership, and ledger state. No inspected path mutates an Event 5 route, package, origin, evolution, event target, or registry value.

### Symmetric autonomous-relation ownership

`independence_wave_form0124_install_autonomous_member` records the carrier scope, carrier generation, family, and each direction-specific relation created by this system. The four ownership flags distinguish carrier-to-member access, member-to-carrier access, carrier guarantee, and member guarantee.

`independence_wave_form0124_remove_owned_autonomous_relations` removes only directions whose ownership flag was set. `independence_wave_form0124_clear_frozen_autonomous_members` re-enters the frozen member scopes and validates the stored carrier generation and family before member cleanup. This repairs the asymmetric-cleanup defect without deleting relations that predated the charter.

## Family-specific proofs

### FORM-01: Celtic Cooperation State / KCX

`common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt` enforces:

- exact founder anchors SCO state 121, WLS state 122, and BRI state 14 (`:9-19`);
- the full compact: all three living, eligible, invited founders with exact frozen consent (`:147-163`, `:222-230`);
- a carrier/member treaty link through faction membership, non-aggression, either-direction military access, either-direction guarantee, or equivalent accepted relation, with no current war (`:102-128`); and
- exact full-integration territory bounds of SCO 121 and 133, WLS 122, and BRI 14.

No ACX/Cornwall substitution exists. Full integration requires the member's explicit integration authorisation; otherwise the consenting member remains a protected autonomous country. KCX identity is assigned only after runtime proof and is protected by the global KCX-in-use lock.

The first-stage system begins at 20/20. The three rotating sessions contribute 15/15 each, and the language and defence actions contribute complementary 25/10 and 10/25 deltas. The route can reach 100/100, exceeds the 75/75 ratification thresholds after the required session count, has a real deadline, timeout outcome, paid recovery, and nonzero AI choices.

### FORM-02: North Atlantic Compact / NUX

The strict trigger enforces:

- Newfoundland/GZX with state 331 as the mandatory anchor;
- any two of ICE state 100, scenario-IW011 AKX state 337, and SCO state 121;
- exact proposal consent and a valid live founder for every accepted optional row;
- a usable port for every participating anchor;
- the accepted carrier/member treaty or no-war connection; and
- a nonzero convoy stockpile on the carrier.

AKX is valid only through its scenario-IW011 Event 006 package. Labrador state 332 is absent from eligibility, transfer, core, and capital dispatch. No AKX release or nearby-tag fallback is present.

Full integration is bounded to ICE 100, AKX 337, GZX 331, and SCO 121/133. With any autonomous member, the carrier keeps its own capital; the priority port-capital selection is used only for a fully integrated compact.

The first stage begins at 20/20. Convoy charting, port standardisation, and warning-line work produce 25/15, 15/15, and 15/25, reaching 75/75 with the required flags. The projects have real equipment/factory/command costs and durations, a deadline and timeout outcome, paid reconvening, and nonzero AI.

### FORM-03: Low Countries Federation / LCX

The current runtime implementation satisfies the accepted territorial and sovereign-associate model:

- the carrier is exactly AFX with scenario-IW006/state 34/capital 34 or AGX with scenario-IW007/state 36/capital 36;
- the second AFX/AGX anchor must be independently eligible, explicitly consenting, and actually connected;
- BEL can found only while sovereign, using `BEL_flanders`, owning and controlling state 6, and holding the exact frozen carrier invitation;
- only AFX state 34 and AGX state 36 may transfer or receive carrier cores;
- BEL, HOL, and LUX remain sovereign after founding and may join the post-charter structure only through their bounded invitation decisions; and
- states 6, 7, 8, 35, 977, and 980 are never transferred, re-cored, assigned a new owner/controller, or selected as the carrier capital.

The static mutation search found only state 34/36 transfer, core, and carrier-capital operations. Sovereign works in states 6, 7, 8, 35, and 977 apply bounded modifiers or construction logic without changing sovereignty. State 980 is not mutated.

The language/industry progression is installed across the six-focus branch, language and works decisions, lifecycle ideas, events `.300-.308`, recovery/withdrawal decisions, and cleanup. Its values are reachable without a failure cycle:

- Language Settlement starts at 15 and can reach at least 70 through each complete settlement line; the parallel-language line can reach 75.
- Industrial Integration starts at 15; one anchor work plus the manifests reaches 55 and therefore supports the compromise threshold, while both anchor works plus manifests reaches 80 and supports full ratification. Associate corridors and development works provide additional bounded routes rather than being silently assumed.
- Required focus conjunctions, status flags, deadline mission, outcomes, real project costs/durations, cancellation penalties, recovery choices, and nonzero AI are present.

#### Processed-marker finalisation

The parent correction at `common/scripted_effects/006_independence_wave_form03_effects.txt:91-149` is semantically correct.

`independence_wave_form03_additional_member_processed` is a boolean-style temporary sentinel, not a counter. It starts at `no_entries` and each successful AFX, AGX, or BEL founding branch assigns `loop_increment` (1). The final test therefore correctly uses `greater_than_or_equals 1`.

It must not require 2: FORM-03 can validly found with the carrier plus one additional accepted founder, including a BEL-only additional founder. It also should not be interpreted as the number of processed founders because repeated successful branches assign 1 rather than add 1. The corrected comparison precisely proves that at least one strict, frozen additional-member branch completed.

#### FORM-03 asset proof

The dedicated package is materially complete:

- six 94x86 focus DDS files, six 64x64 idea DDS files, and six 32x32 decision DDS files are registered in `interface/006_independence_wave_form03.gfx` with focus shine entries where required;
- the 210x176 report DDS is registered as `GFX_report_event_006_form03_charter_convention` in `interface/006_independence_wave_event_pictures.gfx`;
- `events/006_independence_wave.txt:99-397` wires that report sprite to `.300-.308`;
- package and runtime copies have matching hashes;
- the decoded runtime report matches the processed PNG, and the static DDS inspection found the intended dimensions, BGRA masks, and real alpha; and
- source, processed, runtime, prompt, checksum, review, and manifest materials exist.

This asset proof is why F03-P2 is limited to stale submanifest text; it is not evidence of a missing or placeholder runtime image.

### FORM-04: Rhine Federation / RLX

The strict trigger enforces:

- living, independent RHI with state/capital 51 and AJX with state/capital 42;
- both exact frozen founder rows;
- peace between founders;
- national adjacency between the two countries and the explicit state-51/state-42 adjacency proof;
- no GER control of either anchor; and
- full-integration mutation bounded to states 51 and 42, with capital 42 selected only after it is owned by the carrier.

The stronger-Germany preference is AI-only. Human availability is not hidden behind an arbitrary force-ratio check. AI willingness prefers the federation when Germany's compared strength ratio is below the script-constant 0.67 threshold, while the accepted high-chaos sovereignty route can waive that preference gate. The trigger uses an explicit comparison and does not weaken the hard peace, adjacency, consent, or anchor requirements.

The first stage begins at 20/20. Toll, peace, and security projects contribute 25/15, 15/25, and 15/15, reaching 75/75. They have real costs/durations, a deadline and timeout outcome, paid reconvening, and nonzero AI.

## Identity, colours, flags, icons, report art, and localisation

### Cosmetic identities

- `common/countries/006_independence_wave_formable_cosmetics.txt` defines distinct KCX, NUX, LCX, and RLX map/UI colours.
- KCX, NUX, and RLX each have base plus democratic, communism, fascism, and neutrality aliases in normal, medium, and small flag sizes. Each alias is byte-identical to its accepted shared base design, avoiding vanilla ideology lookup overriding the cosmetic flag.
- LCX has the accepted base three-size package for AFX/AGX carriers, for which the audited lookup conflict does not exist.
- Static TGA inspection found the expected 82x52, 41x26, and 10x7 dimensions, uncompressed type-2 32-bit data, alpha descriptor, and expected byte length.
- Country names, ideology variants, and adjectives for KCX, NUX, LCX, and RLX are localised.

### Icons and report images

FORM-01/02/04 decisions and events resolve to already registered Event 006 decision/icon sprites and `GFX_report_event_006_asset_001_wave_summary`. Their consumers are explicit; no missing GFX identifier was found in the audited surface.

FORM-03 uses its dedicated six-focus, six-idea, six-decision, and one-report package as detailed above. It does not silently fall back to the generic report scene.

### Localisation coverage

A fresh extraction of player-facing `name`, `desc`, `title`, `text`, tooltip, custom-effect-tooltip, custom-cost-text, focus-title, and focus-description references found 240 referenced keys plus the six focus title/description pairs and no missing English key in the audited FORM surfaces. The relevant English localisation files retain UTF-8 BOM encoding. The only localisation completion defect found is F03-P1's numeric state language.

## Scan, cleanup, and isolation conclusions

- No audited FORM registry, trigger, effect, decision, event, or progression file introduces `every_country`, `random_country`, `all_country`, `on_daily`, `on_weekly`, or `on_monthly` processing.
- Discovery and cleanup use the bounded Event 006 active registry, frozen invitation/member arrays, and exact BEL/HOL/LUX tags where the accepted FORM-03 design requires them.
- Proposal close is generation- and sequence-safe.
- Autonomous diplomatic cleanup is directionally owned and symmetric.
- Full integration closes only the frozen consenting member's Event 006 origin through the canonical helper.
- Family cleanup clears progression, invitations, ledgers, temporary relation ownership, identity locks, and family runtime flags.
- No Event 5 state is read as authority for, or mutated by, the FORM transaction.

## Exact readiness restoration disposition

All four register helpers currently call `independence_wave_formable_clear_selected_family_readiness` and set nothing. That is the correct fail-closed baseline. Any promoted helper must continue to clear first, then set only the following carrier-scope variable and flags.

The six generic flags are identical for every promoted family:

- `independence_wave_formable_territory_adapter_ready`
- `independence_wave_formable_x_tag_reserved`
- `independence_wave_formable_flag_package_ready`
- `independence_wave_formable_identity_adapter_ready`
- `independence_wave_formable_integration_adapter_ready`
- `independence_wave_formable_member_policy_audited`

The exact safe dispositions are:

| Register effect | Readiness-family value | Family-specific flags | Disposition |
|---|---|---|---|
| `independence_wave_form01_register_readiness` | `constant:independence_wave_formable_family.celtic_cooperation_state` | `independence_wave_form01_readiness_attested` | Safe to restore with the six generic flags. |
| `independence_wave_form02_register_readiness` | `constant:independence_wave_formable_family.north_atlantic_compact` | `independence_wave_form02_readiness_attested` | Safe to restore with the six generic flags. |
| `independence_wave_form03_register_readiness` | `constant:independence_wave_formable_family.low_countries_federation` | `independence_wave_form03_readiness_attested` and `independence_wave_form03_progression_attested` | Not safe yet. Correct F03-P1 and F03-P2, re-run the narrow localisation/manifest check, then restore this exact bundle together. |
| `independence_wave_form04_register_readiness` | `constant:independence_wave_formable_family.rhine_federation` | `independence_wave_form04_readiness_attested` | Safe to restore with the six generic flags. |

The family variable must be set to the value shown in the table so `has_independence_wave_formable_commit_readiness` can prove it equals the currently selected profile family. Do not set generic flags without the matching family variable and family attestation. Do not set either FORM-03 family flag alone: the shared readiness trigger requires both base and progression proof, and the current findings span both player-facing progression text and the progression asset manifest.

If the parent chooses one combined readiness patch, FORM-01, FORM-02, and FORM-04 may be promoted while FORM-03's helper remains clear-only. Family switching remains safe because `independence_wave_formable_register_selected_family_readiness` clears the old bundle before dispatching the newly selected family's helper.

## Meaningful validation evidence

- Exact proposal carrier/generation/member-generation/family/sequence bindings were followed from invitation issuance through response, ledger freeze, commit, and proposal close.
- All four strict commit proofs were followed through the shared cost and mutation dispatcher.
- Full-integration state mutation was enumerated by family; FORM-02 contains no Labrador mutation, and FORM-03 contains no sovereignty mutation for 6, 7, 8, 35, 977, or 980.
- Autonomous bilateral relation installation and removal were compared direction by direction.
- The canonical absorbed-origin cleanup was checked for Event 5 isolation.
- First-stage value ladders were recomputed from configured starts and project deltas; each mandatory path reaches its ratification threshold without requiring a timeout/recovery cycle.
- Decision/event AI blocks are nonzero on invitation responses, projects, outcomes, and repair/reconvening choices.
- KCX/NUX/RLX alias hashes and all four flag packages' static TGA headers were checked.
- Every FORM-03 packaged/runtime DDS was checked for matching copy hash, expected dimensions/header layout, and alpha; the report PNG/DDS decoded-pixel identity was independently confirmed.
- FORM player-facing key extraction found no missing English key; the manual prose review found F03-P1.
- Event and interface consumers were traced to their registered report sprites.
- The audited transaction surface contains no world-periodic scan.

## Simplifications, omissions, and blockers

No implementation simplification or fallback was accepted. This was a static, read-only audit and therefore did not launch HOI4 or claim live runtime execution.

FORM-01, FORM-02, and FORM-04 have no remaining source-level blocker in the requested audit surface. FORM-03 remains incomplete for readiness promotion only because F03-P1 and F03-P2 are unresolved. Its runtime transaction, processed-marker semantics, sovereign territory policy, progression implementation, and produced asset package pass this re-audit.
