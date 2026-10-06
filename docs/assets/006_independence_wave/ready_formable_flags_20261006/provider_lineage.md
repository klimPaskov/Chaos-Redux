# Provider lineage

Production used the official `imagegen` skill and the built-in OpenAI ImageGen tool in native mode; no API key, CLI fallback, external image, or reference-image input was used.

The accepted visual direction came from the parent-approved Event 006 brief and was checked against the canonical flag family at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/flags/` for shape, framing, and native size only.

The generator does not expose a model version in its result, so no model version is asserted here.

| Tag | ImageGen output | Staged source | Source dimensions | Source SHA-256 |
| --- | --- | --- | ---: | --- |
| `NCX` | `C:/Users/klimp/.codex/generated_images/01a110cf-9d6e-78f1-9d55-08fc93052e69/exec-260f662f-5967-4b48-b62a-9e9157dbcd5c.png` | `source_png/NCX_imagegen_master.png` | 1575x999 | `50BABD04713C32424A648AD9A3884EEA7EACF87CAFCD621E7F1B9F568E0F1D54` |
| `IDX` | `C:/Users/klimp/.codex/generated_images/01a110cf-9d6e-78f1-9d55-08fc93052e69/exec-ee124926-c12d-4fa1-b28e-cd9c6aa3041d.png` | `source_png/IDX_imagegen_master.png` | 1575x999 | `C2846C5FCEEBEDC2AAB294D003B637EC4D7FC43AE0D6DE680E7CB93A7B190BB3` |
| `MRX` | `C:/Users/klimp/.codex/generated_images/01a110cf-9d6e-78f1-9d55-08fc93052e69/exec-6601d02b-29d9-4a69-ac1c-41280e8f6d98.png` | `source_png/MRX_imagegen_master.png` | 1575x999 | `A713035BA0F59663277D6A01EBBB101E26BF9BAD2F9604C478DC2AB74C327E77` |
| `MSX` | `C:/Users/klimp/.codex/generated_images/01a110cf-9d6e-78f1-9d55-08fc93052e69/exec-6c4b1815-3f68-46a9-9245-116c1a7ee707.png` | `source_png/MSX_imagegen_master.png` | 1574x999 | `637E752CE4406E58EB3C0FE953BE4DB4BF420B40E70C4290F32BA6EE9D463369` |

Each staged master is an unchanged file copy of its ImageGen output; the manifest records its SHA-256.

Three distinct mainland-segment generations were reviewed before selection: the first was rejected for adding a filled gold hub, the second for taking the stepped bands to the flag edges, and the final output above was selected after explicitly requiring an open angular junction and clear margins.

The rejected mainland outputs remain in the ImageGen default output folder and are not runtime assets or package inputs.
