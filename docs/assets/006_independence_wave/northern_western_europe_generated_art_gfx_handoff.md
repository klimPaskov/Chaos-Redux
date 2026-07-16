# Event 006 northern and western Europe generated-flag engine handoff

## Authority and ownership boundary

This is the current flag-only engine handoff for the ACX, AFX, AGX, and AJX
Event 006 triplets. It supplies exact runtime lookup paths and validation
evidence. It does not supply a sprite registration block because HOI4 loads
country flags by tag filename.

No `.gfx`, `.gui`, country, state, character, event, decision, focus, idea,
history, localisation, or spreadsheet file is edited by this package.

## Automatic engine lookup

HOI4 discovers the four unsuffixed triplets directly under the standard flag
ladder:

| Tag | Normal 82×52 | Medium 41×26 | Small 10×7 |
| --- | --- | --- | --- |
| ACX | `gfx/flags/ACX.tga` | `gfx/flags/medium/ACX.tga` | `gfx/flags/small/ACX.tga` |
| AFX | `gfx/flags/AFX.tga` | `gfx/flags/medium/AFX.tga` | `gfx/flags/small/AFX.tga` |
| AGX | `gfx/flags/AGX.tga` | `gfx/flags/medium/AGX.tga` | `gfx/flags/small/AGX.tga` |
| AJX | `gfx/flags/AJX.tga` | `gfx/flags/medium/AJX.tga` | `gfx/flags/small/AJX.tga` |

Do not add `spriteType` entries for these files. Do not move them into an
event-scoped subdirectory. `gfx/flags/`, `gfx/flags/medium/`, and
`gfx/flags/small/` are engine lookup roots whose filenames must remain exact.

Every file is an uncompressed 32-bit BGRA TGA with eight-bit alpha and a
bottom-left origin. The flag-only builder decodes every runtime file and proves
exact pixel and orientation equality with its processed PNG before refreshing
the ledger.

## Route-use locks

These are unsuffixed baseline identities only:

| Tag | Authorized use | Not authorized by this handoff |
| --- | --- | --- |
| ACX | baseline Cornish identity using St Piran's Cross | inferred ideology variants, cosmetic variants, or content-readiness claim |
| AFX | baseline Walloon identity using the 1913 coq hardi | inferred ideology variants or alternate rooster redesigns |
| AGX | baseline Friesland identity using the provincial flag | pan-Frisian substitution, inferred ideology variants, or altered band/charge layout |
| AJX | baseline Saar identity using the Saar Territory 1920–1935 tricolour | inferred ideology variants, added emblems, or changed stripe order |

No `<TAG>_democratic.tga`, `<TAG>_communism.tga`, `<TAG>_fascism.tga`,
`<TAG>_neutrality.tga`, or cosmetic-tag mapping is approved here. A later route
may add one only through an accepted design and explicit route-to-filename
contract.

## AEX no-standalone-flag boundary

AEX remains a vanilla `BEL_flanders` cosmetic overlay, not a standalone Event
006 flag family. Do not create:

- `gfx/flags/AEX.tga`;
- `gfx/flags/medium/AEX.tga`;
- `gfx/flags/small/AEX.tga`;
- matching generated or processed AEX files under the NWE flag tree.

The retained Lion of Flanders historical source documents the vanilla cosmetic
overlay only. It is not an input for a standalone AEX triplet. The builder
fails if an AEX artifact appears; it does not silently adopt or delete one.

## Source and review authority

- `northern_western_europe_generated_art_manifest.md` is the flag inventory,
  processing, runtime, and hash authority.
- `prompts/006_nwe_generated_art.md` preserves the four exact prompts,
  historical citations, rights notes, original ImageGen output locations,
  canonical ladder choices, repo copies, and palettes.
- `006_nwe_historical_flag_comparison.md` records the manual design comparison.
- `contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`
  compares cited design, official ImageGen raw, and deterministic flat master.
- `contact_sheets/006_nwe_generated_flags_contact_sheet.png` shows the decoded
  runtime normal, medium, and small TGAs.
- `generated_nwe_hashes.sha256` inventories only the explicit flag evidence and
  runtime paths.

## Reproduction and implementer check

Run from the mod root:

```powershell
python -B docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py --scope flags
```

The no-argument invocation is equivalent. `flags` is the only accepted scope
value.

After reproduction, confirm:

1. exactly ACX, AFX, AGX, and AJX exist in each processed flag ladder;
2. all twelve TGAs have the required dimensions, 32-bit depth, eight-bit alpha,
   and bottom-left origin;
3. decoded runtime pixels equal their processed PNGs;
4. both flag contact sheets reopen correctly;
5. the AEX standalone paths remain absent;
6. the hash ledger contains only flag evidence and runtime flag paths.

No copy-ready `.gfx` fragment is required or permitted for this flag family.

## Remaining content boundary

The four triplets resolve their flag-art surface only. ACX retains its separate
Cornwall geography/state-ownership blocker. AEX remains outside standalone
flag scope. Neither condition should be inferred from flag-file presence alone.

## Simplifications, omissions, and blockers

No fallback, placeholder, route variant, or registration workaround is used.
There is no unresolved flag-engine handoff blocker.
