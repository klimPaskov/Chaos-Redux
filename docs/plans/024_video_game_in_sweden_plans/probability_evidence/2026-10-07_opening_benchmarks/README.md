# Event 24 opening benchmarks

These fixtures implement the accepted P24-O1 through P24-O4 analysis conditions without changing gameplay or choosing balance targets.
They are declared hypothetical benchmarks, not extracted campaign or save state.
The complete candidate pool remains `chaosx.nr24.2.a`, `.2.b` and `.2.c` in `events/024_hearts_of_iron.txt`.

High stability is represented by 0.75, above the public-opening threshold of 0.50.
The wartime non-crisis benchmark uses 0.65.
Low stability is 0.15, below both the 0.35 low-stability modifier and 0.20 severe-crisis threshold.
Adequate army experience is 50, and low experience is 10, on opposite sides of the source threshold of 25.
Low and high world tension are 0.20 and 0.75, on opposite sides of 0.50.
Calm World is 100 Chaos, Gathering Storm is 250, and 799 and 800 test the strict Totalen boundary.
These values are selected to exercise the existing modifiers, not replace source tuning constants.

P24-O1 declares both accepted government alternatives.
P24-O2 declares democratic government.
P24-O3 uses the accepted fascist branch and tests increasing Chaos rather than silently treating Gathering Storm as Totalen.
It does not claim to cover every possible non-fascist military or authoritarian government.
P24-O4 declares all four vanilla government alternatives, war, low stability and the actual source's supply-crisis and recent-core-loss flags.
This corrects handoff 27's omitted crisis receipts.

All cases declare independent Sweden, not capitulated, with the Swedish host target.
They are conditional on valid opening delivery and do not prove the event-level host gate, dispatcher, crisis observer, stockpiles or supply delivery.
The absence of the other crisis flags from each declared flag packet is intentional.
`compare_autonomy_state` is not assigned a fabricated ordinal for a non-subject country.
The source's subject helper should be false because `is_subject = false`, but any adapter inability to establish that must remain an explicit unresolved item.
Subject and autonomy campaign coverage remains due separately.

The field names follow the installed 3.10.0 `docs/probability.md` scenario contract and `schemas/probability-scenario-set.schema.json`.
The connected route must still validate the actual request and its supported alternative enumeration.
The audit must begin with `hoi4.probability_inspect`, then evaluate these exact named scenarios and preserve candidate traces, branch bounds, revisions, scenario hashes and artifact limits.
No manual probability calculation, synthetic helper override or self-comparison may substitute for the required MCP evidence.
