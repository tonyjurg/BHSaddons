# BHSaddons website

The site uses the same compact sidebar and documentation style as Doc4TF.
Feature pages are generated from `docs/features/*.md`; the overview and usage
content come from the repository README. The build needs only Python 3.

From the repository root:

```powershell
python scripts/build_site.py
python -m http.server 8766 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8766/ to review locally. Rebuild after editing source files.
Generated output in `site/` is ignored by Git.

After approval, commit and push the source. In GitHub Settings → Pages, select
**GitHub Actions** as the build source. The workflow deploys pushes to `main`
and can also be started manually. If the default branch differs, update the
workflow branch first. The public URL will be https://tonyjurg.github.io/BHSaddons/.
