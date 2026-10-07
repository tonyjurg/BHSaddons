# BHSaddons website

The site uses the same compact sidebar and documentation style as Doc4TF.
Feature pages are generated from `docs/features/*.md`; the overview and usage
content come from the repository README. The build needs only Python 3.

From the repository root:

```powershell
python scripts/build_site.py
python -m http.server 8767 --bind 127.0.0.1 --directory docs
```

Open http://127.0.0.1:8767/ to review locally. Rebuild after editing source files.
The published site lives in `docs/`. Generated HTML and assets are committed
alongside the original `docs/features/*.md` files and their images. The feature
index links to every rendered feature page; each page also links to its Markdown source.

After approval, commit and push the source and rebuilt `docs/` files. In GitHub
Settings → Pages, select **Deploy from a branch**, branch **main**, folder **/docs**.
The public URL will be https://tonyjurg.github.io/BHSaddons/.
