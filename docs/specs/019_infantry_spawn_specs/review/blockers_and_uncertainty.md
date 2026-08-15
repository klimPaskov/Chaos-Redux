# Blockers and Uncertainty

> **Current-state notice (2026-07-18):** The two owner decisions described in
> this file are resolved: controlled one-formation border trials and exact
> recorded-formation recreate/prove/delete are approved. The later
> near-completion improvement addendum is implemented. The fixed identity-scene
> package is 20 claimant army/muster scenes, 6 fantastical massed-host scenes,
> and 1 neutral unassigned muster scene, with no individual focal person. Every
> gameplay specialist gate is clean, including the live-final AI, balance,
> performance, isolation, scenario-safety, and exploit reaudit with zero P0, P1,
> or P2 findings. The owner-approved deterministic spot-colour route now has a
> 91-row raw, spot-master, native PNG, and runtime TGA candidate. Visual and
> runtime rows pass. The independent remediation re-audit handoff
> `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`
> is PASS and clears the regional asset gate for parent-owned package
> promotion. The machine JSON retains its immutable literal
> `candidate_requires_independent_visual_review` processor-state value, which
> is superseded for approval by the separate PASS handoff and was not edited.
> Dated passages below remain useful
> evidence but do not override
> `docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`
> or the newest specialist/final audit handoffs.

> **Provider-extension notice (2026-08-09):** The static Event 19 provider bridge now covers 18 IDs (`501-514`, `518`, `520-522`), including the separate five-gate Event 016 Aryan clone provider 522 and exact multi-resource profiles 130-148. Provider 521 remains combat-only on the CBRN side, and provider 513 remains dormant until Event 012 sets `africa_strange_formation_package_ready`. The historical closure wording in this planning review does not replace current MCP evidence: Event 19 inspection is partial, the bounded render attempt timed out, and normalized dynamic provider-pool odds remain unresolved.

## Current implementation status

The repository, offline wiki, installed HOI4 1.19.2 documentation, vanilla files,
and approved reference mods have been inspected locally. Project subagents were
run with no inherited parent context for bounded implementation, assets,
transaction review, and exploit auditing. Local identifiers for the ordinary
formation pool, helicopters, zombie variants, ghost units, coal golems, dynamic
country creation, scripted GUI, achievements, Event Log, and triggerable
scenarios have been verified against the installed code and documentation.

The old planning-environment blockers are closed. The owner approved controlled
border trials for the exact-formation achievements and the exact recorded-
formation recreate/prove/delete contract for natural revolts. Neither capability
uses an unapproved fallback.

## Exact recorded-formation transfer

The revolt contract requires natural claimant and anomalous-family derivative
revolts to transfer only the loyal Event 19 formations recorded for that
claimant or family. SCN-013 can create fresh exact formations after a dynamic
country is proved, but that path does not solve ownership transfer for live
ordinary-country formations.

HOI4 1.19.2 documents country-ratio transfer and whole-army annex transfer, but
does not expose a division-scoped ownership-transfer effect. The installed
vanilla scripts and approved reference mods do not provide a stronger supported
operation.

A final no-context capability recheck on 2026-07-16 enumerated every documented
division-scope effect. The engine can enumerate and retain an exact division
scope, but the available mutations cover organization, template, history,
medals, commander experience and traits, officer promotion, reseeding, or
destruction only. `transfer_units_fraction` remains country-scoped and
ratio-based; meta effects cannot synthesize an ownership operation the engine
does not register. No exact precedent was found in vanilla or the approved
reference mods.

The approved exact recorded-formation contract is a recreate, prove, delete
transaction:

- freeze the exact Event 19 UID/cohort set, immutable issue manifest, ledger
  identities, starting factors, obligations, auxiliary memberships, claimant,
  territory, and global accounting boundary;
- create a locked dynamic actor and rebuild only that frozen set through the
  sole consolidated registry;
- prove the complete destination army, private ledgers, territory, claimant, and
  unchanged global Event 19 accounting before deleting a source cohort;
- delete only the exact proved source cohorts with no refund, prove source zero,
  and then commit and prove source accounting once;
- on pre-commit failure, remove and prove the destination replacements, annex
  the unpublished actor with troop transfer disabled, return territory, recreate
  only missing frozen source UIDs, and prove the complete restored source set.

The engine does not expose exact live per-equipment inventory, exact live
manpower fill, organization, veterancy, medals, officer history, army assignment,
or orders to this script path. Those properties are explicitly outside the
approved contract and are not guessed. A conservative two-sided `unit_strength`
gate requires the live source to be at or above the larger recorded starting
equipment/manpower factor and proves the replacement at or below it, preventing
the transaction from repairing a damaged formation.

The runtime evaluates every aligned registry provider, calculates family
pressure and live presence, selects the strongest eligible row without a family
list, builds a connected non-capital region from recorded unit origins and the
linked claimant headquarters, and completes the locked transaction only for
the exact verified set. It uses no blanket army transfer, fresh unrecorded unit,
ordinary-division substitute, random formation, fixed tag, or takeover fallback.
One-state countries remain covered by the existing takeover or failed-coup
logic and do not require territorial transfer. If rollback actually has to
recreate a missing source UID, a permanent country flag fails closed against a
second natural recreate/delete transaction.

