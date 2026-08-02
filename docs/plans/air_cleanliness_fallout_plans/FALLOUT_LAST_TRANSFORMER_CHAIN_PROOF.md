# Fallout Last Transformer chain proof

Status: implemented as a dormant reviewed pilot. It is not release-floor
credit because the Fallout scheduler has no activation setter or caller.
Hearts of Iron IV was not launched, as requested. This document records
static source evidence and the engine-sensitive limits that remain open.

## Identity and ownership

| Surface | Identity |
| --- | --- |
| Namespace | `chaosx.fallout` |
| Human opening | `chaosx.fallout.243` |
| Hidden AI opening | `chaosx.fallout.244` |
| Human results | `245` industry, `246` hospital, `247` microgrid, `248` neighbour |
| Hidden AI results | `249` through `252` in the same branch order |
| Human callback | `chaosx.fallout.253` |
| Hidden AI callback | `chaosx.fallout.254` |
| Cleanup | `chaosx.fallout.255` |
| Candidate | `243` |
| Transaction key | `710011` |
| Route | `7111` |
| Event Log history | `9116` |

The event ids are appended after the Door List range `230` through `242`.
No Zombie id, file, asset, audio, sprite, or path is used. The candidate row
is owned by the Fallout candidate producer and is not installed by a generic
world-end owner.

## Candidate and target proof

`fallout_event_pilot_last_transformer_state_is_current` authenticates the
current Fallout timeline phase, the current owner resource row, the durable
state identity row, the durable state resource row, the current Supply Access
row, the produced Air Winter snapshot, population above the minimum, exposure
above `20`, reclamation above `15`, operational infrastructure, and an
operational civilian or military factory. It rejects a prior Last Transformer
chain, every durable branch memory, and a committed state registry.

`fallout_event_candidate_effects.txt` selects a state with the following
priority:

`infrastructure * 4 + industry * 3 + airbase + dockyard`

The producer clamps that priority from `0` through `100` and uses the lowest
state id as the stable tie break. The target country must still own the state
when the opening receipt is checked.

The candidate row carries frozen Power as its mechanic pressure, the target
state's frozen Exposure as severity, and the clamped target priority as state
value. The state id is retained as the source for both target values.

For the neighbour branch, `fallout_event_243_select_partner` scans only AI
neighbours that are not at war, have current identity and resource rows, have
Power at least `25`, and own a state with reclamation at least `20`. It reads
the highest reclamation among the partner's owned states, scores the partner
as `Power + highest reclamation`, and breaks ties with the lowest country id.
The selected partner id, Power, and reclamation are frozen on the requesting
country. The partner receives no mutation.

## Transaction sequence

1. The ordinary event receipt and target are checked again at opening. The
   human event only accepts the human-visible mode. The AI event only accepts
   hidden AI mode.
2. `fallout_event_243_calculate_all_branch_scores` loads every input before
   branch calculation. It freezes Power, Medicine, Scrap, Recognition,
   Cohesion, exposure, reclamation, shelter, Supply Access, building levels,
   population, partner values, selected building type, base viability, all
   branch scores, and all projected outcome bands.
3. The base viability is calculated from the approved weighted contract,
   rounded once, and clamped from `0` through `100`. Branch bonuses and
   success or partial thresholds are held in
   `common/script_constants/fallout_world_end_event_constants.txt`.
4. A delayed result row is requested before payment. The result is due at
   exactly ten days. The visible event budget cost is `3`. Payment and the
   optional factory removal occur only after the delayed row and ordinary
   receipt consume successfully.
5. Human and hidden AI result events use the same result effect and the same
   frozen branch outcome. The failure path records population loss through the
   accepted exact state population loss contract and then records the applied
   count through the shared Deaths effect. Only industry and microgrid failure
   can damage one repairable infrastructure level. Hospital and neighbour
   failure do not damage a building.
6. The callback row is requested only after a successful result resolution. It
   is due at exactly 120 days after the result. The callback applies the
   branch outcome's delayed Supply Access and reclamation memory, writes a
   transient institution receipt, and prepares authenticated cleanup.
7. Cleanup releases the result and callback receipts, clears the transaction
   registry and transient state pointer, clears payment and callback flags,
   and preserves the durable country memory that records the selected branch
   and outcome.

