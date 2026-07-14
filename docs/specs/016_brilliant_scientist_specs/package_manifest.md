# Event 016 package manifest

| Field | Value |
| --- | --- |
| Event ID | `16` |
| Event name | Brilliant Scientist |
| Event slug | `brilliant_scientist` |
| Scientist | Doctor Warren Kruger |
| Entry classification | Minor fire-once |
| Source status | Reconciled implementation specification |
| Package date | 2026-07-14 |
| Intended spec root | `docs/specs/016_brilliant_scientist_specs/` |
| Planning state | Improvement addendum disposition complete, gameplay incomplete, default-disabled |
| Cluster | None |
| World-end capability | Yes, conditional late branch |
| Custom country | Kruger State, working public label |
| Custom UI | Kruger Directorate, working interface label |
| Super-event text research | Complete for all six retained packages |
| Visual asset status | Stage-0 leader and advisor portraits complete and registered, later visual assets missing, later sprite contracts pre-registered only |
| Audio status | Research and six Event 016-owned OGGs complete, shared music, sound, settings, event, and localisation wiring absent |
| World-end reservations | `11` Laboratory World, `12` Strategic Singularity |
| Visible super-event reservations | `90` recognition, `91` formation, `92` threat, `93` Laboratory World, `94` Singularity, `95` defeat |

## Source-of-truth order

1. The user's Event 16 brief.
2. `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`, including parent dispositions R1 through R7.
3. The reconciled specification files in this package.
4. Promoted portions of the improvement addendum. Rejected R1 and R6 recommendations are historical evidence only.
5. The project-wide skills and `AGENTS.md`.
6. Current implementation files as evidence of existing behavior, not as permission to shrink the design.

## Design dispositions

| Question | Disposition |
| --- | --- |
| Preserve the simple baseline | Yes. The opening remains one scientist and one immense research advantage. |
| Build a full science simulation | No. The system is a focused Kruger management loop, not a universal science economy. |
| Replace host focus trees | No. Host content is decision-led and additive. |
| Give Kruger a full focus tree after rebellion | Yes. The breakaway state is a durable playable chaos country. |
| Reveal alien origin immediately | No. Early text keeps the origin uncertain. Evidence accumulates through projects and portrait changes. |
| Make every project mandatory | No. Limited capacity forces portfolio choices. |
| Let removal be a visible percentage roll | No. The player receives readable warning states, while the exact independence threshold stays hidden. |
| Let a rejected Kruger disappear | No. He is transferred to another valid country and the chain continues there. |
| Let the terminal device ignore world-end rules | No. It forces chaos above the existing terminal threshold before firing the world-end branch. |
| Add an Evolution V | No. World Collapse is a terminal gate, not an additional evolution stage. |
| Put Event 16 in the planned Research cluster | No. The user explicitly placed it in no cluster. |
| Keep the catalog's separate `Crazy Scientist` idea | No. It is absorbed and redesigned inside Event 16; the standalone concept is superseded. |
| Remove international recognition from the super-event set | No. Keep it as a thresholded conditional package. |
| Reduce the achievement set | No. Preserve exactly seventeen distinct achievements. |
| Expose Directorate state | Mandate, Dependence, Exposure, and Project Capacity are visible. Independent Capacity and Grievance remain hidden. |

## File status legend

- `specified`: design surface is reconciled and ready for implementation, but is not implemented.
- `research_gate`: implementation depends on source verification or licensing.
- `blocked`: a required implementation, research, asset, audio, or integration dependency is absent.
- `implementation_only`: intentionally left to the implementation agent, such as final focus coordinates and exact script IDs.

## Package integrity summary

- Package file counts and sizes are intentionally not frozen because linked plan, event-doc, asset-manifest, and super-event-research surfaces live outside this directory.
- Source-reading ledger entries: `30`.
- Achievement working keys: `17`.
- Super-event packages: `6`.
- Severe portrait animation families: `5`.
- Integrity ledger: `package_checksums.sha256`.

The checksum ledger preserves the established 53-entry reconciled Event 016 documentation source set named in its header. It uses repository-relative paths in the existing order and excludes the ledger itself. No ZIP or implementation-readiness claim is made.
