# Reviewed global-survival chain: False Spring Losses

## Scope

False Spring Losses is a dormant Fallout-owned recovery chain for a state whose Air Winter thaw becomes visible before its first-frost marker has expired. It is not an ordinary super-event and it does not activate the Fallout scheduler.

The chain is defined by events `chaosx.fallout.478` through `.484` under `add_namespace = chaosx.fallout`. Candidate `478` uses transaction `710042` and route `7142`. Event Log history `9147` carries fifteen branch and callback payloads.

## Entry proof

The state must be owned by the requesting country, controlled by that country, and current in both the Fallout identity and durable resource ledgers. It must have a produced Air Winter snapshot from the current transition generation, a valid first-frost marker, and `air_winter_visual_thaw_is_eligible = yes`. The selector accepts only pastoral, rural, or town states with surviving population, adaptation at least `30`, exposure from `8` through `67`, reclamation below `90`, and a food reserve. Supply access must be absent or below `92`.

The candidate producer chooses the lowest valid owned state id and carries the pre-transition food reserve as scheduler pressure. The country row also requires campaign day `900` through `2999`, Food at least `10`, Medicine at least `5`, Cohesion at least `22`, and no committed chain or closed memory flag.

## Choice surface

The opening exposes four concrete responses with distinct costs and government preferences.

1. Replant before the ground closes spends Food and Medicine on covered beds and emergency crews.
2. Buy seed from the eastern convoy spends resources and records a bilateral debt in the chain's foreign-credit memory.
3. Open the underground reserve spends resources to move seed below an old rail tunnel and makes access a shared civic rule.
4. Accept the smaller harvest spends resources to protect households with the least shelter while agronomists preserve the frost record.

The human and hidden-AI lanes use the same branch constants, delayed transaction, outcome calculation, and cleanup receipts. AI preference checks are deterministic and fall through to an affordable policy without a second event family.

## Numerical and gameplay contract

The chain freezes Food, Medicine, Cohesion, Recognition, Adaptation, Reclamation, and frost-memory values before the result. Viability weights Food, Adaptation, Reclamation, frost memory, Cohesion, and Recognition. Each branch has separate cost and success or partial thresholds.

The result arrives after `35` days and updates Food, Medicine, Cohesion, stability, war support, seed reserve, frost memory, Air Winter adaptation, exposure, reclamation, and supply. Failure damages infrastructure or an industrial complex through the native building effect and requests population loss through the Deaths system. The result then schedules a `240` day second-sowing callback.

The callback applies a second branch-specific ledger update, a second-sowing state memory, a temporary dynamic modifier, and another Deaths-backed failure route. Cleanup releases the callback and result tickets in authenticated order, closes the memory, and clears the frozen registry fields.

## Text and asset contract

Player-facing text names the late frost, low terraces, eastern convoy, rail tunnel, outlying farms, and state ration line. It does not mention implementation history or tuning. The dedicated report image is `GFX_report_event_fallout_false_spring_losses` and is documented under `docs/assets/air_cleanliness_fallout/fallout_false_spring_losses/`.

## Deliberate boundary

This chain remains dormant because scheduler release receipts, reviewed producers, and activation setters are absent. The full-screen blackout and exact engine-native all-valid-province thermonuclear sweep belong to the completed consequence core.
