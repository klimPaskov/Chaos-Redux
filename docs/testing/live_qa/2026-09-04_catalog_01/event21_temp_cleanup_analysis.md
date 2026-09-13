# Event 021 temporary cleanup analysis

Disposition: implemented after parent acceptance of the three exact terminal deletions.
Acceptance basis: the parent authorized bounded read-only investigation of the supplied launch_07 errors and this analysis document; gameplay edits are not authorized in this subtask.
The read-only research worker did not modify gameplay.
The parent applied the three exact terminal deletions after reviewing all inventories and caller continuations; originals are archived under pre_patch_event21_temp_cleanup/.

## Exact affected files and proposed repair

The log resolves the first filename to `common/scripted_effects/021_random_civil_war_parent_effects.txt`, not `021_random_civil_war_effects.txt`.
`logs/launch_07/logs/error.log:1819–1820` reports its unknown `clear_temp_variable` effect at source line 4674.
Log lines 1825–1828 report the two corresponding commands in `common/scripted_effects/021_random_civil_war_treaty_effects.txt:406–407`.
The repeated reports at log lines 4834–4843 describe the same three source commands.

After the independent inventories below, the minimal proposed patch is deletion of exactly these three terminal commands:

```diff
--- common/scripted_effects/021_random_civil_war_parent_effects.txt
-	clear_temp_variable = event021_parent_wars_cluster_prefire_active
--- common/scripted_effects/021_random_civil_war_treaty_effects.txt
-	clear_temp_variable = event021_treaty_binding_accepted
-	clear_temp_variable = event021_treaty_binding_crisis_id
```

Keep all entry assignments and conditional writes in place, including the currently unread parent scratch assignments.
Do not introduce exit zero assignments, persistent flags, or `clear_variable` replacements.
Do not change helper names, call sites, treaty predicates, recipient/actor filters, weights, target arrays, ticket expansion, random draws, or reservation behavior.
This recommendation is based on each identifier's current consumers; it is not a general permission to delete temporary cleanup commands elsewhere.

## Documentation basis

Installed vanilla `documentation/effects_documentation.md:2773` documents `clear_variable` without explicitly claiming support for temporary variables.
The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `clear_variable` table entry, explicitly limits that command to regular variables.
Neither installed effects nor triggers documentation contains `clear_temp_variable`.
The installed effects documentation at line 7820 and triggers documentation at line 7482 document `set_temp_variable` as supported assignment.

The offline Data structures Variable types section at lines 410–419 explains that temporary variables are unscoped, exist within their enclosing effect/trigger lifetime, and do not carry into events.
It warns that values created inside scripted helpers do not always survive into callers; no proposed deletion depends on such survival.
The proposal relies on ordinary temporary lifetime only after the final local read, not on precise deletion at the helper's closing brace.
It does not treat zero as equivalent to absence.

## Inventory 1: parent cluster prefire scratch

Identifier: `event021_parent_wars_cluster_prefire_active`.
Containing helper: `event021_parent_prepare_random_event_fire`, COUNTRY scope, starting at parent effects line 4546.

| Source line | Operation | Role |
| --- | --- | --- |
| 4548 | Unconditional temporary assignment to `constant:random_civil_war_value.zero` | Initializes the invocation's scratch value |
| 4551 | Temporary assignment to `constant:random_civil_war_value.one` when `event_cluster_member_fire_context` is set | Records current cluster context locally |
| 4674 | Unsupported terminal clear | Cleanup attempt after reservation handling |

There are exactly three runtime references, with no reads anywhere in `common`, `events`, `interface`, or `localisation`.
A second repository-wide TXT/GUI/GFX/YML search excluding documentation and the offline wiki confirmed the same three references.
There is no absence test, scoped alias, regular-variable assignment, arithmetic read, or helper parameter consumer for this identifier.
The actual cluster behavior checks `has_country_flag = event_cluster_member_fire_context` directly; it does not read this scratch value.

