# Portfolio — Working Agreement

This is **Akash Reddy Vanga's** personal portfolio, deployed to GitHub Pages at
<https://akash-reddy-46.github.io/portfolio/>.

Repo: `github.com/akash-reddy-46/portfolio`, branch `main` (GitHub Pages publishes from `main`).

## The contract

When the user asks for a change, follow this loop exactly. Do not improvise.

1. **Make ONLY the change that was asked.** Do not refactor surrounding code, restyle adjacent
   sections, re-audit the site, or "improve while you're in here". If the user says "change
   the title", change only the title. Surface anything else you notice in chat — don't act on it.

2. **Verify the change works** before committing.
   - For HTML/CSS/copy edits: open `index.html` (`start index.html` on Windows) and confirm the
     change is visible in the right place and nothing nearby is broken.
   - For JS edits: run the relevant skill/cert/snippet through the browser console and confirm
     no errors in DevTools.
   - For schema/JSON-LD edits: paste the JSON-LD block into <https://search.google.com/test/rich-results>
     (the user can do this) — at minimum, validate it's still parseable JSON.
   - Tag balance: `grep -oE '<section[ >]' index.html | wc -l` should equal `grep -oE '</section>' index.html | wc -l`.
     Same for `<article>` and `<div>`.

3. **If the change broke something**, fix the breakage first. Verify again. Then commit the
   fix as part of the same logical commit — do NOT leave a broken intermediate commit on `main`.

4. **Commit and push.**
   - One commit per user request.
   - Imperative subject, ≤ 70 chars, no co-author footer needed.
   - `git add <specific files>` — never `git add -A` (avoids `.env`, draft files, secrets).
   - `git push origin main` after a successful commit.

5. **Do NOT commit unrelated changes.** If `git status` shows files you didn't touch, stop and
   ask the user before staging them.

## Commit message style

Imperative, lowercase, ≤ 70 chars. Examples:

- `fix availability text on contact section`
- `drop akkash and akash more from json-ld alternate names`
- `add bachelor's degree to education section`
- `tighten hero metrics from 4 to 3 tiles`
- `fix typo in faq tech-stack answer`

Skip: `feat: ...`, `chore: ...`, `Implement feature X` (we use plain sentences, not conventional commits here).

## Constants — do not change without an explicit ask

| Field | Value |
|---|---|
| Display name | Akash Reddy Vanga |
| Brand mark | `Akash Reddy` (no dot separator) |
| Email | vangaakashreddy@gmail.com |
| Phone / WhatsApp | +91 77992 18720 |
| LinkedIn | <https://www.linkedin.com/in/akash-reddy-vanga-49377b358> |
| GitHub | <https://github.com/akash-reddy-46> |
| Location | Hyderabad, Telangana, India |
| Current role | Software Engineer at JaaGa.AI (since Apr 2026) |
| Experience claim | 2.5+ years full-time + 6-month internship (NOT "3+ years") |
| Employer confidentiality | **No JaaGa-internal detail on the site.** No private repo names, module/worker counts, commit counts, business figures (revenue, transaction volume, failure/delivery rates, document throughput) or named internal products (CRM, lawyer module, marketing suite). Describe work by engineering category instead. JaaGa.AI as employer name and www.jaaga.ai are fine. |
| Color palette | Blue (`#4169e1`) + Green (`#008000`) on dark (`#06080f`) |

## Things to NEVER change without an explicit ask

- Color palette
- The `Person` / `WebSite` / `ProfilePage` / `FAQPage` / `BreadcrumbList` JSON-LD `@id` URLs
- The visible name on the page (`Vanga Akash Reddy` in hero h1)
- Section IDs (`#stack`, `#ai`, `#about`, `#experience`, ...) — these are linked from external places
- File structure (`index.html`, `assets/`, `robots.txt`, `sitemap.xml`)
- The 5 most recent commits' style — match the existing repo voice

## Reference: known fragile areas

- **Skills array** in the bottom `<script>` block — every skill needs `{name, cat, icon, level}`,
  and `icon` MUST be a key in the `ICONS` object (`code`, `api`, `db`, `cloud`, `grid`,
  `layers`, `bolt`, `card`, `infinity`, `branch`, `brain`, `spark`, `spider`, `chat`).
- **Hero metrics** — the CSS `.hero-metrics { grid-template-columns: repeat(N, ...) }` must match
  the number of `.hm` children. Keep `.hm-num` values short (a number or one short word); longer
  strings like "Full-stack" wrap mid-word and push the hero past one viewport.
- **Hero height** — the hero is tuned to ~832px so it fits one 900px screen. If you add a line to
  the lede or a metric label wraps, re-check it.
- **Stack card pills** — `.sc-pills span.key` is the highlighted "use daily" state.
- **JSON-LD FAQ entries** must mirror the visible FAQ items. If you add/edit a visible question,
  edit the corresponding entry in `@type: FAQPage` too — otherwise Google rich results break.

## Default response shape

After making a change:

1. One sentence: what changed.
2. One line per file edited: `path:line — what now reads/looks different`.
3. The commit hash (short).
4. Stop. Don't suggest further work unless the user asks.
