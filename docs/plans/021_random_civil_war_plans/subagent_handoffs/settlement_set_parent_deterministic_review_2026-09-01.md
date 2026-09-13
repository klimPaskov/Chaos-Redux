# Event 021 SET Parent Deterministic Review

Date: 2026-09-01

Scope: SET-01 through SET-06.

Classification: current-source deterministic branch and lifecycle review. SET is not a weighted pool in the implementation, so this report does not invent settlement probabilities or normalized option shares.

## Selector contract

`common/scripted_effects/021_random_civil_war_parent_effects.txt::event021_parent_select_settlement_terms` evaluates current front topology and then uses ordered deterministic branches.

The precedence is complete Event 006 independence, ordinary opposition victory, same-tag leverage or compromise, viable partition topology, viable merger topology, strong negotiated autonomy or coalition, then government victory. The topology review counts only live normal-human opposition actors with owned states and an owned and controlled front capital. Partition requires at least two durable fronts with distinct anchors and a preserved government remnant. Merger requires one durable regional or legal front, a preserved remnant, and open talks.

`event021_parent_apply_settlement` records the selected type, assigns a front-bound obligation, resolves or preserves the relevant actor, starts reconstruction and successor grace, prepares recurrence, and clears temporary settlement state.

## Named matrix

| Fixture | Deterministic current result | Disposition |
| --- | --- | --- |
| SET-01 government dominant and high authority | Without talks, government victory. With open talks and authority at or above the centralized strong-settlement threshold, autonomy is selected for a valid regional route and coalition otherwise. | Pass: military or firm negotiated settlement. |
| SET-02 independence actor controls homeland and has recognition | A complete Event 006 front, host, or Event 021-origin actor selects independence before ordinary opposition and topology branches. A non-Event 006 regional claimant can receive autonomy through the negotiated regional branch. | Pass: independence or autonomy is structurally preferred when its complete route is valid. |
| SET-03 several equal fronts and exhausted country | Two durable live fronts with distinct anchors select partition. One durable legal or regional front with talks can select merger. If those topology proofs are absent but strong talks remain valid, coalition or autonomy is selected. Separate front rows resolve independently before the whole crisis closes. | Pass: coalition, partition, merger, or separate-front resolution follows actual surviving topology. |
| SET-04 hardliner government with low legitimacy | A hardliner may reject talks and reach government victory. The pre-review source did not classify that non-negotiated victory as harsh or failed, so it created no recurrence cost. | Demonstrated defect; owner patch applied. |
| SET-05 negotiator government with enforceable guarantees | Negotiator AI raises the emergency-settlement action score. Open talks plus strong State Authority select coalition or regional autonomy and create a front-bound obligation with a finite hold date. | Pass: durable agreement is favored through action AI and deterministic enforceable terms. |
| SET-06 proposed settlement leaves a side without a viable state | Partition and merger topology ignore actors without owned states, a viable controlled capital, or sufficient distinct anchors. Invalid spatial settlements therefore cannot be selected; the branch falls through to another valid resolution rather than preserving a nonviable side. | Pass: invalid territorial settlement is excluded. |

## SET-04 owner patch

The harsh-settlement classifier now also covers a government-victory settlement when the country has `random_civil_war_hardliner_profile` and no `event021_settlement_talks_open` flag. It sets both `random_civil_war_harsh_settlement` and `random_civil_war_failed_settlement` before `event021_apply_settlement` prepares recurrence.

The existing centralized recurrence helper adds `constant:random_civil_war_settlement_tuning.failed_settlement_pressure` for that failed-settlement flag. No new magic value, settlement option, or weighted branch was introduced.

The negotiated classifier remains mutually exclusive with harsh settlement, so a hardliner who actually reaches valid talks does not automatically receive the repression penalty.

## MCP boundary

A source-line `hoi4.event_inspect` state-flow request against the selector completed as a full workspace projection rather than a bounded helper projection. It scanned 3,910 sources and returned 3,942 unrelated blocking diagnostics, so it is not used as SET acceptance evidence. Its artifact is retained only as a tooling-boundary receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cdb8a115efe42cb6d251cbb85e6769422e61ec5b71c2c7707aa70fcc2e3b222/90ed8a7fa1addec9648dc99207acf788a494039a28b06a130a4759584755d7d6/event-state_flow-85614836fc70.json`.

The SET family still needs an independent completion/probability specialist disposition confirming that deterministic settlement selection is correctly excluded from weighted probability claims and that the SET-04 lifecycle patch is accepted.