The helper's sole runtime caller is `fire_event_by_temp_id_no_cluster` in `common/scripted_effects/chaosx_settings_effects.txt:4570`.
That caller checks `event021_parent_prefire_ready` after return and may disable firing or calculate the next timer; it never reads the cluster scratch.
`event021_parent_prefire_ready`, the temporary target pool, the selected event target, and persistent reservation flags are separate outputs and must remain untouched.

Minimal repair: delete only the terminal clear at line 4674.
Ordinary and cluster calls retain exactly the same candidate weights, cursor movement, target selection, readiness result, skip reason, and target reservation.
A repeated call overwrites the scratch at entry; there is no read-before-initialization or stale-value consumer even before that overwrite.
The two unused assignments could be considered separately as dead-code cleanup, but their removal is unnecessary for the confirmed error and is not proposed.

## Inventory 2: treaty acceptance scratch

Identifier: `event021_treaty_binding_accepted`.
Containing helper: `event021_treaty_prepare_signatory_obligations`, COUNTRY settlement-owner scope, starting at treaty effects line 288.

| Source line | Operation | Role |
| --- | --- | --- |
| 292 | Unconditional temporary assignment to zero | Default rejection for this invocation |
| 300 | Temporary assignment to one when `event021_treaty_binding_owner_ready` passes | Initial owner acceptance |
| 341 | Temporary assignment to zero after an intended actor fails front/owner proof | Reject the complete binding transaction |
| 349 | Equality check against one | Gates actor obligation binding and the prepared receipt |
| 406 | Unsupported terminal clear | Cleanup attempt after prepared/rejected receipt is written |

There are exactly five runtime references, all inside this helper.
The scratch is initialized before the owner predicate, before either actor loop, and before its sole read.
There is no external read, input contract, absence check, or persistent variable with the same name.

Minimal repair: delete only the terminal clear at line 406.
Keep the existing entry zero as its explicit rejection sentinel and preserve both conditional writes.
Owner-ready, owner-not-ready, valid-actor, invalid-actor, empty-actor-list, and repeated-call paths all reach the same prepared/rejected flag behavior because the cleanup occurs after that result has already been written.
No new default is introduced.

## Inventory 3: treaty crisis identity scratch

Identifier: `event021_treaty_binding_crisis_id`.
Containing helper: the same treaty preparation helper.

| Source line | Operation | Role |
| --- | --- | --- |
| 293 | Unconditional temporary assignment to zero | Explicit local value when the owner lacks a crisis ID |
| 296 | Copy from the owner's `random_civil_war_crisis_id` after its existence check | Capture the owner identity before changing to actor scopes |
| 313 | Equality comparison against each actor's crisis ID | Restrict preflight to the owner's intended actors |
| 365 | Equality comparison against actor crisis ID | Restrict obligation writes to the same crisis |
| 374 | Inequality comparison against a prior durable treaty ID | Decide whether to mark the actor's prior agreement as recurrent |
| 407 | Unsupported terminal clear | Cleanup attempt after all binding work |

There are exactly six runtime references, all inside this helper.
The value is deliberately unscoped so it remains the owner's crisis identity inside actor loops.
This cross-scope use is required and must not be replaced with a country flag, scoped variable, or a late read of the actor's current crisis ID.
Both entry paths initialize it before any read: missing owner identity leaves the explicitly initialized zero, and existing identity is copied before loops.
The missing-ID rejection is independently enforced by `event021_treaty_binding_owner_ready`, whose source at `common/scripted_triggers/021_random_civil_war_treaty_triggers.txt:12` requires the owner's crisis ID.
Do not change that existing sentinel or add an early return as part of cleanup repair.

Minimal repair: delete only the terminal clear at line 407, preserving initialization, owner capture, and all three reads.
All identity-sensitive work occurs before the removed command.
A repeated preparation call initializes zero and copies the new owner's identity before actor scanning, so a prior owner's ID cannot leak into the next invocation's comparisons.

