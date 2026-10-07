"""Build the GitHub Pages site from repository Markdown (Python 3, no dependencies)."""
from pathlib import Path
import html
import re
import shutil
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"


def inline(text):
    text = re.sub(r'`([^`]+)`', lambda m: '<code>' + html.escape(m[1]) + '</code>', text)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img alt="\1" src="\2">', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    return text


def markdown(source):
    lines = source.splitlines()
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith('```'):
            i += 1
            code = []
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            result.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>')
        elif re.match(r'^#{1,6} ', line):
            level = len(line.split(' ')[0])
            result.append(f'<h{level}>{inline(line[level+1:])}</h{level}>')
        elif i + 1 < len(lines) and re.match(r'^\|?\s*:?-{3,}', lines[i + 1]):
            rows = [line]
            i += 2
            while i < len(lines) and '|' in lines[i] and lines[i].strip():
                rows.append(lines[i])
                i += 1
            table = '<div class="table-wrap"><table><thead>'
            for n, row in enumerate(rows):
                tag = 'th' if n == 0 else 'td'
                table += '<tr>' + ''.join(f'<{tag}>{inline(c.strip())}</{tag}>' for c in row.strip().strip('|').split('|')) + '</tr>'
                if n == 0:
                    table += '</thead><tbody>'
            result.append(table + '</tbody></table></div>')
            continue
        elif re.match(r'^\s*[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*] ', lines[i]):
                items.append('<li>' + inline(re.sub(r'^\s*[-*] ', '', lines[i])) + '</li>')
                i += 1
            result.append('<ul>' + ''.join(items) + '</ul>')
            continue
        elif line.startswith('>'):
            quote = []
            while i < len(lines) and lines[i].startswith('>'):
                value = lines[i].lstrip('> ').strip()
                if not value.startswith('[!'):
                    quote.append(inline(value))
                i += 1
            result.append('<blockquote>' + ' '.join(quote) + '</blockquote>')
            continue
        else:
            paragraph = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r'^(#|```|>|\s*[-*] )', lines[i]):
                paragraph.append(lines[i])
                i += 1
            result.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            continue
        i += 1
    return '\n'.join(result)


def page(title, content, depth=0, active=''):
    prefix = '../' * depth
    nav = [('index.html', 'BHSaddons', 'home'), ('about.html', 'About BHSaddons', 'about'),
           ('usage.html', 'Using BHSaddons', 'usage'), ('features.html', 'Feature documentation', 'features'), ('legal.html', 'Legal', 'legal')]
    links = ''.join(f'<a href="{prefix}{url}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>' for url, label, key in nav)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | BHSaddons</title>