Ordinary-country annex cleanup is not blocked by this limitation because it
destroys, rather than transfers, the removed country's exact Event 19 set. The
annex path locks its templates, deletes only proved unit UIDs/delete cohorts in
the removed country or annexer, proves unit and template absence, then clears
claimants, state markers, missions, ideas, attempts, scenario state, and aligned
ledgers. Its first valid preflight freezes the exact unit, delete-cohort, and
template evidence before deletion. Any failed proof sets the annex-cleanup
invariant quarantine, keeps that frozen set, and queues the exact removed
country on the annexer for a delayed retry. Queue ownership migrates across a
later annexation, and no entry is discarded until the full finalizer positively
sets `infantry_spawn_country_cleanup_complete`.

## Controlled combat-trial resolution

The owner approved controlled Event 19 border trials for the four exact-formation
combat achievements. This resolves the former same-battle capability blocker
without inventing casualty or force-ratio evidence that the engine does not
expose atomically.

Each state-targeted trial freezes the exact generated attacker division and its
unit, generation, lot, template, composition, quality, coherence, readiness,
technology, attacker-state, defender-state, defender-country, and trial-type
evidence. The attacker and defender states each prove one literal sole
participant. The defender is a temporary locked one-battalion detachment owned
by a peaceful independent AI country in an empty adjacent state. The border-war
engine enforces a fourteen-day minimum engagement and does not transfer either
state.

Player and AI countries use the same decision and launch effects, including
type-specific Army Experience and Command Power costs. Every started trial
receives the same cooldown. Attacker and validated defender callbacks converge
on nonce-bound win, loss, and cancellation handlers. Timeout, invalid state,
outside war, civil war, ownership change, or extra participants cancel the same
transaction. Cleanup removes only the exact temporary unit and unique template,
proves both are absent, and quarantines any failed proof before releasing the
opponent lock.

## Dynamic country creation

Safe dynamic creation is implemented and is the required path. No fixed-tag
fallback has been introduced. Dynamic setup uses coherent state selection,
provisional ledger snapshots, verified package creation, rollback, deferred
government/AI installation, and cleanup retries. A fixed-tag fallback remains
forbidden unless separately approved.

## Parent isolation

Zombie, ghost, and golem identifiers were verified locally. Their Event 19
providers use the shared special/nonhuman classifiers and explicit source-event
and parent-isolation profiles. Derivatives do not set parent participant tags,
do not advance parent counts or stages, and do not set any terminal world-end
flag. The root isolation recheck also separated ghost population decline from
Event 10's cause ledger: one real loss is registered once under dedicated
Deaths reason 20, `infantry_spawn_ghost_decline`, without entering consumed-state
or soul counts. The live registry/scenario, country-package, and live-final AI,
balance, performance, isolation, and exploit reaudits are clean for these
invariants.

## Assets

