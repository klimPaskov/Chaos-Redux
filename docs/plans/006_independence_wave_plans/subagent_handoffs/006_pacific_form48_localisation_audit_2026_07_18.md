# Event 006 Pacific / FORM-48 localisation audit

> **Parent follow-up (2026-07-18):** The six shared Event 006 decision/focus
> collisions recorded below were resolved after this audit by renaming only the
> three focus IDs and their focus localisation keys to the
> `independence_wave_focus_*` namespace. The decision and mission IDs remain
> unchanged. The remaining seventeen global duplicate groups are unrelated to
> Event 006.

Date: 2026-07-18
Scope: IW-173 HAW, IW-179 FSM, IW-184 HBX, FORM-48 Pacific Regional
Federation/PFX, the Pacific focus branch, Pacific decisions and missions,
ideas, characters, invitation and withhold surfaces, post-formation ledgers and
cycles, dissolution, Event Details/history, scripted localisation, and the
dangerous-milestone reason-4 wording.
Status: audit complete; five narrow player-facing wording fixes applied. No
readiness flag, country package attestation, portrait, flag, focus DDS, adviser
icon, sprite, or gameplay mechanic was changed.

## Files changed

- `localisation/english/006_independence_wave_pacific_l_english.yml`
  - `independence_wave_cost_pacific_island_strategic`
  - `independence_wave_form48_federal_compact_category_desc`
  - `independence_wave_form48_federal_coordination_desc`
  - `independence_wave_form48_commission_convoy_defense_rotation_desc`
  - `independence_wave_form48_allocate_shared_procurement_contracts_desc`
- This handoff only. No separate `006_independence_wave_form48_l_english.yml`
  exists; FORM-48 Pacific strings live in the Pacific package localisation
  file, while the shared formable registry name/method/cost strings live in
  `localisation/english/006_independence_wave_formable_registry_l_english.yml`.

## Changed keys and before/after behavior

### Pacific strategic project cost

`independence_wave_cost_pacific_island_strategic` previously said only that a
project required a stable government, public resolve, command attention,
manpower, and a convoy reserve. It now exposes the dynamic thresholds and the
payment distinction:

> Requires more than the configured Stability, War Support, Command Power,
> manpower, and convoy values; completion commits exactly those amounts.

The wording deliberately says “more than.” The independent Pacific helper
`can_pay_independence_wave_pacific_island_strategic_cost` uses strict `>` gates
against the actual displayed values (stability 0.10, war support 0.05, command
power 20, manpower 2500, and convoys 5), while
`independence_wave_pacific_pay_island_strategic_cost` deducts the exact negative
spend constants. This avoids implying that an equal balance passes the gate.

FORM-48 payer triggers are different: the completed decision audit uses the
availability-threshold constants (for example 19.9 command power, 19 convoys,
999 fuel, 499 infantry equipment, and 49 support equipment) so the exact
positive resource amounts shown by the existing `Commits ...` strings are
payable. Those FORM-48 cost strings were intentionally not changed to “more
than.”

### PFX identity in post-formation surfaces

PFX is a cosmetic identity on the HBX carrier, not a new country tag. The
post-formation category already rendered `[HBX.GetName]` as the carrier but then
said “California administers” in its explanatory paragraph. The paragraph now
uses `[HBX.GetName] administers`.

The post-formation coordination idea and carrier cycle 1/2 descriptions also
used “California” after PFX was active. They now use “The federal carrier,”
which remains correct before and after the cosmetic identity changes. The
dissolution description still names California because the effect explicitly
restores the carrier's national identity; that is an outcome, not stale PFX
branding. Invitation text still names California because invitations are issued
before formation by the HBX carrier.

## Required audit output

### Missing key list

None in the requested surface.

Mechanical coverage checks found:

- 208 quoted player-facing entries in the Pacific file and 120 quoted entries
  in the shared formable-registry file (the `l_english:` root is excluded from
  these counts).
- 137 distinct localisation references from the Pacific/FORM-48 decisions,
  categories, focus branch, ideas, and characters; all resolve in the complete
  English localisation set.
- Every Pacific focus title/description/tooltip, FORM-48 decision or mission
  name/description/tooltip/custom cost, Pacific idea, and package character
  name/description resolves.

### Duplicate key list

No duplicate key occurs inside either requested localisation file. A global
English scan found 23 duplicate key groups elsewhere; none is Pacific-specific:

- Shared Event 006 decision/focus collisions (parent-owned shared-surface
  cleanup):
  `independence_wave_build_permanent_foreign_service`,
  `independence_wave_build_permanent_foreign_service_desc`,
  `independence_wave_coordinate_reclamation_fronts`,
  `independence_wave_coordinate_reclamation_fronts_desc`,
  `independence_wave_discover_regional_identity`, and
  `independence_wave_discover_regional_identity_desc` are each defined in both
  `006_independence_wave_decisions_l_english.yml` and
  `006_independence_wave_focus_l_english.yml`.
- The remaining 17 duplicate groups belong to unrelated feature files
  (`brilliant_scientist_foreign_protection_effect_tt`, ICD, KRG, NRF, IKX, ILX,
  and ZIN surfaces) and were not touched.

### Scripted localisation issue list

None found in the requested Event 006 scripted-localisation family.

- `006_independence_wave_formable_registry_scripted_localisation.txt` has 63
  distinct `localisation_key` targets and no missing targets. Its Pacific
  branch resolves `independence_wave_formable_name_pacific_regional_federation`.