## Branch contract

| Branch | Cost | Success | Partial | Failure |
| --- | --- | --- | --- | --- |
| Industrial line | Power `2`, remove one operational factory | Power `+12`, Scrap `+5`, Supply `+4`, Reclamation `+3` | Power `+7`, Scrap `+3`, Recognition `-2`, Supply `+1` | Power `+2`, Scrap `+1`, Supply `-5`, Exposure `+3`, Reclamation `-3`, Deaths `0.04%`, one infrastructure level |
| Clinic circuit | Power `5`, Medicine `4` | Recognition `+6`, Shelter `+2`, Supply `+2` | Recognition `+2`, Shelter `+1`, Supply `-1` | Medicine `-2`, Recognition `-5`, Supply `-5`, Exposure `+2`, Deaths `0.06%` |
| Feeder districts | Power `4`, Scrap `6` | Power `+8`, Recognition `+3`, Supply `+6`, Reclamation `+6`, Shelter `+2` | Power `+4`, Recognition `+1`, Supply `+2`, Reclamation `+2` | Supply `-6`, Reclamation `-4`, Exposure `+4`, Deaths `0.03%`, one infrastructure level |
| Neighbour technicians | Power `3`, Recognition `4` | Power `+9`, Recognition `+2`, Supply `+4`, Reclamation `+4` | Power `+5`, Recognition `-2`, Supply `+1` | Recognition `-5`, Supply `-3`, Deaths `0.02%` |

The failure percentages are fractions of the frozen state civilian
population. The shared loss effect enforces the minimum remaining population
and records no second casualty source. Callback deltas are success Supply
`+2` and reclamation `+2`, partial Supply `0`, and failure Supply `-3` with
reclamation `-1`.

The frozen base formula is `30% Power + 20% Supply Access + 15%
infrastructure score + 10% industry score + 10% Reclamation + 5% Shelter +
5% Recognition + 5% Medicine - 20% Exposure - 10% auxiliary load`.

## AI and cleanup proof

The AI starts with the same projected branch outcomes as the human route and
adds deterministic weights for Power pressure, exposure, war, one-factory
states, dockyards, Recognition, government archetype, and prior branch
memory. It chooses in strict order industry, hospital, microgrid, neighbour
when scores tie. A neighbour score is invalid when no eligible partner was
frozen. Hidden AI results and callbacks use separate event tokens but share
the same effects, result row, callback timing, history payloads, and cleanup
receipts.

The Event Log writer is idempotent per result or callback history flag. The
payloads are `11` through `43` for branch outcomes and `51` through `53` for
the callback outcomes. The global log name and detail mappings use history
`9116` and the dedicated scripted localisation function. A frozen neighbour
partner is written as the secondary actor for the bilateral branch.

## Dedicated asset proof

The fictional report image is owned by Fallout and uses no Zombie surface.
The final runtime asset is
`gfx/event_pictures/fallout/report_event_fallout_last_transformer.dds`
with sprite `GFX_report_event_fallout_last_transformer` registered in
`interface/fallout_world_end.gfx`. The source, processed image, contact sheet,
prompt, manifest, and hashes are in
`docs/assets/air_cleanliness_fallout/fallout_last_transformer/`. The DDS is a
210 by 176 uncompressed 32-bit BGRA texture. No production fallback was used.

## Engine-sensitive limits

- The candidate producer and its live scheduler activation are still
  intentionally dormant. Static code cannot prove that an uncalled candidate
  will be reached in a human campaign.
- The installed documentation does not expose a literal multiplayer lobby
  host predicate. The chain is receipt and owner authenticated, but that is
  not a host-authority proof.
- The partner's stable country id, Power, and highest reclamation are frozen.
  The result text does not reread a mutable partner name because the native
  script surface does not provide a safe country-scoped persistent string
  receipt for concurrent delayed chains. A global event target would collide
  between countries, so it is not used.
- State scope lookup, stable country-id tie order, dynamic modifier display,
  delayed-row save recovery, callback timing, and Deaths readback are static
  source proofs only until an authorized runtime pass exists.
- General Fallout successor allocation, player continuation, focus package
  producers, and the full 660-block review floor remain outside this pilot.

No fallback or placeholder was introduced. The open limits are reported as
blockers rather than treated as completion evidence.
