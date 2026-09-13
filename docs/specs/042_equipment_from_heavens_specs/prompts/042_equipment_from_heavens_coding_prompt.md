# Coding prompt: Event 42 Equipment from Heavens

Implement the complete Event 42 rework from `docs/specs/042_equipment_from_heavens_specs/`. Treat every mapped mechanic, evolution, AI rule, cluster rule, asset row, achievement, log surface, safety gate, and acceptance scenario as required unless a documented engine blocker makes it impossible. Do not replace blocked content with an unapproved fallback.

## Required source review

Before editing, read:

- `AGENTS.md`
- every file in `docs/specs/042_equipment_from_heavens_specs/`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- the relevant offline Paradox wiki pages
- current vanilla effects, triggers, events, equipment, variants, air equipment, nuclear weapons, decisions, AI, scopes, localisation, and event-modification documentation
- current Chaos Redux random-event, Event Log, evolution, cluster, achievement, nuclear, CBRN, unit-family, stockpile, and catalog patterns

Use the installed HOI4 MCP event tools for the event chain and the probability tools for every weighted surface. If an in-scope MCP route is unavailable, record the blocker and do not treat source-only inspection as equivalent evidence.

## Event identity and registration

- Keep the entry root `chaosx.nr42.1`.
- Register Event 42 as Minor Repeatable with Chaos level 1.
- Add it to the reworked-event default enable allowlist when implementation is complete enough for normal selection.
- Use an event-owned valid-recipient trigger based on the shared ordinary-country classifiers.
- Give every eligible recipient exactly equal raw selection weight.
- Keep player countries, ordinary subjects, civil-war participants, majors, and minors eligible under the same rules.
- Return no target and `N/A` weight when no valid recipient exists.
- Exclude a country only while its own Event 42 landing-report chain remains unresolved.

## One-transaction delivery

Build one persisted manifest before applying effects. Store recipient, sequence, magnitude, family list, quantities, equipment tokens or variants, provenance signature, report states, nuclear result, special-family result, and compatibility receipts.

Apply the entire stockpile grant exactly once. Delayed landing reports must never call the grant, pacing handler, repeatable cap handler, or Event 42 history recorder.

The same country can receive later independent deliveries. Earlier history must not reduce or improve later package size.

## Conventional manifest registry

Create an event-owned curated registry for every safe conventional family and complete variant. Do not use bare designer chassis or empty airframes as finished rewards.

The registry must cover active DLC and non-DLC paths. Inspect current vanilla equipment and variant behavior directly. A selected family with no valid complete item rerolls into a comparable-value family. It never shrinks the package.

Implement the anchor, support, mismatch, family-count, magnitude, technology, and quantity rules from the specification. Recipient economy, manpower, army, stockpile, fuel, supply, ideology, geography, and major status must not reduce quantities.

Centralize tuning in script constants or a documented event tuning file. Do not scatter family weights and quantity bands across event blocks.

## Landing reports

Create three to seven delayed report events across persisted owned and controlled states. Permit repeated states for small countries with different local themes.

Reports may apply bounded temporary landing-zone state modifiers and rare visible recovery accidents. They do not grant more equipment or create more event history.

Persist the report chain through save and reload. Clean all temporary targets, arrays, flags, and report state after the final report.

## Evolutions

Implement one ordered global evolution track:

- Evolution I at 200+ Chaos, Everything Falls
- Evolution II at 400+ Chaos, Arsenal of the Future
- Evolution III at 600+ Chaos, Chaos Arsenal

Use normal paced evolution behavior around a ninety-day base with documented dynamic factors. Set the shared evolution context and record one actorless evolution entry per stage. Activation gives zero Chaos.

If an evolution is active before first firing, the first package uses it. Disabled stages cannot set recorded flags or unlock their content. Disabling a stage never deletes existing equipment.

## Nuclear stockpile

At Evolution II, implement the audited Chaos-scaled nuclear cache roll and substantial quantity bands. Use the existing nuclear stockpile effect.

Prove that a country without nuclear research can use the received weapons through ordinary valid delivery rules. Reuse a validated Event 23 physical-stockpile route when available. Otherwise create the narrowest launch-only compatibility contract.

