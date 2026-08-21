# Event 006 dormant-carrier capital-scope regression guard — 2026-08-21

The Banat, Thrace, and Epirus package availability triggers now use their fixed anchor states (82, 184, and 185) with explicit former-host ownership checks. They do not call `capital_scope`, because AXX, BAX, and BBX are dormant carrier shells and intentionally have no valid capital before release.

The allocator audit now asserts this contract for all three package trigger files. It rejects any future reintroduction of `capital_scope`, verifies the fixed anchor state, and verifies the expected ROM/GRE host-owner proof. This directly guards the runtime error class that reported invalid `capital_scope` targets for AXX, BAX, and BBX and could suppress the candidate pool before allocation.

This is a source regression guard only. It does not add a decision, mission, category, cost, queue, pressure, or pre-event surface, and it does not promote any package.

Validation: `.tools/audit_event6_allocator.py` passes with the 20-package static witness and the existing retired-crisis assertions.
