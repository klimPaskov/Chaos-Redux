# Event 006 FORM-01 through FORM-04 operational audit

Date: 2026-07-15
Mode: read-mostly operational audit with narrow exact patches
Commit authority: none
Readiness authority: none; this audit did not set any package, family, asset, or progression attestation

## Verdict

The shared registry and the four family implementations are **not ready for operational certification**. The compact-state, core, capital, Event 5 isolation, bounded-scan, post-formation mission, cost, and AI foundations are substantially present, but the following completion blockers remain:

1. Founding consent is not tied to an explicit invitation from a specific carrier.
2. FORM-01 lacks the required carrier/member diplomatic-connection proof.
3. FORM-02 lacks the required port and verified convoy-connection proof.
4. FORM-04 does not implement the accepted stronger-living-Germany exclusion; it only checks the two corridor controllers.
5. FORM-01/02/04 autonomous-member cleanup is carrier-local and leaves member state and relations behind.
6. The family integration adapters do not provide a strict rollback for member transfers, Event 006 origin closure, or autonomous relations after mutations begin.
7. FORM-03's accepted progression asset package is absent and its progression attestation is not part of readiness.
8. KCX, NUX, and RLX lack the mechanically required ideology-named cosmetic flag files for carriers whose base tags have ideology flags.

No fallback identity, fallback member, fallback state, readiness attestation, or broad redesign was introduced by this audit.

## Sources and required references used

