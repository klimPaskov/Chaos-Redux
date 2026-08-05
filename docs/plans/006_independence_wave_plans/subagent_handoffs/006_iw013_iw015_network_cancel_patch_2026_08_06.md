# Event 006 Iberian Network mission cancellation patch

Date: 2026-08-06

Scope: narrow parent-owned correction following the current IW-013/IW-015 decision and mission audit.

The NAV and GLC `open_iberian_network` projects already required Network membership and displayed only while the League route was available. Their cancellation predicates did not repeat the League-route requirement, so an active project could survive a route withdrawal and complete after the route was no longer valid.

`common/decisions/006_independence_wave_iberian_decisions.txt` now cancels both projects when `independence_wave_league_route_available` is absent, in addition to the existing package, membership, and capital-control guards. The change preserves the paid diplomatic cost, project failure effect, and route-specific completion effects.

This patch does not promote NAV or GLC to central content attestation. The country-package, source/identity, flag, portrait-consumer, command-roster, and independent probability gates remain fail-closed. No advisor icon was created.

Validation: the two project blocks were re-read after patching; both contain the new League-route cancellation guard and retain the existing custom-cost and failure-effect wiring. Fresh MCP source inspections of the edited file completed with zero diagnostics: `decision_ai_will_do` found 2 candidates and 9 required inputs (`probability-inspect-32a71a8f91b4.json`, source hash `32a71a8f91b4e65ee386b18f93fe45498d7ecef941485f378880888945a3fe9d`), and `mission_ai_will_do` found 22 candidates and 12 required inputs from the same source revision. Both pools remain runtime-dependent and are not treated as probability or live-AI proof.
