# Provenance

## Generation

All visible case-card artwork was created through thirteen separate calls to
OpenAI's built-in ImageGen. Ten calls supply the accepted masters. Three calls
are retained under `sources/rejected/` because their approximately 2.5:1
canvases would have required a material vertical crop for the 3.125:1 runtime
contract.

The PNG sources retain their built-in C2PA provenance assertions. Exact
generation handles, timestamps, revised prompts, reference roles, workspace
paths, and source SHA-256 values are frozen in
`metadata/source_handles.json`; the same prompts are readable in
`prompts/exact_imagegen_prompts.md`.

## Reference use

- `utopia_ledger_background_panel.png` was used only as a palette and existing
  interface-family style reference for the first master and the initial family
  calls.
- The accepted `no_target` master was used only as a family composition,
  camera, and proportion reference for later states.
- Every state call requested a fresh, independent illustration. No accepted
  state was constructed by recolouring, tracing, warping, or attaching a stock
  icon to another card.
- No web-sourced or third-party media is included, so there are no external
  licence or attribution obligations.

## Rejections and replacements

| Handle | State | Reason |
|---|---|---|
| `exec-eda0034a-0e35-4ee9-bab3-f7e7ec617d52` | Target selected | 2.5197:1 post-matte canvas required a material vertical crop. |
| `exec-92568123-7993-4044-b10c-a9d8a4564078` | Ultimatum available | 2.5006:1 post-matte canvas required a material vertical crop. |
| `exec-30745e31-dd3f-4eaf-a3ce-e00154a1dd83` | Target selected retry | 2.5006:1 retry still required a material vertical crop. |

Fresh 3.0:1 replacements were accepted for Target Selected and Ultimatum
Available. The rejection sheet is
`contact_sheets/case_cards_rejected_aspect_contact_sheet.png`.

## Mechanical finishing

`tooling/process_case_cards.py` performs only these operations:

1. trim an external near-white matte where present;
2. make a centred, content-safe crop to the 3.125:1 runtime ratio;
3. apply one restrained family-wide colour grade;
4. resize uniformly with Lanczos to `300x96` and apply restrained output
   sharpening;
5. export PNG and one-level uncompressed BGRA8 DDS;
6. decode the DDS and require exact RGBA pixel equality.

The processor does not draw, trace, reconstruct, composite, or author any
state symbol or border. Per-state crop and grade records are in
`metadata/processing_report.json`.

