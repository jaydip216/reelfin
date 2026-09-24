# Reelfin — Netflix-inspired Jellyfin theme

A standalone CSS theme with a dark canvas, red accents, rounded cards, responsive controls and an optional Continue Watching hero. Uses Jellyfin's own media, navigation and playback controls. No JavaScript, plugins, external fonts or bundled artwork.

Repository: [jaydip216/reelfin](https://github.com/jaydip216/reelfin).

## Compatibility

This theme is server-independent, not version-independent. There are no server addresses, user IDs, library IDs, media IDs or artwork URLs in the stylesheet. Existing and newly added movies and TV shows use the same rules. Your server name and library names remain your own.

The original layout was checked on a client reporting Jellyfin Web 12.0, in Desktop/Auto and Mobile (Legacy) modes. Earlier and future Web versions are unverified. Modern CSS support, including `:has()`, is required for all enhancements. Native clients that do not render Jellyfin Web are unaffected. TV remote navigation, right-to-left layouts and physical mobile apps have not been validated.

## Install

Back up your existing Custom CSS. Use this theme alone; remove other theme imports to avoid conflicting layouts.

**Direct installation (available now):** paste the complete `netflix-inspired.css` into **Dashboard > Branding > Custom CSS**, save and reload the client.

**Import from GitHub via jsDelivr:** paste the following into **Dashboard > Branding > Custom CSS**, save and reload the client. This URL requires `netflix-inspired.css` to be published at the root of the repository's `main` branch.

```css
@import url("https://cdn.jsdelivr.net/gh/jaydip216/reelfin@main/netflix-inspired.css");
```

The `main` import follows updates to the theme. For a fixed version, replace `@main` with an existing tested release tag from [Reelfin releases](https://github.com/jaydip216/reelfin/releases). Only use a tag after it has been published; no release tag is assumed to exist here.

Imports must precede any custom CSS rules. Each client needs access to the CDN; paste the CSS directly for installations that must work without that external dependency. CDN/browser caching can delay branch updates. Remove the import or pasted theme to uninstall, then restore your previous CSS and reload.

## Home layout and artwork

The theme works with your existing home section order. For the large hero, optionally put **Continue Watching first** in each user's Home settings. The hero activates only when that first section contains native landscape resume cards. Empty or differently arranged sections retain the regular row layout. CSS does not change user preferences.

- Portrait cards keep Primary poster artwork and native portrait proportions.
- Landscape cards use the thumbnail/backdrop selection made by Jellyfin.
- Square cards keep their native square proportions.
- Missing images follow Jellyfin's fallback behavior; CSS cannot create missing artwork or change which image endpoint the client requests.

Recently Added retains its native shape. To use landscape artwork in Movies/Shows library grids, select **Thumb** in that view's image settings where available. No per-title maintenance is needed when media is added.

## Customize labels

The extra hero labels default to English. Override them after the import (or after the pasted stylesheet):

```css
:root {
  --nfi-play-label: "Play";
  --nfi-info-label: "More Info";
}
```

These are visual labels on existing controls/links, not new navigation actions. Native Jellyfin labels retain the client's language. This is a visual theme, not a complete Netflix implementation: it cannot add recommendation logic, preview playback, or modal detail navigation. Hero paging uses Jellyfin's native scrolling.

## Validation and release

Earlier live checks covered home, Movies/Shows grids, movie/episode details and 320–430px phone layouts plus 1440px desktop. Movie and series posters and Next Up thumbnails were checked after removing item-specific overrides. The public packaging revision has static checks only; test it on target Web versions before claiming support for them.

Run `python3 validate.py` to check CSS structure and prevent server-specific artwork/URLs from entering the release. This is not a replacement for browser layout testing. Before tagging a release, check desktop/mobile home with Continue Watching first, a different first section, empty resume history, movies, episodes, missing artwork, keyboard navigation, detail pages and a server hosted under a URL base path.

Publish only `netflix-inspired.css`, `README.md`, `LICENSE`, `validate.py` and `.gitignore`. Historical local backups and artwork mappings are deliberately excluded. Publish these files at the root of `jaydip216/reelfin` on `main`, then verify that the CDN URL in the installation instructions returns the stylesheet. Verify a tagged import before recommending a pinned release.

## License

MIT. This community theme is not affiliated with Netflix or the Jellyfin project and includes no Netflix assets.

References: [Jellyfin CSS customization](https://jellyfin.org/docs/general/clients/css-customization/) and [jsDelivr documentation](https://www.jsdelivr.com/documentation).
