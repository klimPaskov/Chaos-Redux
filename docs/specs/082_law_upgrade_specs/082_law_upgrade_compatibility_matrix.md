# Law Upgrade: law-owner compatibility matrix

This is a coverage and implementation contract, not a claim that every listed provider has been found or implemented. The supplied archive contains planning sources and shared documentation, not a complete installed-game and DLC inventory.

## Required owner contract

Each participating category supplies one authoritative record with the following meaning.

| Field or operation | Required meaning |
| --- | --- |
| Stable category identity | One real category, independent of translated name, tag, or menu order |
| Owning system and source | The actual law or policy owner and its maintained progression definition |
| Applicability | Whether the country genuinely has this category and its underlying institution |
| Current position | The exact current law or policy on the owner's wartime path |
| Minimum Event 82 profile | Baseline, I, or II, with III inheriting rather than duplicating participation |
| Immediate successor | At most one next position from the start-of-firing snapshot |
| Immediate predecessor | The owner's actual lower adjacent position |
| Structural prerequisites | Requirements that a forced mobilization cannot invent |
| Ordinary purchase gates | Political, support, and payment requirements bypassed only for the forced advance |
| Forced-change operation | An effect that performs exactly one valid change without ordinary purchase cost |
| Change result | Advanced, at cap, structurally blocked, not applicable, or unrecognized |
| Side effects | Existing owner consequences that must occur once with a real law change |
| Tier identity | Whether an extreme successor satisfies an existing minimum-mobilization condition |
| Manual adjacent price | Current ordinary price when an Event 82 reversal needs this category |
| Reconciliation | Behavior after inheritance, external removal, country change, or save load |

These are semantic interface requirements. They do not assert that HOI4 provides a native reflective registry or accepts arbitrary token dispatch. The scripted architecture must use actual supported owner integration.

The owner maintains its sequence once. Event 82 consumes that definition through a shared, testable interface or a generated integration whose source of truth is still the owner. Copying a second ladder into Event 82 is not accepted.

## Required release inventory

| Family | First profile | Planned treatment | Evidence currently available | Required before release |
| --- | --- | --- | --- | --- |
| Vanilla economy | Baseline | Advance one real step, append Totalen Krieg!!! | Legacy Event 82 call and offline idea documentation | Complete loaded economy file, helpers, legal costs, exact slot behavior |
| Vanilla conscription | Baseline | Advance one real step, append Totalen Menschen!!! | User brief and offline idea documentation | Complete loaded manpower file, levels, population formula, mobilization behavior |
| Vanilla trade | I | Advance toward Closed Economy | User brief and project design sources | Complete loaded trade file, actual order, forced-change effects |
| Country-specific replacement economy laws | Baseline where a true economy replacement exists | Owner exposes its path and compatible final vanilla-equivalent position | No exhaustive installed inventory | Per-country adapter and full source review |
| Country-specific conscription systems | Baseline where applicable | Preserve population permissions and actual path | No exhaustive installed inventory | Per-owner population and law proof |
| Registered production-priority laws | I | Advance the owner's declared wartime branch | Required design, owner inventory absent | Real family definition, prerequisites, no sidegrade guessing |
| Registered manpower policies | I | Advance a true policy path without a duplicate manpower grant | Required design, owner inventory absent | Current-state and pool accounting evidence |
| Registered economic emergency policies | I | Advance existing institutions only | Required design, owner inventory absent | Owner effects, resource commitments, reversible state |
| Registered other wartime policies | II | Advance every declared compatible family once | Required design, owner inventory absent | Complete category list and justified wartime direction |
| Chaos Redux wartime authority systems | I or II, as justified by the owner | Preserve institutional prerequisites, no automatic weapon use | Shared mechanics mention systems, complete owners not inspected | Actual ordered policy source and bounded integration |
| MIO policies and specialization choices | None by default | Do not impose an invented rank on sidegrades | No compatible monotonic owner verified | Explicit owner wartime branch before participation |
| Military doctrines, technologies, advisors, and focus completion | Outside scope | No free selection, completion, or purchase | Fixed design boundary | Negative tests show no unintended changes |
| Country balances of power or political chambers | None by default | Only a genuine explicitly registered wartime sub-policy participates | No generic ordering verified | Exact subsystem adapter or explicit exclusion |
| True nonhuman population institutions | Owner-defined | Advance only actually used compatible families | Shared project distinction, actual owners not fully inspected | No human-law installation, duplicate population, or blanket tag exclusion |

“No exhaustive inventory” is an open compatibility task, not proof that no such systems exist. A negative repository search does not close that task.

## Canonical boundary rules

A category is visited once per firing regardless of how many profile labels or owner aliases refer to it. Resolve applicability, the old law, the proposed successor, and structural prerequisites from a consistent start-of-firing state. Apply the War Support gain before computing the effects of the resulting extreme laws.

A newly satisfied structural prerequisite caused by another category's step does not create a second cascading advance during the same firing. It can matter at the next firing.

Unknown positions are preserved. Missing institutions stay missing. Structural failure in one category does not cancel the country's remaining categories.

An old cap helper that awards Political Power is not the correct no-change provider. Event 82 needs a provider that returns the cap result without a replacement effect.

## Owner compatibility and identity checks

Audit exact `has_idea` checks that may mean “at least this mobilization level”. Do not blindly rewrite every exact-law condition. Record each affected owner and whether the condition is a threshold, an exact political choice, an initial state, or a forced reset.

Any external removal of an extreme law must remove its owned penalties. Any inheritance of an extreme law must install its current penalties. Neither operation replays the worldwide War Support grant.

Source-level category support is distinct from live consumer proof. The release matrix must record both.

## Price provider contract

The reversal action requires the real ordinary current adjacent-law price, including native law levels, ordinary category modifiers, active applicable cost sources, and ordinary rounding. It then doubles that resolved price.

The shared discounted-cost framework may be used only through a verified normal-price provider. Its existence does not prove that it can read every native law price automatically.

Do not feed an already discounted normal quote through the discount sources a second time. Do not replace unavailable native pricing with a hardcoded 300 PP action. Keep missing current-price access as an explicit blocker until an exact provider exists.