- `006_independence_wave_focus_scripted_localisation.txt` has 60 distinct
  targets and no missing targets. Its selectors are country-scoped and use
  accepted package metadata; no Pacific-specific branch is required.
- `006_independence_wave_scripted_localisation.txt` has 17 distinct targets and
  no missing targets.
- `[This.GetIndependenceWaveSelectedFormableName]` and
  `[This.GetIndependenceWaveFormableCommitCostText]` are used from the country
  formable decision surface. The Pacific category uses country-scoped
  `[HBX.GetName]` and `HBX` ledger variables consistently.

No raw scripted trigger text, unresolved scripted-localisation fallback, or
scope mismatch was found. The apparent `Get...` names returned by broad key
regexes are function names, not missing localisation keys.

### Dynamic text opportunities

- Fixed: Pacific strategic cost now shows dynamic thresholds and distinguishes
  strict `>` availability from exact completion payment.
- Fixed: post-formation category/idea/carrier-cycle identity is dynamic or
  identity-neutral under cosmetic PFX.
- Already present and verified: all five post-formation ledger values and the
  dissolution threshold are dynamic in the compact category; cycle durations
  and all carrier/member material costs use FORM-48 constants; invitation and
  member obligations expose command-power/convoy/equipment costs.
- No additional safe dynamic branch is needed for the dangerous super-event:
  the approved reason-neutral text intentionally covers all five qualifying
  trigger families, including hidden-formable reason 4.

### Cross-surface mismatch notes

- The source plan and package documentation describe HBX as California before
  formation and PFX as a cosmetic Pacific Regional Federation identity after
  commit. The edited player-facing post-formation strings now follow that
  lifecycle; dissolution retains the explicit “restore California” outcome.
- Invitation acceptance/withhold text correctly keeps Hawai'i and Micronesia
  sovereign and explicitly denies annexation/full integration. Withholding
  says the founding proposal cannot form through that consent record.
- Carrier/member cycle descriptions, deadline descriptions, withhold text, and
  dissolution text describe material commitments, deadlines, autonomy/capacity
  tradeoffs, and cleanup consequences. No static timer or ledger value was
  found where a dynamic constant is already available.
- `Hawai'i` with an ASCII apostrophe is used consistently in the requested
  English strings and matching package documentation. No mixed `Hawaii`, curly
  apostrophe, or Unicode `Hawaiʻi` player-facing variant occurs in this surface.
  `Micronesia`, `FSM`, `HBX`, `HAW`, and `PFX` names resolve consistently.
- Event Details/history has no Pacific-specific extra surface. The shared Event
  006 history selector routes payload 6002 to
  `independence_wave.history.danger_milestone.title/description`, both present
  in `006_independence_wave_super_event_l_english.yml`; normal Event 6 entries
  use the generic Event Details key. No FORM-48/Pacific EventLog key is missing.

### Dangerous super-event reason 4

Reason 4 (`hidden_formable_bloc_center`) is selected in gameplay by the FORM-48
post-formation effect and sent through the existing one-shot super-event FIFO.
The player-facing title/description/button/quote remain the approved
route-neutral “Every Border a Casus Belli” package. The approved research notes
explicitly require route-neutral wording for the offensive league, high-chaos
wave, synchronized wars, hidden aggressive formable, and sponsorship-cascade
families. No separate reason-4 localisation key is expected or missing.

### File encoding concerns

Both requested localisation files begin with UTF-8 BOM bytes `EF BB BF`.
The Pacific file remains LF-only (228 LF, 0 CR); the registry file remains
LF-only (129 LF, 0 CR). LF-only line endings are not an encoding failure for
HOI4, and no BOM was lost during the patch.

## Validation performed

- Re-ran key-count, duplicate, and source-reference coverage checks after the
  wording edits.
- Re-ran scripted-localisation target extraction for registry, focus, and
  shared Event 006 selectors.
- Compared the strict Pacific strategic helper and exact payment effect against
  the new cost wording; separately checked FORM-48 availability-threshold
  triggers against their existing exact `Commits ...` strings.
- Inspected Event 006 history localisation dispatch and FORM-48 category,
  mission, cycle, withhold, and dissolve surfaces.

Skipped meaningful validation:

- No runtime GUI/event render was available or needed for these text-only edits;
  the HOI4 MCP decision-inspect path was previously blocked by artifact-storage
  limits in the parent FORM-48 handoff. No claim of runtime FORM-48 readiness
  or package attestation is made here.

## Assets, readiness, and unresolved wording decisions

- No adviser icon, adviser portrait, focus icon, flag, sprite, DDS, `.gfx`, or
  portrait file was added, referenced, or changed. The package characters'
  existing comments and docs continue to state that they have no adviser role
  or adviser portrait.
- No IW-173/IW-179/IW-184 attestation or FORM-48 readiness flag was promoted.
- No gameplay mechanic, cost constant, trigger, effect, focus, decision, idea,
  character, or event-log registration was changed.
- Wording decision resolved: “The federal carrier” is used for PFX-era idea and
  cycle descriptions, while `[HBX.GetName]` is used where the category already
  exposes the dynamic carrier name. California remains only where it denotes
  the pre-formation carrier or the explicit post-dissolution restored identity.

No broader localisation plan handoff was written; the shared duplicate groups
listed above remain parent-owned and out of this narrow Pacific/Form-48 patch.