## Treaty helper callers, nested helpers, and absence semantics

The preparation helper's sole runtime call is in `event021_parent_apply_settlement`, `common/scripted_effects/021_random_civil_war_parent_effects.txt:4311`.
The parent selects settlement terms and the owner obligation, calls preparation, and immediately calls `event021_treaty_capture_settlement`.
That capture helper has separate `event021_treaty_capture_*` temporaries and uses `event021_treaty_capture_ready`.
The readiness trigger at treaty triggers lines 58–62 reads `event021_treaty_bindings_prepared` and the absence of `event021_treaty_bindings_rejected`; it does not inspect either temporary scratch identifier or their existence.
Those persistent prepared/rejected flags are cleared at preparation entry and set before the two unsupported cleanup commands, so their lifecycle is unaffected.

During actor binding, `event021_treaty_mark_recurrence` is called at treaty effects line 378 for an actor carrying a different durable agreement.
Its body at lines 1090–1164 initializes and uses separate lookup/index/recurrence scratch values and neither reads nor writes either binding scratch.
Its lookup helper `event021_treaty_find_agreement_row` also uses separate lookup fields.
Thus the binding crisis ID remains an internal cross-scope input, not a cross-helper input to recurrence; no helper-return cleanup requirement was found.

The matching owner documentation `common/scripted_effects/021_random_civil_war_treaty_effects.md` identifies prepared/rejected receipts and actor-local obligations as preparation outputs, consistent with these source consumers.
No temporary absence contract is documented there.

## Meaningful verification and scope limits

Completed source checks independently inventoried all 14 occurrences across the three identifiers, classified every write/read/cleanup, traced both sole direct callers, checked the capture continuation and its receipt trigger, and reviewed the recurrence helper reached from the binding actor loop.
All three unsupported commands occur after their identifiers' final local read; the parent scratch has no read at all.
No gameplay patch or runtime test was performed.

Current inspected SHA256 values are `5f394e9c318e71ac4f44a54a0da2dd9d586676a7af04907c934f1a4b9bca0e5f` for the parent effects file and `72ef1e631cfb6472982574ea617398ecca944d5f01885841e2869cdb0e9224d1` for the treaty effects file.
An implementing owner should recheck these files for concurrent changes, archive the immediate originals, and confirm the patch contains exactly the three terminal line deletions.
After deletion, verify all entry assignments, actor identity checks, prepared/rejected flags, weights, target pools, and direct outputs remain byte-identical outside those lines.

The mandatory narrow MCP trace for `chaosx.nr21.1` used downstream depth 1, 12 nodes, 20 edges, and helper expansion requested.
It returned `EVENT_INSPECTED_PARTIAL`, focused analysis, revision `524f2937a47d4d31bd89ec3b5e6185825935909d15ff955e2e35187522458d75`, with helper projections and lifecycle passes deferred and zero indexed helpers.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79ef26c3c39a50ad531c7d6b770757c6846f3e3b8864c344ef950872ce58cf84/1b0f26b05553e7ede6fb0e47f8fd1edb112349b546656ab2d7ab7750c5b6267c/event-trace-524f2937a47d.json`.
This is direct event evidence only and does not certify the cleanup helpers or game acceptance.
No full workspace expansion, probability evaluation, or probability comparison was performed: the proposed patch has no read by weighted logic, changes no weighted surface, and claims no balance result.

Only the parent and treaty effects files contain proposed gameplay edits; the main `021_random_civil_war_effects.txt`, settings, triggers, events, localisation, and other event packages are read-only context.
All active concurrent work remains protected.
No game, desktop, process, staging, or commit operation was performed.
Skills used: chaos-redux-events and chaos-redux-subagents; required data-structure and installed variable documentation were reused and rechecked.
No gameplay simplification or fallback is proposed.

Parent acceptance basis: user-authorized safe startup repair; no current consumer observes scratch absence or a downstream value, and entry assignments remain unchanged.
Native confirmation is pending launch 09.
