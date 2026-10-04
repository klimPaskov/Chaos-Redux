# Event 021 catalog changes pending

Disposition: accepted and queued.
Acceptance basis: agent decisions D5, D6, and D11 in `agent_decisions_2026-10-04.md`, taken under the user's full-authority takeover grant.
Queue reason: implementation agents may not edit `docs/spreadsheets/chaos_redux_events_catalog.xlsx` or its CSV exports; the spreadsheet owner applies these rows and then runs `python .tools/export_event_catalog_csv.py`.
No spreadsheet or CSV file was edited.

Row: ID 21, Random Civil War.
Status stays **Needs Testing**.

## Details

Reason: the current Details text omits two behaviors that exist in the game.
When Evolution I activates, a war already under way is reviewed and either gains new regional sides or moves its government and claimants into the front-management phase.
A claimant that replaces the government receives a choice to open a new war for its own core or claimed territory against the old government's foreign enemies, or to decline.
The proposed first paragraph is the in-game text of `event021_event_log_detail`; the Settlement and Reconstruction sections are unchanged and match `event021_event_log_detail_settlement` and `event021_event_log_detail_reconstruction` without their live crisis summary.

Proposed Details:

```text
A country's chain of command has split between rival political and military authorities. Capitals, supply routes, public legitimacy, and the terms offered to each front will shape the conflict. When the fronts gather, a war already under way can draw in new regional sides, or its government and claimants take firmer command of the fronts they hold. A claimant that replaces the government can open a new war against the old government's foreign enemies for its own core or claimed territory, or let that quarrel lapse.

Settlement

The sides have accepted terms based on recognition, autonomy, coalition, partition, or disarmament. The peace will last only if every signatory meets its obligations.

Reconstruction

The fighting has ended. Repaired railways, restored civil administration, demobilization, and fulfilled peace terms will determine whether the settlement lasts.
```

## Evo I

Reason: the current text says new commands entered "the first war", which no longer describes the stage: Evolution I reviews every war already under way, opens a new side only where a region can stand on its own, gives the other wars the front-management phase, and lets new crises open on several fronts.
The proposed text is the in-game text of `event021_evolution_i_body`.

Proposed Evo I:

```text
Rival commands and regional movements are joining the civil wars already under way. Where a region can hold its own capital and forces, a new side takes up arms; elsewhere, governments and claimants tighten their grip on their fronts. New crises can now open on several fronts at once.
```

## Unchanged fields

Evo II, Evo III, Type (Minor Repeatable), Chaos level (1), Cluster ID (1), and Status (Needs Testing) are unchanged.
