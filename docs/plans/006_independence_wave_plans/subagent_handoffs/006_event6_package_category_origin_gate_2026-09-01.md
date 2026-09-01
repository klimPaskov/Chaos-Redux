# Event 006 package-category origin gate handoff

Date: 2026-09-01

## Scope

The consolidated Event 006 decision-category registry now requires `is_independence_wave_active_country = yes` in every package-specific category visibility block.

The gate covers 47 package-category blocks, including the fixed-package categories for the Western, Iberian, Balkan, Mediterranean, Pacific, Siberian, Caucasus, frontier, and first-footprint packages, plus the IW-043/IW-058 and IW-093/IW-098 signature categories.

## Reason

Event 021 has a bounded adapter window in which `is_independence_wave_package_content_active` may be true while the Event 006 active-origin marker is deliberately absent.

Package predicates remain adapter-aware so the existing setup transaction can consume package-local leaders, focuses, forces, and identity checks, but category visibility must not expose Event 006 decisions during that preparation or after an origin-neutral adapter receipt.

The added active-origin requirement therefore makes the player-facing category boundary match the Event 006 lifecycle without changing adapter setup or package execution predicates.

## Changed surface

- `common/decisions/categories/006_independence_wave_categories.txt`

No decision costs, missions, queues, pressure variables, release logic, package setup effects, or Event 021 adapter flags were changed by this tranche.

## Evidence

A static category-block scan found no package-specific visibility block lacking the active-origin gate after the edit.

The existing focused Event 006 validators remain the acceptance checks for allocator, country API, flags, FORM-16, SCN-008, and GUI semantic coverage.

Runtime HOI4 rendering and save/load proof remain the user's live-validation boundary; this handoff does not claim engine execution evidence.

## Risks and follow-up

The central recognition, patron, border, formable, and overlay categories retain their existing phase or runtime gates because they do not directly use the adapter-aware package predicate in this registry.

If a later package intentionally needs an Event 021-only player-facing surface, it must receive an explicitly named adapter category rather than weakening this Event 006 origin gate.
