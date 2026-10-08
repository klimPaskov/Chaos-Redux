# Planning-package improvement pass, 8 October 2026

The user requested another review of all current planning packages, specifically improving their design, connecting events where useful, making explanations clearer and reducing bloat.
This authorizes planning and documentation changes, with parent review of new design choices.
Gameplay, assets and catalog implementation remain separate work.
Event 091 was excluded from the preceding import and must not be imported in this pass.

## Review standard

Review every assigned package, including its authoritative design, existing connections, current acceptance/disposition records, and relevant previous improvement work.
The 7 October audit and the 098–100 import reviews supply prior cleanup evidence, not a reason to skip the new design review.
Existing accepted implementation backlog stays queued because this request concerns plans; build on its recorded design instead of creating competing addenda.
Identify a concrete weakness before proposing expansion.
Preserve user-required identity, branches, achievements, difficulty, historical grounding and accepted mechanics.
Preserve unresolved design alternatives as alternatives; do not choose a branch by treating existing code as approval.

Useful improvements clarify an actual player choice, connect existing consequences, remove an exploit or contradictory timing rule, give an existing route a stronger purpose, or consolidate repeated explanations into a better canonical passage.
Do not add the same integration table or generic safeguard paragraph to every package.
Do not manufacture a new meter, interface, country, world-end, subsystem, resource or repeated event merely to create a connection.
The amount of editing should follow the weakness found; an evidence-backed decision to retain an already strong package is acceptable.
Replace or integrate text where it belongs instead of stacking a new appendix onto each spec.
Short connections must still identify the actual condition, affected actor/state, player consequence, existing owner, overlap behavior, AI implication where meaningful, and a distinguishing acceptance case.
They must remain optional when the other event is absent or disabled and must not force-fire or grant another event's progression.
An existing consequence may have several consumers but only its owning system applies the underlying loss, payment, reward or Chaos receipt.
Preserve ordinary play when the connection is unavailable.

Use chaos-redux-improvement-loop and chaos-redux-event-planning, with relevant owner skills and repository source evidence.
Use primary research when introducing new historical or scientific claims, and distinguish inspiration from fact.
Do not claim engine feasibility from a prose review.
Actual engine-facing or weighted source auditing requires its normal references and MCP evidence; propose named future validation cases rather than treating them as executed.
No gameplay or AI-weight patch is in scope.

## Ownership and delivery

Each planner owns only its assigned group handoff and external candidate files.
Read other packages to verify proposed connections, but do not edit another group's files.
Do not edit canonical specs directly before parent review.
Prepare candidate text files outside the repository with an exact base copy, original SHA-256, candidate SHA-256 and intended repository path.
Keep a machine-readable candidate manifest and an LF unified patch outside the repository for parent review and application.
Write one concise group handoff under this directory's `handoffs/`, covering every assigned package, exact candidate changes, design rationale, connected owner references, previous-addendum disposition, checks and remaining uncertainty.
New proposals remain unresolved until the parent explicitly accepts them within this request and promotes the reviewed text.
No staging or commits by workers.

All agents share the checkout and must preserve other work.
Use explicit UTF-8 byte IO and `rg --no-mmap` on Windows.
Do not edit these already-dirty files without first reporting the exact need to the parent: Event 006 README, quality/package_manifest.md, quality/spec_acceptance_checklist.md, spec parts 6 and 7, and its untracked specs/006_signature_payoff_contract.md; Event 016 specs/016_final_completion_contract.md; Event 025 handoffs/025_completion_status.md, handoffs/025_process_limitations.md, matrices/025_requirement_coverage.md and package_checksums.sha256.
Read them where relevant and preserve their acceptance decisions.
Keep archive manifests, original source ledgers, dated audit receipts and original briefs immutable as historical evidence.
Refresh only genuinely current inventories after the parent applies accepted edits.
Do not execute attached production prompts, create source snapshots under the repository, launch HOI4, generate assets, or edit XLSX/CSV sources.

Shared identifiers remain parent-owned.
Reuse the central registry and current owners; flag any new allocation need rather than inventing an ID.
Presentation slots 119 and 120 are already reserved for New Ore and Sandstorm, independently of audio IDs.
The parent owns cross-group consistency, final scope review, coverage proof, validation and the isolated commit.