The contract must not grant production, research, facilities, missiles, thermonuclear weapons, or permanent access after the finite stockpile is gone. Actual use must enter the existing nuclear, fallout, Deaths, Air Cleanliness, Condemnation, and Chaos pipelines once.

Do not mark Evolution II complete while the nuclear result is only a number that the recipient cannot use.

## Evolution III safety registry

Use `research/042_equipment_from_heavens_special_equipment_audit_matrix.md` as the starting matrix. Reinspect the live repository and installed game before finalizing it.

For each exact token, prove:

- physical stockpile grant works
- a real consumer exists
- the recipient can field or use it
- production remains unavailable unless normally earned
- AI can use it safely
- save and reload work
- owner event state is unchanged
- owner event can fire later without conflict
- cleanup is bounded

Create a minimal fielding or captured-payload receipt only when the owner API can separate use from production and lifecycle. Do not set owner-event host flags, evolution flags, project stages, facility flags, world-threat flags, source-country markers, focus unlocks, super-event flags, or terminal-route flags.

Keep unproven families excluded. Do not invent substitute special equipment.

## AI

Use the same recipient and package distributions for AI and players. Add one bounded post-delivery AI assessment for conventional, nuclear, and allowlisted special equipment.

Do not add free manpower, fuel, airbases, supply hubs, doctrine, research, commanders, or divisions. AI may reorganize and build ordinary infrastructure through existing systems. Every special family needs a defined AI fielding or payload path before allowlisting.

## Chaos impact

Implement the guarded Event 42 sources:

- +2 for the first successful public skyfall, once globally
- +10 for the first Event 42 nuclear cache that creates a genuinely new nuclear actor, reduced to +5 when the recipient already had launch access but no bombs
- +5 for the first fieldable owner-event equipment escape, or +10 when the verified family is a strategic mass-casualty payload

Evolution activation and ordinary repeat delivery add zero direct Event 42 Chaos. Actual use relies on shared systems and must not be double-counted.

## Cluster

Reconcile the accepted Various Anomalies assignment with the authoritative workbook and live cluster registry. Do not invent a numeric cluster ID when the source registry has not assigned one.

Register Event 42 as a Low member. Preserve independent Chaos level 1 eligibility. Enforce at most one Event 42 delivery per cluster transaction. Add clear invalid-recipient skip reasons and full cluster-history behavior.

## Event Log and Event Details

Wire the full Event Log contract:

- event name and debug name
- recipient actor mapping
- one history row per delivery
- detail text and manifest summary
- three evolution entries and details
- Events-tab type, Chaos level, weight, fired count, and enable state
- cluster member row and details
- `N/A` when no recipient exists

Do not expose hidden weights, internal tokens, or compatibility flags in player-facing text.

## Achievements

Implement the three routes from the achievement prompt with full snapshot, persistence, disqualifier, callback, icon, localisation, and documentation coverage.

## Assets and localisation

Implement the asset handoff only after final assets exist. Register six report-event sprites and nine achievement-state textures. Do not use placeholder art.

Write final localisation from the tone directions. Do not paste working labels or instruction prose. Keep localisation UTF-8 with BOM and align Event Details and workbook wording with the in-game text.

## Documentation and catalog

Create or update permanent Event 42 documentation, cluster documentation, compatibility registry documentation, achievement documentation, asset crosswalk, and task-specific validation notes.

Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`. Align Event 42 details, three evolution details, cluster membership, Low severity, Chaos level 1, and final implementation status.

## Mandatory audits

Before completion:

- run the named probability scenarios through `chaosx_ai_probability_auditor`
- use `hoi4.probability_compare` after any final weighted patch
- use `chaosx_localisation_auditor`
- use `chaosx_event_completion_auditor`
- use the correct asset reviewers
- run `chaosx_improvement_loop_planner` once after a meaningful implementation tranche
- reconcile every planner finding by implementing it, promoting it into specs, queuing it with a reason, or rejecting it with a reason

Do not claim completion while any nuclear-use proof, special-family row, asset, AI path, log surface, cluster registration, achievement callback, probability scenario, documentation row, or accepted plan remains unresolved.
