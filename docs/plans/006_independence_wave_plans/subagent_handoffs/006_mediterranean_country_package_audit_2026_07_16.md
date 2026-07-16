# Event 006 Mediterranean country-package audit

Date: 2026-07-16
Auditor role: `chaosx_country_package_auditor`
Scope: `IW-017` / `COR`, `IW-018` / `ARX`, `IW-019` / `ASX`, and their `FORM-05` linkage only

## Verdict

**PASS for parent-controlled exact admission.** The three Mediterranean country
packages and the sovereign `FORM-05` charter league are implementation-complete
within the audited surface after the two narrow trigger corrections recorded
below. No P0, P1, or P2 package finding remains.

This verdict authorizes only exact-row promotion for `IW-017`/`COR`,
`IW-018`/`ARX`, and `IW-019`/`ASX`, with the existing `FORM-05` dependency. It
does not authorize a generic tag fallback, another region-02 package, global
SCN-008 coverage, or an Event 006 completion claim. Admission, shared capacity,
dispatch, and scenario registries were deliberately not edited by this audit.

## Narrow corrections made

### Prepared focus-tree proofs

In
`common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`:

- `has_prepared_independence_wave_iw_018_package_setup` now requires
  `has_focus_tree = independence_wave_focus_tree`;
- `has_prepared_independence_wave_iw_019_package_setup` now requires the same
  exact tree.

`IW-017` already had this proof. The three packages can no longer report setup
success if their full-framework tree assignment fails or becomes a no-op.

### Stable FORM-05 carrier lifecycle

In `common/scripted_triggers/006_independence_wave_form05_triggers.txt`:

- `is_independence_wave_form05_prospective_carrier` now requires
  `independence_wave_origin_committed`;
- `is_independence_wave_form05_eligible_carrier` now requires
  `independence_wave_origin_committed`.

The former gate, `independence_wave_origin_activation_ready`, is transactional:
the shared commit effect clears it before setting
`independence_wave_origin_committed`. Requiring the stable committed flag makes
the post-release charter reachable without weakening setup validation. The
carrier remains fail-closed to non-Event-006 countries because it must also be
an active Event 006 country and match one of the exact package/tag/anchor triples
`IW-017`/`COR`/state 1, `IW-018`/`ARX`/state 114, or
`IW-019`/`ASX`/state 115.

## Binding, identity, history, and host proof

| Package | Identity | Anchor / group | Former host witness | Depth |
|---|---|---|---|---|
| `IW-017` | vanilla `COR`, Corsica | state 1 / `RG-1` | `FRA`, protected capital state 16 | Level 1 |
| `IW-018` | dormant `ARX`, Sardinia | state 114 / `RG-114` | `ITA`, protected capital state 2 | Level 1 |
| `IW-019` | dormant `ASX`, Sicily | state 115 / `RG-115` | `ITA`, protected capital state 2 | Level 2 |

- `COR` is reused rather than redefined. Setup accepts it only while its current
  tree is exactly `generic_focus`; any meaningful external COR tree causes
  setup to fail before mutation. Cleanup restores `generic_focus` only if COR
  still has `independence_wave_focus_tree`, so a later external tree is not
  overwritten.
- `ARX` and `ASX` are distinct Event 006 X-ending tags. The 2026-07-16 installed
  tag audit reports no collision for either tag across vanilla and the installed
  mod set. Their history shells provide baseline economy/trade/conscription and
  the exact guarded roster, while runtime setup owns territory, politics,
  technology inheritance, forces, and package readiness.
- Planning reserves only the exact anchor. The shared allocator protects one
  living host state first and revalidates host survival, frozen ownership,
  reservation group, tag availability, and anchor ownership/control before
  release.
- Event 5 separation is explicit at candidate, setup-input, and runtime
  preflight layers through the Soviet-collapse origin flag/variable exclusions,
  the joint reservation arrays, and the synchronized allocator order. These
  tags and anchors are not Event 5 opening republic identities or opening Soviet
  core anchors.

## Country-package completeness

### Characters, laws, forces, and public values

- The tranche has fourteen exact characters: four COR, five ARX, and five ASX.
  All accepted personal portraits are male. Each country has its political
  leadership, one corps commander, and two recruitable advisers with role,
  trait, cost, and AI selection logic.
- Advisers have no custom portrait or icon consumers. The three dual-role
  commanders use the supported large civilian/army portrait contract only;
  there are no small portrait slots.
- COR character recruitment is guarded and cleanup retires all four characters,
  supporting safe re-release. ARX and ASX use their dormant history rosters and
  do not duplicate them during runtime setup.
- All three packages prove `civilian_economy`, `export_focus`, and
  `volunteer_only`, exact command roster, and exact force generation before
  setup can pass.
- Force rows resolve exactly to COR coastal-maritime/tradition 53, ARX
  coastal-maritime/tradition 52, and ASX regular-defectors/tradition 65. The
  mapping controls templates, divisions, stockpiles, inheritance, and
  reinforcement behavior; final proof requires the current-generation package
  and `independence_wave_force_package_applied`.
- COR and ARX each have six package ideas; ASX has seven. Crisis and mature
  lifecycle ideas replace one another, route ideas are mutually exclusive, and
  visible country values clamp to the shared 0-100 public range with centralized
  thresholds and deltas.