<meta name="description" content="Additional parasha, aliya and word boundary features for the BHSA Text-Fabric dataset.">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/style.css"></head>
<body><a class="skip" href="#content">Skip to content</a><div class="wrapper">
<header><h1><a href="{prefix}index.html">BHSaddons</a></h1>
<div class="project-mark"><img src="{prefix}assets/logo.svg" width="250" height="163" alt="BHSaddons — additional features layered on the BHSA dataset"></div>
<p class="tagline">Additional features for the BHSA Text-Fabric dataset.</p>
<nav aria-label="Project navigation">{links}<a href="https://github.com/tonyjurg/BHSaddons">GitHub repository</a><a href="https://doi.org/10.5281/zenodo.14051603">Zenodo archive</a></nav></header>
<main id="content">{content}</main>
<footer><p><a class="project-credit" href="https://www.tj-engineering.nl"><img src="{prefix}assets/tje-black.png" width="40" height="40" alt="TJ Engineering"><span>a TJ Engineering project</span></a></p><p><small>Hosted on GitHub Pages<br>Layout inspired by <a href="https://tonyjurg.github.io/Doc4TF/">Doc4TF</a> and the <a href="https://github.com/orderedlist/minimal">Minimal theme</a>.</small></p></footer>
</div></body></html>'''


def build():
    OUT.mkdir(exist_ok=True)
    (OUT / 'assets').mkdir(exist_ok=True)
    shutil.copy(ROOT / 'website/style.css', OUT / 'assets/style.css')
    shutil.copy(ROOT / 'website/favicon.svg', OUT / 'assets/favicon.svg')
    shutil.copy(ROOT / 'website/logo.svg', OUT / 'assets/logo.svg')
    shutil.copy(ROOT / 'website/tje-black.png', OUT / 'assets/tje-black.png')
    shutil.copytree(ROOT / 'images', OUT / 'images', dirs_exist_ok=True)
    shutil.copytree(ROOT / 'docs/features/images', OUT / 'features/images', dirs_exist_ok=True)
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    overview = readme.split('# BHSaddons\n', 1)[1].split('## Adding the features')[0]
    overview = overview.replace('docs/features/', 'features/').replace('.md)', '.html)')
    overview = overview.replace('our this feature set focus', 'this feature set focuses').replace('wordboudaries', 'word boundaries')
    usage_notes = 'To use this functionality' + readme.split('To use this functionality', 1)[1].split('## BibTeX')[0]
    feature_list = 'The following features' + overview.split('The following features', 1)[1]
    pages = {
        'index': ('BHSaddons', '# BHSaddons\n\n## What is BHSaddons?\n\n' + overview.split('The following features')[0] + '\n## How to use BHSaddons\n\nLoad the additional features alongside BHSA using the Text-Fabric `mod` option. See the [usage guide](usage.html) for installation and examples.\n\n## Available features\n\nSeven features describe parashot, aliyot, maftir verses, and surface word boundaries. Browse the [feature documentation](features.html) for descriptions, values, and frequency tables.\n\n## Licence\n\nSee the [legal page](legal.html) for attribution, licence details, and the BHSA data licence.'),
        'about': ('About BHSaddons', '# About BHSaddons\n\n' + overview.split('The following features')[0] + '\n## Dataset\n\nThe features in this repository accompany BHSA version `2021`. Six features apply to verse nodes; `wordboundary` applies to word nodes.\n\n## Cite this project\n\n' + readme.split('## BibTeX')[1]),
        'usage': ('Using BHSaddons', '# Using BHSaddons\n\n## Adding the features\n\n```python\nfrom tf.app import use\n\nA = use("etcbc/BHSA", version="2021",\n        mod="tonyjurg/BHSaddons/tf/", hoist=globals())\n```\n\n' + usage_notes),
        'features': ('Feature documentation', '# Feature documentation\n\n' + feature_list),
        'legal': ('Legal', (ROOT / 'LICENCE.md').read_text(encoding='utf-8').replace('# License', '# Legal and licence', 1)),
    }
    for name, (title, source) in pages.items():
        (OUT / f'{name}.html').write_text(page(title, markdown(source), active='home' if name == 'index' else name), encoding='utf-8')
    for path in sorted((ROOT / 'docs/features').glob('*.md')):
        text = path.read_text(encoding='utf-8').replace('.md)', '.html)').replace('wordboudaries', 'word boundaries')
        value_type = 'Integer' if '@valueType=int' in (ROOT / f'tf/2021/{path.stem}.tf').read_text(encoding='utf-8') else 'String'
        text = re.sub(r'`Node`\|`(?:String|Integer)`', f'`Node`|`{value_type}`', text)
        content = '<p class="breadcrumb"><a href="../features.html">Features</a> / ' + path.stem + '</p>' + markdown(text)
        (OUT / f'features/{path.stem}.html').write_text(page(path.stem, content, 1, 'features'), encoding='utf-8')
    (OUT / '.nojekyll').touch()
    validate_links()
    print(f'Built 12 pages in {OUT}')


def validate_links():
    class Links(HTMLParser):
        def handle_starttag(self, tag, attrs):
            for key, value in attrs:
                if key not in ('href', 'src') or not value:
                    continue
                url = urlsplit(value)
                if url.scheme or url.netloc or not url.path:
                    continue
                target = self.path.parent / unquote(url.path)
                if not target.exists():
                    raise ValueError(f'Broken local link in {self.path}: {value}')
    for path in OUT.rglob('*.html'):
        parser = Links()
        parser.path = path
        parser.feed(path.read_text(encoding='utf-8'))
    print('All local page and asset links are valid.')


if __name__ == '__main__':
    build()

