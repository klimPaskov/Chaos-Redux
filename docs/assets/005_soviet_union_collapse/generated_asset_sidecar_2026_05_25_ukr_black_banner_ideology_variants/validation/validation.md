# Validation

Commands run from repository root:

```bash
identify docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants/processed_png/*.png docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants/tga/*.tga
```

Result:

- `UKR_BLACK_BANNER_communism_normal.png`: `82x52`
- `UKR_BLACK_BANNER_democratic_normal.png`: `82x52`
- `UKR_BLACK_BANNER_fascism_normal.png`: `82x52`
- `UKR_BLACK_BANNER_neutrality_normal.png`: `82x52`
- `UKR_BLACK_BANNER_communism_medium.png`: `41x26`
- `UKR_BLACK_BANNER_democratic_medium.png`: `41x26`
- `UKR_BLACK_BANNER_fascism_medium.png`: `41x26`
- `UKR_BLACK_BANNER_neutrality_medium.png`: `41x26`
- `UKR_BLACK_BANNER_communism_small.png`: `10x7`
- `UKR_BLACK_BANNER_democratic_small.png`: `10x7`
- `UKR_BLACK_BANNER_fascism_small.png`: `10x7`
- `UKR_BLACK_BANNER_neutrality_small.png`: `10x7`

TGA metadata checked with a small header read:

- all sidecar TGA outputs are image type `2`
- all sidecar TGA outputs are `32` bpp
- all sidecar TGA outputs have descriptor `8`

Visual check:

- `contact_sheets/ukr_black_banner_ideology_variants_contact.png` decodes upright.
- No generated text, labels, watermarks, vanilla Ukrainian flag layout, or real extremist symbols were visible in the processed previews.
