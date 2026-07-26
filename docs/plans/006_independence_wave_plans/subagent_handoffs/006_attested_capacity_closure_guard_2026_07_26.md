# Event 006 attested-capacity closure guard

Status: **implemented static guard; exact-ten runtime band remains intentionally fail-closed**.

The accepted v10 improvement-loop closure forbids manufacturing a tenth compatible reservation group by rebinding Rhineland and Saar. The current content-attestation set is therefore expected to contain ten packages, ten unique mandatory anchors, and nine compatible reservation groups because IW-008 RHI and IW-010 AJX both use `RG-RHINE-SAAR`.

`.tools/audit_event6_allocator.py` now reads the canonical content-attestation OR block and the current package loaders, then asserts:

- the exact accepted attestation IDs are IW-001, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-017, IW-019, and IW-184;
- every attested loader has a reservation group and anchor;
- all ten mandatory anchors are unique;
- exactly nine compatible groups are exposed;
- IW-008 and IW-010 still share `rg_rhine_saar` unless a later accepted closure changes the design.

Validation command:

```text
python -B .tools/audit_event6_allocator.py
```

Current static result: 149 publishers, 126 automatic/high-chaos packages, 138 SCN-008 ranked packages, 10 attested packages, 9 compatible reservation groups, exact 3/4/5/7/10 count targets, World Collapse count 10, and anchor → compact → extended → lock ordering. This is source evidence only; it does not claim a live ten-country transaction, host-remnant proof, Event-005 collision matrix, save/load proof, or scenario playback.

No gameplay, tag, map, asset, portrait, flag, advisor-icon, localisation, or attestation admission was changed by this guard.
