# IW-179 FSM King John Sigra source-gate audit handoff (2026-09-20)

## Disposition

`BLOCKED / fail-closed`.

This bounded audit covers only King John Sigra, Na II, King John of Kosrae, image record `1936. [BM01009]`, and exact Micronesian Seminar or Bishop Museum collection variants of that record.

The consumer identity remains `FSM_independence_wave_inter_island_congress_chair`.

The expected sprite remains `GFX_portrait_FSM_independence_wave_inter_island_congress_chair`.

The expected runtime path remains `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds`.

The withdrawn fictional Elias Kihleng identity was not restored, substituted, or promoted.

## Exact source and collection evidence

The Rulers.org Micronesian traditional-polities roster is [https://rulers.org/micrtrad.html](https://rulers.org/micrtrad.html).

The roster lists Kosrae as Na II, “King John,” with a 1910–1946 governing period, birth year 1875, and death year 1957.

The Micronesian Seminar named photo record is [https://micsem.org/librarysearchphoto/king-john-sigra-chief-of-kosrae-stands-in-front-of-the-church/](https://micsem.org/librarysearchphoto/king-john-sigra-chief-of-kosrae-stands-in-front-of-the-church/).

The named photo title is “King John Sigra, Chief of Kosrae stands in front of the church.”

The Micronesian Seminar page identifies Francis X. Hezel S.J. as the poster and shows March 29, 2019 as the posting date.

The Micronesian Seminar footer states `© 2010-2019 all rights reserved`.

The exact Micronesian Seminar search record is [https://micsem.org/search-photos-results/page/82/](https://micsem.org/search-photos-results/page/82/).

The exact indexed record reads `1936. [BM01009]. Black & White Photo, Photograph, Restricted. King John Sigra, Chief of Kosrae stands in front of the church.`

The supplied collection association is the Bishop Museum Collection at Lelu, Kosrae.

Search snippets associated with the record mention 1953, but the exact indexed record states 1936 and is treated as authoritative for this audit.

Rulers.org establishes a named Kosraean traditional governor whose 1910–1946 tenure overlaps the 1936 opening, but it is not image or reuse-rights evidence.

The Micronesian Seminar record establishes an attributable named image record, but it is not an explicit derivative or reuse licence.

## Gate review

| Gate | Evidence | Result |
| --- | --- | --- |
| A. Named adult male Micronesian, Pohnpeian, or Carolinian identity | The exact records name King John Sigra, Na II, King John of Kosrae, and give a 1875 birth year, making him an adult in 1936. | `PASS` at the named adult identity level. |
| B. Civic or traditional governing role tied to the 1936 opening | Rulers.org gives a 1910–1946 Kosrae governing period, and the Micronesian Seminar title identifies him as Chief of Kosrae; this supports an adult traditional governing role during the 1936 opening. | `PASS` for the bounded traditional-role fit, without claiming an independently documented congress-chair appointment. |
| C. Stable attributable full-resolution image | The Micronesian Seminar page and exact BM01009 record are stable attributable records, but the full-resolution image bytes were not downloaded or decoded because the rights gate is restricted. | `FAIL CLOSED` for this admission because full-resolution dimensions, crop safety, and decoded-pixel evidence remain unverified. |
| D. Explicit derivative or reuse rights | The exact record is marked `Restricted`, the Micronesian Seminar footer says `all rights reserved`, and no explicit public-domain, Creative Commons, derivative, or written reuse permission is present in the supplied exact records. | `FAIL`. |
| E. Independent identity, framing, and provenance review | No image bytes were inspected, cropped, processed, or compared against the 156x210 leader reference family, and the 1936 versus 1953 date discrepancy remains unresolved. | `FAIL / NOT RUN`. |

All five gates do not pass, so the candidate cannot be admitted to IW-179.

## Rights finding and exact next action

No explicit reuse or derivative-rights path was found in the exact BM01009/Micronesian Seminar evidence supplied for this audit.

Do not download, process, crop, resize, convert, publish, or wire BM01009 without written permission.

The user or rights requester must ask Micronesian Seminar and the Bishop Museum collection rights contact to identify the controlling rights holder and provide written permission for reproduction of BM01009, a 156x210 source-placeholder crop and resize, DDS conversion, inclusion in a publicly distributed Hearts of Iron IV mod, and the required attribution and distribution terms.

That written response must also confirm whether the authoritative image date is 1936 or 1953 and whether the captioned subject is King John Sigra, Chief of Kosrae.

Only after that permission and date confirmation should an independent reviewer inspect identity, framing, and provenance and decide whether a source-placeholder package is admissible.

The user alone supplies any later HOI4-style grounded final through RunPod; RunPod was not opened or operated for this audit.

## Portrait references and current runtime state

The matching canonical leader reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`, including `contact_sheet.png` and the corresponding `CATALOG.md` rows.

The installed vanilla leader examples `gfx/leaders/AFG/Portrait_Afghanistan_Mohammed_Zahir_Shah.dds`, `gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds`, and `gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds` are 156x210 textures registered through `interface/_leader_portraits.gfx`.

The existing FSM runtime DDS is 156x210, 131168 bytes, and SHA-256 `64db23c13f8f3f488079ea24ca4d8ef9326bbb3fd9abbc94ee9b9251b004ae29`.

That existing DDS is withdrawn fictional evidence and is not King John Sigra source-placeholder evidence.

The portrait state for King John Sigra is `blocked`.

No `source_placeholder`, `replacement_pending`, or `styled_final` package state was created for King John Sigra.

## What was not changed

No source image was downloaded or archived under `docs/assets/portraits/006_independence_wave/`.

No original source file, lossless crop, crop-equality JSON, processed PNG, contact sheet, provenance contract, manifest, or source package was created.

The portrait converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was not run.

No new PNG or DDS output was created.

The existing FSM DDS, portrait-specific `.gfx` entry, character definition, localisation, central attestation, package counts, event scripts, country setup, gameplay, decisions, focuses, and unrelated UI were not changed.

No generated grounded likeness was created.

No generic regional image, unnamed person, other island leader, or withdrawn Elias Kihleng portrait was used as a substitute.

## Local archive recheck during continuation

The current FSM-named archive contains only the withdrawn fictional ImageGen master, its processed/review/DDS derivatives, and the associated metadata; that metadata records `source_kind = fictional`, `portrait_provenance = null`, and `status = candidate_requires_visual_approval`, so it is not source-placeholder evidence.

The retained `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/pacific_asante_sokoto/FSM_tosiwo_nakayama_1970_original.jpg` is a 12,421-byte historical source record with SHA-256 `CBD966FEDAF37E5901F0BF0CCBBF78F5E07A6954B2BD0254A4D9B5ED2C0AEEBC`, but its recorded 1970 date does not satisfy the 1936 opening-year role and image gate.

No new attributable 1936-compatible FSM source lead, durable source master, crop-equality record, provenance manifest, or rights receipt was found, and no portrait or gameplay state was changed.

## Remaining risks and skipped checks

The 1936 exact-record date versus 1953 search-snippet discrepancy remains a provenance risk until the collection owner confirms it.

The full-resolution source dimensions, source bytes, crop coordinates, decoded-pixel equality, alpha behavior, and SHA-256 for BM01009 were not established because the rights gate failed.

Independent identity, framing, and provenance review was skipped because there was no rights-cleared image to inspect.

DDS conversion, DDS header validation, runtime portrait replacement, live consumer validation, and any RunPod workflow were skipped by design.

The existing fictional runtime DDS may be mistaken for an admitted grounded source unless the parent keeps the source-gate state and central admission flag fail-closed.

## Changed files and handoff status

The only file changed by this audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw179_fsm_king_john_sigra_source_gate_2026-09-20.md`.

No gameplay, localisation, GFX, DDS, source archive, manifest, central attestation, package count, or unrelated Event 006 surface was changed.

This handoff is ready for parent review as a fail-closed source-gate record.
