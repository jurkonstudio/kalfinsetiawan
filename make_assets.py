#!/usr/bin/env python3
"""Membuat ulang semua aset visual kalfinsetiawan.com: logo, wordmark, favicon, ikon, OG.
Jalankan: python3 make_assets.py   (butuh rsvg-convert, ImageMagick `convert`, fonttools, Playwright, font Inter)"""
import os, json, subprocess
from icons import ICONS, icon_file, mark, mark_favicon, mark_full, mark_mono, mark_tile, G1, G2, YEL, AMB

A = 'assets'
os.makedirs(A + '/icons', exist_ok=True)


def w(path, txt):
    open(path, 'w', encoding='utf-8').write(txt)


def png(svg_path, out, size):
    from playwright.sync_api import sync_playwright
    svg = open(svg_path, encoding='utf-8').read().replace('<svg ', '<svg width="%d" height="%d" ' % (size, size), 1)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': size, 'height': size})
        pg.set_content('<body style="margin:0;background:transparent">%s</body>' % svg)
        pg.screenshot(path=out, omit_background=True, clip={'x': 0, 'y': 0, 'width': size, 'height': size}); b.close()


# 1) Logo, favicon (SVG)
w(A + '/logo.svg', mark('k') + '\n')
w(A + '/logo-mono.svg', mark_mono() + '\n')
w(A + '/favicon.svg', mark_favicon() + '\n')
w(A + '/icon-full.svg', mark_full() + '\n')
w(A + '/icon-tile.svg', mark_tile() + '\n')

# 2) Wordmark / lockup: teks diubah jadi kurva (Inter Bold) agar tampil sama di mana pun
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen


def text_path(text, font_path, size):
    f = TTFont(font_path); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    sc = size / upm; x = 0; d = []
    for ch in text:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x, 0)))
        d.append(pen.getCommands()); x += gs[g].width * sc
        # kerning sederhana dinonaktifkan; jarak huruf diperketat sedikit
        x -= size * 0.02
    return ' '.join(d), x


INTER = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
word, wd = text_path('kalfinsetiawan', INTER, 40)
dot_x = wd + 4
lock_w = 64 + 12 + dot_x + 12
lockup = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %.1f 64" role="img" aria-label="kalfinsetiawan.">%s'
          '<g transform="translate(76 43.5)"><path d="%s" fill="#111315"/><circle cx="%.1f" cy="-3.8" r="4.6" fill="%s" stroke="%s" stroke-width="1.8"/></g></svg>\n')
mk = mark('lk').replace(' xmlns="http://www.w3.org/2000/svg"', '').replace(' role="img" aria-label="kalfinsetiawan"', '')
mk_inner = mk[mk.index('<defs>'):mk.rindex('</svg>')]
w(A + '/logo-wordmark.svg', lockup % (lock_w, mk_inner, word, dot_x + 4.6, YEL, AMB))
w(A + '/logo-wordmark-light.svg', (lockup % (lock_w, mk_inner, word, dot_x + 4.6, YEL, AMB)).replace('#111315', '#ffffff'))

# 3) PNG & ICO
for n in (16, 32, 48):
    png(A + '/favicon.svg', '/tmp/_fav%d.png' % n, n)
subprocess.run(['convert', '/tmp/_fav16.png', '/tmp/_fav32.png', '/tmp/_fav48.png', A + '/favicon.ico'], check=True)
png(A + '/favicon.svg', A + '/favicon-32.png', 32)
png(A + '/icon-tile.svg', A + '/icon-192.png', 192)
png(A + '/icon-tile.svg', A + '/icon-512.png', 512)
png(A + '/icon-full.svg', A + '/apple-touch-icon.png', 180)
png(A + '/icon-full.svg', A + '/icon-maskable-512.png', 512)
for p in ('/tmp/_fav16.png', '/tmp/_fav32.png', '/tmp/_fav48.png'):
    os.remove(p)

# 4) Manifest
w(A + '/site.webmanifest', json.dumps({
    'name': 'Kalfin Agus Setiawan', 'short_name': 'kalfinsetiawan', 'start_url': '/', 'display': 'browser',
    'background_color': '#f7f7f4', 'theme_color': '#4f46e5',
    'icons': [
        {'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
        {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
        {'src': 'icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]
}, indent=2) + '\n')

# 5) Set ikon baru: berkas per-ikon + sprite
for k in ICONS:
    w('%s/icons/%s.svg' % (A, k), icon_file(k))
sprite = '<svg xmlns="http://www.w3.org/2000/svg" style="display:none">' + ''.join(
    '<symbol id="i-%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</symbol>' % (k, v) for k, v in ICONS.items()) + '</svg>\n'
w(A + '/icons/sprite.svg', sprite)

# 6) Gambar Open Graph 1200x630 (dirender di Chromium)
html = '''<!doctype html><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0}body{width:1200px;height:630px;font-family:Inter,sans-serif;color:#fff;position:relative;overflow:hidden;
background:radial-gradient(60%% 90%% at 100%% 0%%,rgba(236,72,153,.55),transparent 70%%),radial-gradient(70%% 90%% at 0%% 100%%,rgba(99,102,241,.55),transparent 70%%),linear-gradient(135deg,#1e1b4b,#312e81 55%%,#4c1d95)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:60px 60px;mask-image:linear-gradient(120deg,transparent 30%%,#000)}
.in{position:absolute;left:84px;top:78px;bottom:78px;width:720px;display:flex;flex-direction:column;justify-content:space-between}
.mascot{position:absolute;right:34px;top:100px;width:410px;height:410px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.4))}
.halo{position:absolute;right:-20px;top:50px;width:500px;height:500px;border-radius:50%%;background:radial-gradient(circle,rgba(255,255,255,.16),transparent 68%%)}
h1{font-size:92px;font-weight:700;letter-spacing:-.045em;line-height:1}h1 b{color:#fde047}
.t{font-size:34px;font-weight:600;letter-spacing:-.01em;margin-top:22px}.s{font-size:26px;color:#ddd6fe;margin-top:12px;font-weight:500}
.ic{display:flex;gap:14px}.ic i{width:60px;height:60px;border-radius:16px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.25);display:grid;place-items:center}
.ic svg{width:28px;height:28px;color:#fff;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
</style><div class="grid"></div><div class="halo"></div><div class="mascot">%s</div><div class="in"><div class="ic"><i><svg viewBox="0 0 24 24">%s</svg></i><i><svg viewBox="0 0 24 24">%s</svg></i><i><svg viewBox="0 0 24 24">%s</svg></i></div><div><h1>kalfinsetiawan<b>.</b></h1><div class="t">Jurkon &nbsp;·&nbsp; Boombastis &nbsp;·&nbsp; Smartphone Empire</div><div class="s">Portofolio Kalfin Agus Setiawan, Jurkon Studio</div></div></div>''' % (
    mark('og').replace(' xmlns=\"http://www.w3.org/2000/svg\"', '').replace(' width=\"132\" height=\"132\"', ''), ICONS['x'], ICONS['jurkon'], ICONS['github'])
w('/tmp/_og.html', html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
    pg.goto('file:///tmp/_og.html'); pg.wait_for_timeout(400); pg.screenshot(path='/tmp/_og.png'); b.close()
subprocess.run(['convert', '/tmp/_og.png', '-quality', '90', '-sampling-factor', '4:4:4', A + '/og.jpg'], check=True)
os.remove('/tmp/_og.png'); os.remove('/tmp/_og.html')
print('Aset selesai')
