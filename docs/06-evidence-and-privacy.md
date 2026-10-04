# Evidence and privacy

The public collection contains **46 images**: **22 with permanent redactions** and **24 with no sensitive details identified during review**. Twenty-three images have added context banners; analysis screenshots use amber outlines where a visible directory/file selection can be marked accurately.

## Publication method

1. Preserve the original image privately and record its SHA-256.
2. Review visible content for credentials, account paths, email identifiers, device labels/serials, MAC addresses, unique IPv6 values, and home-network details.
3. Replace sensitive regions with opaque black pixels using precise local image processing.
4. Re-encode from pixels as PNG, removing source metadata.
5. Add a separate context banner and, where appropriate, an amber selection outline to the publication copy.
6. Confirm original hashes, unchanged evidence pixels outside documented masks/outlines, correct captions, and publication image hashes.
7. Review the new publication copy visually and check the final package.

Two high-resolution photographs exceed GitHub's browser upload limit as PNG. Their public copies use metadata-free, lossless WebP; decoded RGB pixels were compared byte for byte against the reviewed PNG and matched exactly. The remaining 44 images use PNG. No generative image editing or screenshot resampling was used. The underlying screenshot retains its original pixel dimensions; context labels add space above it. The published file therefore has different dimensions when a banner is present. Hashes in the image manifest identify the **publication copies**, not the private originals.

Private originals, raw USB images, OEM firmware exports, raw acquisition reports, configuration files, DHCP lease contents, passwords, and the generated OpenWrt configuration archive are excluded. Device-specific MAC/IPv6 values and private upstream addresses are masked. Factory defaults such as `192.168.1.1`, public test targets, observed public DNS answers, and firmware integrity digests remain because they explain the tests.

The original collection numbering is retained. One earlier removed-USB view, numbered E007, could not be recovered. It is not counted as a published image or represented as present. The remaining E001–E047 entries total 46 images.

## Navigating the evidence

- [Evidence index](../evidence/README.md): All images grouped by phase with individual captions.
- [Local gallery](../evidence/evidence-gallery.html): Download/clone the repo and open this file in a browser; it has no external dependencies.
- [Image manifest](../evidence/image-manifest.json): Per-image SHA-256, dimensions, redaction categories, and annotation information.
- [Review report](../evidence/results/redaction-review.json): Counts and checks used for the publication set.
- [Validation summary](../evidence/results/validation-summary.json): Current completed scope and remaining limits.

## Verify a downloaded copy

From the repository root, run:

```text
python scripts/verify-publication.py
```

The checker uses Python's standard library. It checks the image count, SHA-256 values, PNG and lossless WebP dimensions/chunks, referenced local files, and excluded artifact types. It does not execute the USB installation script or certify that an image contains no visually sensitive information; visual review remains part of publication preparation.
