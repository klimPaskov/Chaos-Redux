## Validation Notes

Commands run:

```bash
identify docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/processed_png/*.png
identify docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/package_dds/*.dds
identify -verbose docs/assets/005_soviet_union_collapse/central_asia_federation_first_batch/processed_png/*.png | rg "Type:|Alpha:"
identify -verbose gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_city_congress.dds
identify -verbose gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_turkestan_federation_road.dds
identify -verbose gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_delegates.dds
identify -verbose gfx/interface/goals/soviet_collapse/central_asia_soviet_collapse_federation_state.dds
```

Results:

- all processed PNG files are `94x86`
- all package/root DDS files are `94x86`
- all processed PNG and root DDS files report `TrueColorAlpha`
- checker preview sheet written to `contact_sheets/central_asia_federation_first_batch_checker.png`

Known caveat:

- the source generator rendered a fake checkerboard instead of native transparency
- alpha was recovered with ImageMagick corner flood-fill cleanup
- because of that, these four files should be treated as `needs_user_review` before broad duplicate-group rollout