- Accepted identity and membership source: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form01_04_identity_research_2026_07_15.md`
- Accepted FORM-03 progression source: `docs/plans/006_independence_wave_plans/006_form03_language_industry_progression_addendum_2026_07_15.md`
- Repository skills: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, and `chaos-redux-event-assets`
- Offline wiki core pages required by `AGENTS.md`, plus `Country creation` and `Cosmetic tag modding`
- Vanilla documentation for effects, triggers, script concepts/constants, decisions, events, focuses, ideas, modifiers, scopes, and localisation
- Vanilla decision, mission, focus, cosmetic-tag, and country-flag precedents

The installed HOI4 MCP tools were not exposed in this subagent's callable tool surface, so no MCP event/focus render result is claimed here.

## Family verdicts

| Family | Exact membership and territory | Operational verdict | Principal blockers |
|---|---|---|---|
| FORM-01 / KCX | Correctly restricts founders to SCO state 121, WLS state 122, and BRI state 14; ACX/Cornwall remains excluded. Scotland plus a Brythonic council and three exact consents are required. Full integration is bounded to 121/133, 122, and 14. | Not certifiable | No explicit carrier invitation or carrier/member diplomatic-connection validation; autonomous cleanup and strict rollback incomplete; KCX ideology-named flag files missing for supported carriers. |
| FORM-02 / NUX | Correctly restricts founders to ICE 100, AKX 337, GZX 331, and SCO 121, requires Newfoundland plus two eastern members and three exact consents, excludes Labrador 332, and does not auto-release scenario-only AKX. | Not certifiable | No invitation, port, or convoy-connection proof; autonomous cleanup and strict rollback incomplete; NUX ideology-named flag files missing for ICE/SCO carriers. The autonomous-capital policy and first-stage value dead end were patched. |
| FORM-03 / LCX | Correctly restricts carriers to AFX 34 or AGX 36, permits only a consenting connected AFX/AGX second founder to integrate, preserves BEL/HOL/LUX as sovereign associates, and never transfers or cores 6, 7, 8, 35, 977, or 980. | Not certifiable | Founding consent is still self-presented rather than invitation-bound; progression assets are absent; progression attestation is neither set nor required by readiness; strict transfer rollback remains incomplete. |
| FORM-04 / RLX | Correctly requires living RHI 51 and AJX 42, integrates/cores only those certified states after consent, and uses state 42 only when the carrier actually acquires it. | Not certifiable | No explicit invitation or connected-capitals proof; the stronger-Germany exclusion is reduced to `controller != GER` on states 42/51; autonomous cleanup and strict rollback incomplete; RLX ideology-named flag files missing for an RHI carrier. The first-stage value dead end was patched. |

## Blocking findings

### 1. Founding consent is not an invited, carrier-bound exchange

The accepted shared rule requires a living country to enter the congress ledger only after an explicit invitation and recorded response. That invariant is not implemented for the founding ballot:

- `common/decisions/006_independence_wave_form01_02_04_decisions.txt:10-130` exposes full integration, sovereign membership, and withholding to any locally eligible FORM-01/02/04 country. There is no invitation flag, inviting-carrier event target, or check that the member is answering the carrier that will commit.
- `common/decisions/006_independence_wave_form03_decisions.txt:11-162` lets eligible AFX/AGX and BEL delegations authorize themselves when a prospective partner exists. Connection checks are present, but no carrier issues and owns the invitation.
- The shared arrays record country and consent values, but they do not freeze an inviting-carrier pointer for each founding response.

This permits unrelated eligible countries to populate a global family ballot and a later carrier to consume their consent. The repair needs a bounded invitation effect from the proposer, a persistent carrier/member pairing for the proposal lifecycle, and response decisions/events limited to that pairing. Post-charter FORM-03 associate invitations are already explicit and provide the nearest in-repo pattern.

### 2. Required FORM-01 and FORM-02 connection proofs are absent

- FORM-01 runtime proof in `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt:92-99` validates cultural-side counts and exact consents, but not the accepted diplomatic relation from each autonomous member to the carrier.
- FORM-02 runtime proof at lines 101-108 validates Newfoundland/eastern counts and exact consents, but not a usable port on every member or a verified convoy/treaty connection to the carrier.
- Member eligibility validates ownership/control of anchor states only. It does not validate a naval base, transport relation, or proposal-specific carrier connection.

These are formation gates, not optional flavour. Missing transport or relationship proof must block formation without substituting a nearby tag or state.

### 3. FORM-04's stronger-Germany exclusion is under-specified in code

`has_independence_wave_form04_undominated_corridor` at `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt:87-90` only requires that GER not control states 42 and 51. It does not test whether a stronger living Germany dominates the founders under the accepted matrix exclusion rule, and it does not verify the connection between their capitals.

The current predicate can block a weak Germany that happens to control one corridor state while allowing a much stronger living Germany that dominates both founders without directly controlling either state. This needs the exact strength/exclusion rule from the candidate matrix expressed as a reusable trigger; no strength formula was invented in this audit.

### 4. Autonomous FORM-01/02/04 cleanup is not symmetric

`independence_wave_form0124_install_autonomous_member` at `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:202-215` installs member flags, a family variable, ideas, reciprocal access, and guarantees. `independence_wave_form0124_cleanup_runtime` at lines 392-419 calls `independence_wave_form0124_clear_member_state` only in the carrier scope.

It does not revisit frozen autonomous member scopes before the registry arrays are cleared. An autonomous member can therefore retain its family flag, family variable, idea, access, or guarantees after carrier cleanup. Cleanup must traverse only the frozen ledger or explicit saved member pointers, remove both sides of the relations where the effects support it, clear member state, and then clear the carrier/registry state.

FORM-03 does not share this defect for BEL/HOL/LUX: its cleanup dispatches explicitly to those bounded tags and clears their progression/member mirrors.

### 5. Integration is prevalidated but not strictly rollback-safe

The shared transaction correctly waits for identity and integration commit flags before declaring the family active, and identity rollback drops the cosmetic tag and global identity lock. The family adapters nevertheless mutate member state before the integration commit flag is set:

- A fully integrating member's Event 006 origin can be ended before all later transfers and cores have been demonstrated.
- Autonomous flags, ideas, guarantees, and access are installed while iterating the member rows.
- `independence_wave_form0124_additional_members_processed` and the comparable FORM-03 count prove that qualifying rows were visited, not that every mutation reached its required postcondition.
- The failure path has no territorial, origin-state, or diplomatic rollback ledger.

The strong preconditions make ordinary failure less likely, but they do not satisfy the requested atomic rollback contract. The repair should freeze all member/territory postconditions, fail before the first mutation when any is absent, and either make the remaining mutation phase non-failable by construction or record an exact reverse ledger before applying it.

### 6. FORM-03 readiness does not enforce the accepted progression package

The accepted addendum defines `independence_wave_form03_progression_attested` as the pre-formation proof that every progression surface is installed and audited. Current implementation:

- never sets that flag;
- does not require it in `has_independence_wave_form03_readiness_attestation` (`common/scripted_triggers/006_independence_wave_form03_triggers.txt:210-216`);
- automatically sets `independence_wave_form03_readiness_attested` from `independence_wave_form03_register_readiness` (`common/scripted_effects/006_independence_wave_form03_effects.txt:14-27`).

Consequently the route self-certifies its base readiness while ignoring the accepted progression attestation. This audit intentionally did not set or broaden any attestation. The readiness contract must remain fail-closed until the missing assets and audits are complete.

### 7. FORM-03's accepted visual package is absent

The addendum requires a custom report image, six focus icons, six idea icons, distinct decision icon families, interface registration, and an asset manifest. The only FORM-03-owned asset package currently present is the LCX flag package under `docs/assets/006_independence_wave/low_countries_form03_2026_07_15/`.

Current progression references reuse generic Event 006 assets:

- `.300-.308` use `GFX_report_event_006_asset_001_wave_summary`, `_002_host_crisis`, or `_003_first_recognition` in `events/006_independence_wave.txt`.
- The six focuses at `common/national_focus/006_independence_wave_focus.txt:1751-1889` reuse generic constitutional, administration, infrastructure, and congress icons.
- `common/ideas/006_independence_wave_form03_ideas.txt` and all FORM-03 decisions likewise use shared generic sprites.

This is an explicit accepted deliverable, not an optional polish pass. Asset generation, processing, final DDS/TGA placement, interface registration, manifesting, and wiring remain outstanding.

### 8. Cosmetic flag lookup is broken for several valid carriers

All four base TGA triplets are technically valid uncompressed 32-bit, type-2, bottom-left-origin files at 82x52, 41x26, and 10x7. However, the offline cosmetic-tag wiki documents that a base country's ideology-specific flag outranks a cosmetic tag's no-suffix fallback.

Fresh installed-file checks found:

- SCO and WLS have vanilla democratic, communist, fascist, and neutrality flag triplets.
- BRI and ICE have vanilla communist, fascist, and neutrality flag triplets.
- RHI has vanilla democratic, communist, fascist, and neutrality flag triplets.

KCX, NUX, and RLX currently provide only no-suffix triplets. Therefore a valid SCO/WLS/BRI KCX carrier, ICE/SCO NUX carrier, or RHI RLX carrier can retain its base ideology flag after formation. The accepted research rejects *distinct ideological designs*, but mechanically named ideology files can and should intentionally reuse the same accepted shared design. The asset manifests must document that shared-design exception. LCX's AFX/AGX carriers do not currently have this conflict.

`common/countries/006_independence_wave_formable_cosmetics.txt` also omits LCX while defining KCX, NUX, and RLX map/UI colours. No unaccepted LCX colour was invented; the parent should either add a researched LCX colour pair and document it or explicitly accept retention of the carrier colour.

## Invariants that passed

- Registry discovery and ledger work is bounded to the Event 006 active-country array. No new daily, weekly, or monthly all-country on action was added.
- The country/consent arrays are checked for alignment before commit.
- Identity commit precedes family integration, and the family becomes active only after both adapters report commit.
- `independence_wave_formable_end_consenting_member_origin` rechecks the frozen consenting member and calls the canonical Event 006 end-origin helper.
- `independence_wave_end_active_origin` clears Event 006 origin state only. No Event 5 origin, route, package, or evolution state is mutated by the formable absorption path.
- Full integration and immediate cores are bounded to accepted compact states: FORM-01 121/133, 122, 14; FORM-02 100, 337, 331, 121/133; FORM-03 34/36; FORM-04 51/42.
- FORM-02 correctly excludes Labrador state 332. FORM-03 correctly excludes Belgian/Dutch/Luxembourg states 6, 7, 8, 35, 977 and extension state 980.
- FORM-03 preserves AFX capital 34 or AGX capital 36. FORM-01 retains the carrier capital. FORM-04 uses state 42 only after acquisition. FORM-02 now preserves its existing capital whenever an autonomous member was installed.
- Autonomous paths do not transfer or core member states and preserve member tags, trees, capitals, and Event 006 origins during normal operation.
- FORM-03's constitutional/Development Compact route gate, connected second-founder logic, sovereign-associate model, active ratification mission, failure/repair phases, reserve accounting, state-project bounds, and cleanup guards match the accepted addendum in the audited source.
- FORM-01/02/04 use manually activated deadline missions, one-shot projects, explicit ratification decisions, timeout outcomes, reconvening costs, and nonzero AI weights.
- Event IDs `.300-.308`, `.320-.322`, `.330-.332`, and `.340-.342` each have exactly one definition in `events/`; their audited localisation keys are present.
- All six FORM-03 focus IDs are unique and have title/description localisation.
- A fresh text and filename collision scan across vanilla and all 122 installed Workshop directories found no KCX, NUX, LCX, or RLX collision. This agrees with the accepted full-environment identity audit.

## Narrow patches made by this audit

### `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`

- Raised FORM-02 convoy-chart collective-security gain from `minor` to `standard`.
- Raised FORM-02 air-warning shipping-integration gain from `minor` to `standard`.
- Raised FORM-04 toll-settlement member-confidence gain from `minor` to `standard`.
- These corrections make the mandatory first-stage projects reach at least 75/75 from the configured 20/20 start without requiring a failure/recovery cycle.
- Preserved the FORM-02 carrier's existing capital when any autonomous member is present; priority capital selection now applies only to a fully integrated configuration.
- Replaced processed-member magic thresholds with existing script constants.

### `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`

- Replaced consent/member/value/session magic thresholds with the existing formable and FORM-01/02/04 script constants and explicit `greater_than_or_equals` comparisons.

### `localisation/english/006_independence_wave_form01_02_04_l_english.yml`

- Added ideology-specific adjective localisation for KCX, NUX, and RLX.
- Replaced player-facing implementation-history wording such as `Event 6 package`, `Event 6 origin`, and `Event 6 mechanics` with in-world institutional wording.
- Replaced numeric state references with Rhineland/Moselland wording.
- Replaced hardcoded maximum, threshold, and rotating-session numbers with script-constant localisation tokens.

### `localisation/english/006_independence_wave_form03_l_english.yml`

- Replaced the player-facing phrase `Event 6 League member` with `League member`.

Both touched localisation files retain UTF-8 BOM encoding.

## Required follow-up order

1. Implement proposal-scoped invitations and carrier/member pairing for all four founding families.
2. Add FORM-01 diplomatic and FORM-02 port/convoy proof; add connected-capitals and the exact stronger-Germany exclusion for FORM-04.
3. Make FORM-01/02/04 autonomous cleanup symmetric and make all family integration mutation phases strictly rollback-safe or demonstrably non-failable after prevalidation.
4. Produce and wire the accepted FORM-03 progression asset package.
5. Add the mechanically required shared-design ideology flag triplets for KCX, NUX, and RLX and update the manifests; resolve the LCX colour decision without guessing.
6. Re-run family-specific decision/focus/event audits and only then add the progression/readiness proof through the parent-owned attestation process.

Until those steps are complete, no FORM-01/02/03/04 readiness or completion attestation should be set.