### Focuses, routes, diplomacy, ambition, AI, and incidents

- ARX has six connected package focuses and ASX has eight. COR's five shared
  focuses are explicitly attached to the full Event 006 tree. All three expose
  their accepted constitutional, traditional, military, labor/patron variants,
  with excluded shared routes proven absent.
- Host negotiation, guarded-frontier, association, and reclamation lanes are
  registered. French/Italian property settlements use the stored former-host
  scope; patron and sponsor behavior remains in the shared diplomatic system.
- Each package registers its internal power struggle, Mediterranean island
  ambition, network/league lane, and exact `FORM-05` family readiness. ASX also
  supplies the mutually exclusive Two Sicilies and Mediterranean-republic
  dossier; only the latter grants the FORM-05 carrier mandate. ASX's separate
  mainland claims are removed during package cleanup.
- Seventeen exact country AI strategies cover founding restraint, survival,
  construction, equipment, route, host threat, maritime policy, the ASX Level 2
  dossier, and post-formation FORM-05 behavior. Severe host threat increases
  defensive and charter-recovery priorities without creating an unrequested war.
- Events `chaosx.nr6.21` through `.27` are the three founding incidents, three
  route incidents, and the ASX ambition incident. Events `.28` through `.34`
  cover the FORM-05 charter, congress seat, proclamation, failure/recovery, and
  first maritime board. All fourteen event definitions are unique and gated by
  exact scheduled/unresolved state.

## FORM-05 sovereign-charter proof

- The readiness loader selects only
  `constant:independence_wave_formable_family.mediterranean_island_league` and
  attests the exact FORM-05 territory, X-tag, flag, identity, integration, and
  member-policy surfaces. The minimum carrier/member/consent/anchor counts are
  all two.
- Carrier identity is restricted to the three exact audited package rows.
  Candidate members must be independent, active Event 006 origins with the same
  selected family, a live owned/controlled anchor port, bilateral maritime
  diplomacy, and no war with the carrier.
- Formation uses only `set_cosmetic_tag = MIX`, keeps every member sovereign,
  and records autonomous membership. A targeted scan found no annexation,
  subject creation, autonomy change, state transfer, core change, controller
  change, or capital move in the FORM-05 source set.
- Shipping, coastal-warning, customs-clearinghouse, defense, and first-board
  ratification provide the post-formation lifecycle. Cleanup removes its
  missions, decisions, ideas, invitations, variables, country/global locks, and
  the MIX cosmetic identity from the carrier.

## Cleanup and rollback evidence

- All 87 COR/ARX/ASX package flags set by the package effects, decisions,
  focuses, and incidents have exact cleanup partners.
- All 29 Mediterranean decisions/missions have matching cleanup removals.
- Route and lifecycle ideas, public variables, family selection, incidents,
  claims, AI markers, and package completion state are removed before the shared
  provenance reset.
- FORM-05 cleanup covers all 16 of its decision/mission surfaces and all timed
  recovery/global-lock state. The shared transaction rolls back a package if
  prepared proof, activation proof, array alignment, or final proof fails.

## Visual and localisation integration observed

The parent-owned portrait registration landed during this audit as
`interface/006_independence_wave_mediterranean_portraits.gfx`. Read-only linkage
checking found eight unique large portrait consumers, eight exact sprite
definitions, and eight existing DDS paths; no small or adviser sprite was
introduced. The package and FORM-05 gameplay/icon/flag asset handoffs report the
dedicated focus, decision, idea, report, portrait, ARX/ASX flag, and MIX identity
files finalized and wired. The localisation handoff reports complete mechanical
coverage with UTF-8 BOM files and adviser text that does not imply custom art.
Those parent/asset-owner files were not modified by this audit.

## Parent-owned exact admission work

The regional planners, setup/final-validation dispatch calls, cleanup dispatch,
and package implementation are present. Runtime remains intentionally
fail-closed because the shared admission trigger currently lists only the prior
audited set. The parent promotion should add exact immutable entries for all
three rows to the runtime adapter/content-attestation/preflight and SCN-008
preflight surfaces, together with the parent-owned capacity witnesses and exact
tag-availability predicates. No broad region-02 admission is authorized.

## Files changed by this audit

1. `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`
2. `common/scripted_triggers/006_independence_wave_form05_triggers.txt`
3. `docs/plans/006_independence_wave_plans/subagent_handoffs/006_mediterranean_country_package_audit_2026_07_16.md`

No commit was created.

## Simplifications, omissions, and blockers

No gameplay fallback, placeholder route, generic country substitute, force
simplification, missing AI profile, missing incident, sovereignty-changing
FORM-05 shortcut, adviser icon, or small commander dossier was accepted.

There is no remaining package blocker to exact parent-controlled admission.
The only outstanding action is the intentionally parent-owned exact registry
promotion described above; other Event 006 packages and global completion are
outside this verdict.

## References and skills used

The audit applied `chaos-redux-events`, `chaos-redux-subagents`,
`hoi4-focus-trees`, and `hoi4-decisions-missions`. It also consulted the required
offline wiki pages, official vanilla documentation, vanilla COR/history/focus/
character/AI precedents, and all accepted Event 006 specification parts. No web
Paradox wiki was used. No skill was created or updated.
