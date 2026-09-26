# IW-039/DON vanilla Sidorin portrait reuse audit — 2026-09-26

**Disposition:** `blocked` for Event 006 reuse; the existing vanilla Sidorin role remains unchanged outside Event 006.

## Acceptance basis and scope

The user accepted conditional use of the existing vanilla Sidorin portrait only after source, DLC, sprite, and role-consumer audit, with no Event 006 portrait dependency and no substitute face. This was a read-only audit; no asset, sprite, character, localization, or gameplay file was changed.

## Consumer and installed asset findings

Vanilla `common/characters/DON.txt:3-29` defines `DON_vladimir_sidorin` with `army.large = GFX_portrait_DON_Vladimir_Sidorin` and `army.small = GFX_idea_DON_vladimir_sidorin`, as well as despotism/fascism country-leader roles and a field-marshal role. Vanilla DON history recruits Sidorin at `history/countries/DON - Don Republic.txt:82`.

The large sprite registration is `dlc/dlc034_no_step_back/interface/nsb_portraits.gfx:378-380` and points to `gfx/leaders/DON/portrait_DON_Vladimir_Sidorin.dds`. The small sprite registration is `dlc/dlc034_no_step_back/interface/nsb_ideas_characters.gfx:12-14` and points to `gfx/interface/ideas/idea_DON_vladimir_sidorin.dds`.

Both registrations and both referenced DDS assets are under the No Step Back DLC; no base-game copy or registration was found. The large DDS is 156×210, 131,168 bytes, SHA-256 `1be56c40228920e9354380f9ef9193320a98e14171ddeedd6b29de66b31eeb63`. The small DDS is 65×67, 17,548 bytes, SHA-256 `66495d37184f4e4800088b200181a7fcba8abc539f97c6fbe478b6c821e9c47e`.

`descriptor.mod:1` does not require No Step Back, so the target audience's DLC availability is unknown. A current source search across `common/`, `interface/`, `events/`, `history/`, and `gfx/` found no Event 006 Sidorin consumer or portrait sprite reference. The existing vanilla character and its registered DLC portrait do not create an Event 006 consumer.

## Provenance and review limits

The earlier [IW-039 source portrait handoff](006_iw039_don_portrait_source_placeholder_2026_08_12.md) attributes an archived Sidorin photograph to a Commons record and a Commons-credited RIA 1914 image, recording unknown authorship, 1914–1918 dating, `PD-RusEmpire`, and a United States pre-1931 public-domain basis. It does not establish that this photograph is the source of the No Step Back DDS. The handoff documents a 380×512 crop and a 156×210 PNG, but those derivative files are absent from the current portrait archive inventory.

The vanilla DDS could not be inspected visually because the viewer rejected its format; no conversion or image processing was performed. Thus, no visual likeness assessment or provenance link between the archival image and the vanilla portrait is claimed.

## Result and follow-up gate

The conditional reuse contract remains blocked until No Step Back availability, vanilla DDS source lineage, visual/role suitability, and an actual Event 006 consumer are established. Do not add a new Event 006 portrait dependency, portrait sprite, placeholder, or substitute face while these gates remain unresolved.

No game launch, runtime test, or MCP portrait validation was performed. The user alone handles any HOI4-styled grounded final through the repository's RunPod workflow if a future approved design requires a distinct portrait.
