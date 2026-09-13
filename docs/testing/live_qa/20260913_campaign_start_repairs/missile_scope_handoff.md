# Missile state-scope repair

Disposition: implemented within the user's request to fix campaign-start errors.
The pasted batch contains 3,915 invalid State-scope `exists` evaluations at `032_missiles_triggers.txt:164`.

The eight state helpers in `common/scripted_triggers/032_missiles_triggers.txt` now start with `scope_exists = yes`.
Country recipient, command, targeting, rogue-actor, achievement, and CXT gates retain `exists = yes`.
The other seven helpers share the exact reported defect and are reached through state-target decisions, controlled-state iteration, selected target states, and registered launch-site arrays.
Ownership, control, infrastructure, capital, damage, capacity, flags, cooldowns, and arithmetic are unchanged.

Installed `documentation/triggers_documentation.md` declares `exists` as Country-only and `scope_exists` as valid in any scope.
The offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, and `Data structures - Hearts of Iron 4 Wiki.md` provide the parallel scope and existence references.
The decision callers in `common/decisions/032_missiles_decisions.txt` use `FROM` as their state target, and the operation effects use controlled-state and launch-site array scopes.

`missile_scope_receipt.json` records original and final byte hashes and the exact eight names.
Reversing those eight substitutions restores the complete baseline text, proving no other script content changed.
The original bytes are retained under `baseline/missiles/`.
The read-only probability auditor captured the pre-edit inspection and found no weighted surface defined in the helper file itself; linked weighted consumers are covered separately in its handoff.

No gameplay simplification was made.
These source checks do not execute a campaign or prove a fresh runtime log is empty.