The current asset handoffs own visual completion and integrity evidence. The
twenty claimant, six derivative, and one neutral technical fixed sprite slots
retain their stable GFX identifiers and gameplay mappings, but their contract is
an army, muster, or massed-host scene without an individual focal human. This
document therefore defers source, processed, runtime, hash, and consumer-
coverage claims for those twenty-seven slots to those handoffs. The remaining
report cards, focus and decision icons, idea icons, board and category UI,
achievement triplets, and frame-sheet animations remain under the manifest and
asset-handoff inventories. The 91 regional flag identities now use the
owner-approved Event 019 deterministic spot-colour flattening route. The
current chain is 91 unmodified full-flag ImageGen raws, 91 deterministic 820 by
520 spot masters, 273 native PNGs, and 273 bottom-left-origin runtime TGAs.
Visual and runtime rows pass, and the seven retained GHOST_BASE prompt records
were recovered exactly from the original archive. The independent remediation
re-audit handoff is PASS and clears the regional asset gate for parent-owned
package promotion. See
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`.
The machine JSON retains the immutable literal
`candidate_requires_independent_visual_review` processor-state value, which is
superseded for approval by that PASS handoff. The 7/16 `regional_variants/` composites,
motif/composite notes, validation/checksum pair, and contact sheets are archival
superseded evidence.

The no-focal-person rule is limited to the twenty-seven fixed identity slots and
their UI, scenario, or authority reuse. Independent report, focus, decision, and
achievement illustrations are separate asset classes under their own briefs and
do not represent a claimant, commander, council, or derivative authority.

The claimant identity pool contains no global catch-all. Profiles 04 and 12 are
explicitly compatible with their documented Asia/Australasia diaspora pools,
profiles 09 and 13 carry their documented European/North American and
European/South American pools, and profile 20 is Australia-only. Every supported
origin region therefore has at least three compatible identities for the three-
claimant ceiling without a regionally mismatched name. Visual proof for the
fixed identity-scene slots is deferred to the current asset handoff.

## Localisation and catalog

Final in-world English localisation is wired in the existing Event 19 file. The
catalog workbook records Event 19 as ID 19 and Minor Repeatable, supplies all
four evolution records, leaves cluster fields empty, and includes SCN-013. Both
are `Fully Functional` after the completed workbook/catalog reconciliation,
export, 33/33 package inventory, and final completion audit. The fixed
army/host/neutral identity-scene package is present and wired. B-019-001 and
B-019-002 are closed through the two owner-approved engine-constrained
substitutes described below. The four SCN-013 type summaries and four intensity
summaries match the in-game wording exactly.

## Final audit closure

The weighted-obligation, manpower-liability, request rollback,
standardization, supervised salvage, unaccounted-unit settlement, and same-tag
scenario transaction passes are implemented. Same-tag deferred replay covers
all 53 current routed outcomes. Successful direct ordinary actors receive the
minimum applied evolution profile required by their scenario type, retain a
higher pre-existing applied stage, and are then frozen out of later ordinary
global evolution history. Paid zombie, ghost, and golem reinforcement now uses
a proved request snapshot and rollback boundary; a refund is permitted only
after a clean rollback, while a rollback failure stays quarantined and receives
no cooldown or reinforcement credit. The original 52-route tranche and bounded
ledger compaction have independent clean audits; the later
prototype-maintenance route has root structural validation. A later required
named planner run produced the near-completion addendum; its natural-release,
first-family reception, documentation, and asset findings are implemented. The manual review
findings are remediated: all three dynamic decision categories place runtime
gates in `visible`, and derivative ideas occupy four distinct, mutually
exclusive tracks: government recognition, family command,
logistics/doctrine/sustainment, and former-parent/expansion. Encircled Remnant
completes the four-form defeat matrix.

The current no-context focus-tree, decision/mission, country-package,
localisation, registry/scenario, evolution-counter, and live-final AI, balance,
performance, isolation, scenario-safety, and exploit reaudits each closed with
no P0, P1, or P2 finding. The evolution-counter reaudit specifically supersedes
the earlier recurring global-country scan finding. Maintained country-local
receipts and counters now drive the bounded work. All gameplay specialist gates
are clean. The independent regional-flag remediation re-audit is separately
PASS, recorded in
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`.
These specialist verdicts are reinforced by the final completion audit
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md`,
which is PASS with P0/P1/P2 = 0. Parent package inventory is complete at 33/33
current files, and the catalog promotion is complete.

The authoritative live-final AI evidence is
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_ai_balance_performance_live_final_reaudit_2026_07_16.md`.

The earlier final completion audit reviewed the then-current runtime, workbook,
assets, and shared systems. Its B-019-001 and B-019-002 findings are closed as
design blockers by the two approved substitutes, but that dated audit predates
the current transfer, registry v4, evolution-counter, and visual-source state.
It is historical evidence, not a completion verdict for the current project.

## Final closure status

The final completion audit
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_completion_audit_2026_07_18.md`
is PASS with P0/P1/P2 = 0 and authorizes the `Fully Functional` promotion.
Parent package inventory is complete at 33/33 current files. Event 19 and
SCN-013 are `Fully Functional`, and no closure gate remains.

## Historical pre-inventory-completion gate wording (superseded)

1. Reconcile the remaining parent package inventory after the PASS regional-flag
   remediation handoff. Parent workbook/catalog export and reconciliation are
   complete, with Event 19 and SCN-013 intentionally remaining `In progress`.
2. Run the final completion audit only after the package inventory
   reconciliation is
   complete. Regenerate `review/package_contents.md` last, after every
   hash-affecting edit.

## Historical pre-PASS gate wording (superseded)

1. Run the independent remediation re-audit against the unchanged 7/18 raw,
   spot-master, native PNG, and runtime TGA rows after the documentation
   corrections. The visual and runtime row review already passes, and no raw row
   or runtime file is to be regenerated for this gate.
2. Reconcile parent documentation, workbook status, generated catalogs, and
   package inventory. Event 19 and SCN-013 remain `In progress` unless that
   evidence justifies promotion. The workbook export remains parent-owned and
   the CSV files remain export-only.
3. Run the final completion audit only after the parent reconciliation is
   complete. Regenerate `review/package_contents.md` last, after every
   hash-affecting edit.

The clean specialist surfaces, regional asset review, and final completion
audit are closed without a concrete regression. No unapproved fallback was
used to clear a gate.

## Simplification statement

Exactly two engine-constrained substitutes were explicitly approved by the
owner and are implemented: controlled one-formation border trials for the four
exact-combat achievements, and the recreate/prove/delete transaction for
transferring exact recorded-loyal Event 19 formations. The separate
Event-19-only regional-flag exception uses 91 independent full-flag ImageGen
raws followed by deterministic full-colour spot-palette normalization. No
additional fallback, fixed tag, country-level battle proxy, blanket army
transfer, random formation, guessed live-state compensation, or silent omission
is treated as complete. The remaining capacity limits on the read-only HOI4
inspection tools are validation-tool constraints, not a source implementation
blocker.
