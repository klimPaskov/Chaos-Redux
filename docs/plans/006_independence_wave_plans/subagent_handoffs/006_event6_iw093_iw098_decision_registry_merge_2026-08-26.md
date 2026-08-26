# Event 006 IW-093/IW-098 decision-registry merge — 2026-08-26

## Scope

This bounded source-layout tranche reduces one Event 006 scripted-effect parser
file without changing the Asante or Sokoto decision contract. The source file
was a pure scripted-effect registry with no outer container and no duplicate
public effect identifiers in the canonical decision registry.

## Changes

- Appended the exact body of `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt` to `common/scripted_effects/006_independence_wave_decision_effects.txt` under the marker `MERGED SOURCE: common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt`.
- Removed the standalone parser file after the body comparison.
- Kept `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.md` as the scoped package documentation surface and changed it to point to the canonical registry.
- Added the source-layout note to `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`.

## Preserved identifiers and behavior

The merge retains all 24 public IW-093/IW-098 effect identifiers, including
paid transaction open/close helpers, project resolvers, host negotiation and
settlement effects, ratification, and cleanup. No decision, trigger, cost,
localisation, package-admission, formable, event, or runtime behavior was
changed.

## Validation

- The 765-line source body was compared against the appended section after line-ending normalization.
- The source exposes 24 public effect definitions, while the canonical registry had 46 before insertion, with no duplicate public names.
- Repository search found no active gameplay reference to the deleted parser filename. Historical handoffs may still name the former path and remain dated traceability.
- This was a source-layout-only change. No live game, save/load, or runtime completion claim is made.

## Follow-up

The package remains under the current IW-093/IW-098 admission and whole-event
HOLD/PARTIAL boundary. Future changes to these helpers should edit the
canonical decision registry and retain this package markdown as documentation.
