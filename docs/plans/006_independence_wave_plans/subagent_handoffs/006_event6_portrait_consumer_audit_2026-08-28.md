# Event 006 portrait consumer audit handoff — 2026-08-28

## Scope and disposition

This was a read-only audit of the supplied Event 006 portrait outputs against the current runtime consumers. No gameplay, GFX, character, DDS, archive, manifest, or localisation file was changed, and nothing was staged or committed by the audit.

The existing exact-consumer wiring remains authoritative. No additional portrait can be safely wired without changing an identity, role, rights, or package-admission gate.

## Evidence

- 110 supplied PNG/DDS pairs decode at `156x210`; each DDS is `131168` bytes, uses the required legacy BGRA layout, has opaque alpha, and matches its PNG pixels.
- 70 Event 006 runtime DDS files pass the same contract.
- 38 supplied DDS files are exact SHA-256 matches for stable runtime consumers across NAV, AXX, BAX, BBX, BOS, MNT, KOS, RUT, BSK, YAK, ARX, ASX, ASY, BAY, CHU, COR, DOX, GLC, MAC, RHI, SOK, and WLS.
- The current Event 006 GFX registry exposes 64 unique portrait sprite/texture pairs, all with existing paths and no duplicate names or textures.
- The Event 006 character registry resolves all 47 unique portrait references.

## State and gates

NAV Aguirre and GLC Castelao retain their previously accepted `styled_final` state. The other exact runtime matches remain `source_placeholder` or `styled_final_candidate` according to their existing provenance records; no replacement was promoted.

The remaining supplied candidates are intentionally unmapped because their identity, historical role, rights, framing, or live consumer is unresolved. This includes the alternate NAV crop, malformed or background-only Kosovo candidates, and the supplied DON candidate with no Event 006 consumer. The current Kosovo Shaban runtime DDS is unchanged.

No RunPod, ImageGen, game process, or runtime MCP check was used. The existing closure ledger in `006_event6_portrait_consumer_closure_2026-08-26.md` remains the detailed 38-row hash and consumer authority; this handoff records the 2026-08-28 revalidation and its no-edit disposition.

## Remaining blocker

Portrait evidence does not admit a package by itself. The eight adapter-only packages and the unresolved identity/rights packages remain fail-closed, and Event 006 remains **HOLD / PARTIAL**. No fallback portrait, relabelled person, or new consumer is authorized by this audit.
