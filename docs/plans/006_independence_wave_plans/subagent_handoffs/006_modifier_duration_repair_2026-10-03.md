# Event 006 decision modifier duration repair

Disposition: implemented, source lifecycle audited, post-fix live behavior remains unobserved.
Acceptance basis: the user-authorized orchestrator supplied the four native decision errors from scenario 013 at HEAD `d51bba41f` on 2026-10-03 and requested a family-wide repair with no simplification.
The user instructed the parent to take recommended implementation choices without waiting for input.

## Source correction

The complete `common/decisions/006*.txt` inventory contains 808 decision blocks, including 307 with a decision-level `modifier` or `targeted_modifier`.
Nested AI `modifier` blocks were excluded from this count.
Exactly four modifier-bearing decisions lacked `days_remove`.
All four are repaired, and the repeat inventory reports no remaining missing durations.

| Decision | Removal duration | Factory commitment | Outcome timing |
| --- | --- | --- | --- |
| `independence_wave_choose_client_future` | `independence_wave_decision_duration.strategic`, 300 days | Existing standard commitment, two factories | Immediate on selection |
| `independence_wave_mnt_codify_durable_sovereignty` | `independence_wave_decision_duration.strategic`, 300 days | Existing light commitment, one factory | Immediate on selection |
| `independence_wave_challenge_league_leadership` | `independence_wave_decision_duration.standard`, 120 days | Existing standard commitment, two factories | Immediate on mission selection |
| `independence_wave_transform_league_charter` | `independence_wave_decision_duration.long`, 180 days | Existing standard commitment, two factories | Immediate on mission selection |

The removal clock begins after selection and is distinct from the mission timeout clock.
The two selectable missions retain their existing 120-day and 180-day mission deadlines.
The immediate settlements use the centralized strategic duration that matches their existing strategic payment family.
The native timer presents the duration without duplicating it in prose or introducing an idea carrier.

The charter sets its global active flag in its own successful completion block.
Its political cancellation conditions therefore need a success-receipt guard to avoid immediately waiving the factory reservation.
Leadership uses the equivalent successful-challenge receipt.
Pending missions retain all existing cancellation conditions, and Event 006 origin shutdown remains an unconditional cancellation condition.
After successful selection, later political changes leave the paid factory reservation running until its removal timer expires.
No failure or reward effect was moved between lifecycle blocks.

## Review and validation

`chaosx_decision_mission_auditor` independently reviewed the four durations and recommended both success-receipt guards.
It confirmed that timeout failure outcomes remain unchanged because the successful receipts are absent on the failure path.
The parent checked 256 source predicate cases across active/ended origins, membership, client lock, crisis phase, charter state, high-chaos eligibility, and pending/successful states.
Pending cancellation matched the previous predicates in every case, and successful reservations canceled only on origin shutdown.
This is a source contract check, not observed native engine behavior.

For both selectable missions, structural comparison confirms unchanged activation, availability, affordability, modifier magnitude, mission deadline, completion effects, timeout effects, and AI expressions.
All other decision blocks remain unchanged.
The repair changes only `common/decisions/006_independence_wave_decisions.txt` and `common/decisions/006_independence_wave_balkan_decisions.txt` plus this evidence.
No assets or catalog wording change is required.
No simplifications were made within this repair.
The full Event 006 implementation and project-wide clean-log goal remain incomplete.

The orchestrator confirmed that the earlier unknown variable-trigger and `clear_global_flag` errors no longer appear at `d51bba41f` following commit `f23bf79542e371c67b2035785abffa85d3803c18`.
That supplied live result closes those specific startup findings.
It does not establish that the present timer correction has been observed in game.

## Reference evidence

The connected `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` routes were exposed and callable in the parent context.
A decision context limit of two omitted source kinds, so the parent repeated it with limit ten and obtained no omitted or missing sources.
Only pertinent detailed sections were treated as read coverage.
The independent decision auditor could not call those routes in its own context and used the local files, while the parent performed live retrieval.

| Source | Read lines | Revision or SHA-256 |
| --- | --- | --- |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 337-356 and 467-482 | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` | 1-46 | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | 1066-1080 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_generic_decisions.txt` | 303-368 | `83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md` | 2202-2205 | `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 216-221 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `common/script_constants/006_independence_wave_constants_registry.txt` | 992-1011 | `215fe277fa18e912c90a2bd59706568410227e5cfd6ea0a7da65a03591f328f4` |

Vanilla `war_propaganda` is the inspected precedent for an immediate completion receipt plus a temporary decision modifier bound by `days_remove`.
The repository already uses matching removal and mission timeout durations for eight other modifier-bearing selectable missions.
The parent retained those precedents while fixing the two political post-selection cancellation guards.

Live reference and source results, including their paths, spans, and revisions, are retained in [the MCP reference evidence](../mcp/006_modifier_duration_reference_20261003.json).
Source lookup was refreshed after a revision-bound continuation reported `SOURCE_REVISION_STALE` during the parent edit.
The fresh charter read identifies the removal duration and success receipts in indexed revision `e605315c074d05b0040e7c6cf57b2dfe332026b9b175e04373576fc8965bde1c`.
Exact-ID decision scenario inspection was requested for all four decisions and remains pending at this source commit.
