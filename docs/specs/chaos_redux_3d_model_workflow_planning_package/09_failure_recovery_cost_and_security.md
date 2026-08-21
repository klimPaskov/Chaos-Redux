# Failure Recovery, Cost, and Security

## Failure taxonomy

| Code | Failure | Normal response |
| --- | --- | --- |
| `REF_AMBIGUOUS` | Reference hides or confuses geometry | Revise reference or ask for review |
| `REF_RIGHTS` | Provenance or use rights unresolved | Block |
| `GEN_IDENTITY` | Candidate does not match the subject | Regenerate within budget |
| `GEN_FLOATING` | Critical floating or disconnected geometry | Regenerate unless local repair is clearly bounded |
| `GEN_FUSED` | Limbs, weapons, turrets, or wings fused | Regenerate or revise reference |
| `GEN_THIN_LOSS` | Barrel, mast, antenna, leg, or edge lost | Higher-detail route or local reconstruction review |
| `GEN_REAR_HALLUCINATION` | Unseen side is unacceptable | Regenerate, revise reference, or manual review |
| `TEX_FAILURE` | Texture style, seams, or baked light unacceptable | Retexture after geometry approval or repair in Blender |
| `RIG_UNSUPPORTED` | Provider cannot rig the asset class | Blender custom rig |
| `RIG_DEFORM` | Weights or hierarchy deform badly | Reweight, retarget, or rebuild rig |
| `ANIM_MISSING` | Required action unavailable | Author in Blender, do not substitute static |
| `ANIM_LOOP` | Loop or root motion fails | Clean and rebake |
| `EXPORT_EXTENSION` | `io_pdx_mesh` missing or incompatible | Repair managed dependency, block export |
| `EXPORT_FAILURE` | Exporter error or invalid output | Return to Blender checkpoint and diagnose |
| `RUNTIME_MATERIAL` | Texture or shader fails in game | Return to material stage |
| `RUNTIME_ACTION` | Wrong or broken action in game | Return to action or entity mapping |
| `RUNTIME_SCALE` | Wrong map scale or pivot | Return to normalization and re-export |
| `SECURITY` | Secret, path, listener, or arbitrary-code violation | Stop all automation and remediate |
| `BUDGET` | Job or account credit ceiling reached | Parent decision required |

## Recovery ladder

Use the least destructive valid response:

1. retry status or download without creating a paid task
2. retry transient provider call with backoff
3. perform bounded Blender repair
4. submit another paid generation within the approved attempt budget
5. create an approved derived reference
6. perform substantial manual modeling after scope approval
7. stop and block

The ladder is not mandatory order when the cause is already known. For example, a rights failure blocks immediately.

## Free-retry claims

The tutorial describes a free retry in the Meshy web interface. The API workflow must not assume that an API retry is free. Record actual `consumed_credits` for every task and use the live billing rules.

## Current API credit snapshot

Snapshot date: 2026-07-22. Recheck before implementation.

| Operation | Planning cost |
| --- | ---: |
| Image-to-3D, smart topology, no texture | 5 |
| Image-to-3D, smart topology, textured | 15 |
| Image-to-3D, Meshy 7, no texture | 20 |
| Image-to-3D, Meshy 7, textured | 30 |
| Retexture | 10 |
| Remesh | 5 |
| Convert | 1 |
| Resize | 1 |
| Auto-rig | 5 |
| Animation per action | 3 |
| UV unwrap | Not listed in the reviewed pricing table. Require a live unit cost or actual `consumed_credits` |

Example planning totals:

```text
smart-topology textured humanoid + rig + 3 actions = 29 credits
Meshy 7 textured humanoid + rig + 3 actions = 44 credits
smart-topology textured static prop + remesh = 20 credits
```

These examples exclude retries and optional retexture.

## Budget policy

Each job defines:

- `credit_soft_limit`
- `credit_hard_limit`
- `paid_generation_attempt_limit`
- `paid_postprocess_attempt_limit`
- `animation_action_limit`

Behavior:

- estimated cost above soft limit requires warning and reviewer acknowledgement
- no call may exceed the remaining hard limit
- actual consumed credits update the ledger immediately
- failed tasks record zero or charged credits from the provider response, not an assumption
- parent approval is required to raise the hard limit

## Cost estimator

`tools/estimate_meshy_credits.py` supports:

- model family
- texture state
- remesh count
- retexture count
- rig count
- action count
- retry scenarios

Its output is an estimate and includes the pricing snapshot date.

## Rate limits and queue handling

Provider rate and queue limits are account-specific. The orchestrator stores the current discovered limits when available.

On 429:

- honor `Retry-After` when present
- apply exponential backoff with jitter
- do not create a new attempt record for a request the provider did not accept
- stop after the configured transient retry ceiling

Do not parallelize paid work simply because the MCP can submit it.

## Asset retention risk

The current provider documentation states that API assets for non-Enterprise accounts have a limited retention period. The package therefore requires immediate local capture and does not rely on provider storage as an archive.

A task is not `generation_approved` until local files open successfully and have checksums.

## Blender security incidents

Stop and invalidate the active job when:

- Blender MCP listens beyond loopback
- free-form Python reaches the production backend
- a script accesses a path outside the job and approved read-only roots
- a downloaded `.blend` runs unreviewed embedded code
- an extension checksum differs from the lock
- the adapter invokes an unapproved shell command
- credentials appear in a log

Response:

1. stop servers
2. preserve logs without redistributing secrets
3. rotate exposed credentials
4. compare changed files against the job boundary
5. restore the last trusted checkpoint
6. update the incident and dependency records
7. rerun environment verification before resuming

## Supply-chain recovery

When an extension or MCP update is needed:

- install into a new isolated profile
- run the complete smoke and pilot tests
- compare output checksums and reports where deterministic
- keep the old profile until the new one passes
- promote by changing the dependency lock
- document removal or rollback commands

Never update a production Blender profile in place during an active asset job.

## No silent fallback examples

Forbidden:

- use a static model because attack animation failed
- keep a provider mesh far above the tested budget because remesh was difficult
- remove a required turret to simplify rigging
- omit normal/specular textures because PDX mapping was unclear
- use a different Blender MCP backend without documenting it
- call a web-app retry free in the API budget
- mark export complete without an in-game check

Required response is to fix, revise scope with the user, or block.
