# Event 006 IW-013 NAV project lifecycle patch

Date: `2026-08-13`.

The NAV founding mission can enter the terminal `independence_wave_nav_compact_crisis_failed` state after timeout or failed cancellation. The eleven NAV project decisions now share `is_independence_wave_nav_project_ready`, which requires the active IW-013 package, completed package setup, and absence of that terminal failure flag.

Changed files:

- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`: added `is_independence_wave_nav_project_ready`.
- `common/decisions/006_independence_wave_iberian_decisions.txt`: applied the helper to every NAV project visibility and availability path, and to every timed-project cancellation path; the immediate sovereignty decision also requires the helper before it can be selected.

This closes the post-failure repair/retry path without inventing a recovery mechanic. It preserves the existing concrete costs, route locks, capital and host checks, completion effects, and cleanup. The founding mission remains independently responsible for setting the resolved or failed lifecycle flag.

Validation: the NAV slice contains 42 helper references (22 visible/available gates, 10 cancellation guards, and 10 cancellation-effect guards), no project visibility path still uses only the package predicate, and targeted `git diff --check` is clean apart from normal line-ending warnings. The central content-attestation and Join lists were not changed. A fresh mandatory `hoi4.probability_inspect` on the current Iberian mission source returned `PROBABILITY_SOURCE_INSPECTED`, with 22 candidates, 12 required inputs, zero inspect-unresolved items, and an incomplete empty fixture pool. Source revision `8dd98dec081093e0f501764f9d66226b700843775a45af386d4b02c2217d2fbb`, source hash `84a87d4bff8bbbac761ca65cc1a46de2a4e0a0ee25aebeadef84e1b68f67b657`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0b/artifact/8b1c405a77da043a0d6997fa712701cbeb751ce274933e31c916f5a8331dc10b/bffa198f099d70273477f97353d73bff0d50ec56710249a697354684fe2d8ac7/probability-inspect-84a87d4bff8b.json`. Typed scenario evaluation remains incomplete, so no balance claim is made.

Remaining design boundary: if a future design wants post-failure rehabilitation, it must add an explicit recovery decision or mission and separate localisation rather than reopening these projects implicitly.
