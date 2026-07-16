# Frozen v4.3 portrait-input resolution

Date: 2026-07-16

The final independent audit found that five second-tranche commander-small metadata records retained absolute paths to the removed private production directory. The portrait pixels, runtime DDS files, review sheets, processor hashes, and overlay hashes all passed, but those path strings were not portable.

The complete seventeen-file v4.3 input set is retained under `_tooling/v4_3_frozen_inputs/` as exact Git blob bytes from commit `6729ad0cd74e0ed294a0b603a0eb677a0533099c`. It includes the processor, overlay manifest, frame and paper sources/overlays/prompts, the two retained superseded ImageGen iterations used by the manifest, the dossier comparison sheet, and all six canonical dossier references.

All thirty metadata `processor` fields now resolve to the frozen processor. All ten commander-small metadata records resolve their embedded overlay, prompt, reference-directory, and canonical-comparison paths inside the same frozen bundle. Independent path and hash validation found zero missing records and confirmed:

- processor: `c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`;
- overlay manifest: `be1ff82d3f460ca1e0572ff3cb23853fdd87d2a0a8444f20cdad6565cacd2d2f`;
- frame source/overlay: `77857264f8f6e36c75c675969f73e5ba5ee936f38599c6d843e2e07c527c0740` / `950596dd88da0b58861af9e58cacdaa80b2e6308af9168dd98ad390ae42aea79`;
- paper source/overlay: `5d5f5c76e0a290c848cc71e8ff8f102a87e47227d32c9902350bc7f1eb00d491` / `e5db0602b4b5d82ba148552bfa2a6c7b6e00c6a91137de2b3baec404535210a0`.

No portrait image, DDS file, processing value, processor pin, sprite, gameplay file, or custom advisor asset changed in this provenance repair.
