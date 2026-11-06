"""Ikon & logo kalfinsetiawan.com — satu sumber untuk build.py dan make_assets.py.

Ikon bergaya garis pada grid 24x24 (stroke 1.8, ujung bulat), kecuali logo X yang berupa isian.
Logo merek pihak ketiga (X) dipakai hanya untuk menautkan ke profil resmi.
"""

# ---------- Set ikon (isi <svg viewBox="0 0 24 24">) ----------
ICONS = {
    # kontak & sosial
    'x': '<path fill="currentColor" stroke="none" d="M18.9 1.15h3.68l-8.04 9.19L24 22.85h-7.41l-5.8-7.58-6.64 7.58H.47l8.6-9.83L0 1.15h7.59l5.24 6.93zm-1.29 19.5h2.04L6.49 3.24H4.3z"/>',
    # Jurkon: gelembung percakapan berisi tiga titik (sama seperti gelembung di antena Titik)
    'jurkon': '<path d="M6 3.5h12A2.5 2.5 0 0 1 20.5 6v8.5A2.5 2.5 0 0 1 18 17h-5.2L8.6 20.6a.5.5 0 0 1-.85-.37V17H6a2.5 2.5 0 0 1-2.5-2.5V6A2.5 2.5 0 0 1 6 3.5z"/><path d="M8.5 10.6h.01M12 10.6h.01M15.5 10.6h.01" stroke-width="2.6"/>',
    'github': '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>',
    'whatsapp': '<path d="M3.5 20.5l1.3-4.4A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.6 3.6 5.9 6.3 6.2l1.2-1.4-2.2-1.1-.9.7c-.9-.4-1.9-1.3-2.4-2.3l.7-.9-1-2.2z"/>',
    'email': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    'theme': '<circle cx="12" cy="12" r="8.5"/><path fill="currentColor" d="M12 3.5v17a8.5 8.5 0 0 0 0-17z"/>',
    # ikon proyek
    'chat': '<path d="M4 5h16v11H9l-5 4z"/>',
    'bolt': '<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
    'phone': '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M10 7.5h4M10 10.5h2.5"/>',
    'news': '<path d="M5 4h14v16H5zM8 8h8M8 12h8M8 16h5"/>',
    'page': '<path d="M6 3h9l3 3v15H6zM9 11h6M9 15h6"/>',
}
ICON_ATTR = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'


def icon(name, cls=''):
    """SVG inline (dekoratif) untuk dimasukkan ke HTML."""
    return '<svg%s viewBox="0 0 24 24" aria-hidden="true" focusable="false">%s</svg>' % (' class="%s"' % cls if cls else '', ICONS[name])


def icon_file(name):
    """Berkas SVG mandiri; warna mengikuti `color` (currentColor)."""
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="#111315" %s>%s</svg>\n' % (ICON_ATTR, ICONS[name])


# ---------- Logo: kepala Titik, maskot Jurkon Studio ----------
# Geometri diambil dari maskot (mascot/gen.py, kanvas 200): badan, visor gelap, mata, senyum,
# titik di perut, dan antena berujung titik kuning. Logo hanya memotong bagian kepala.
G1, G2 = '#4f46e5', '#ec4899'          # indigo -> pink (warna merek)
VISOR, YEL, AMB = '#0f1020', '#fde047', '#f59e0b'
TILE1, TILE2 = '#1e1b4b', '#2e1065'    # latar gelap untuk ikon aplikasi
_FIT = 'translate(-4 .32) scale(.36)'  # kanvas maskot -> viewBox 64


def _defs(uid, c1=G1, c2=G2):
    return ('<defs><linearGradient id="%sg" x1="38" y1="58" x2="162" y2="166" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
            '<linearGradient id="%sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".3"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>') % (uid, c1, c2, uid, )


def _titik(uid, stalk=G1, cls=False):
    """Kepala Titik dalam koordinat maskot (200 x 200)."""
    g = 'url(#%sg)' % uid
    a = ' class="lg-ant"' if cls else ''
    return (
        '<g%s><path d="M100 60C100 46 108 40 114 30" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="116" cy="24" r="17" fill="%s" opacity=".3"/><circle cx="116" cy="24" r="10.5" fill="%s" stroke="%s" stroke-width="2.6"/>'
        '<circle cx="112.6" cy="20.6" r="3" fill="#fff" opacity=".9"/></g>'
        '<ellipse cx="34" cy="122" rx="10" ry="14" transform="rotate(18 34 122)" fill="%s"/>'
        '<ellipse cx="166" cy="122" rx="10" ry="14" transform="rotate(-18 166 122)" fill="%s"/>'
        '<rect x="38" y="58" width="124" height="108" rx="48" fill="%s"/><rect x="38" y="58" width="124" height="108" rx="48" fill="url(#%sh)"/>'
        '<rect x="56" y="84" width="88" height="54" rx="27" fill="%s"/>'
        '<ellipse cx="80" cy="108" rx="8.2" ry="11" fill="#fff"/><ellipse cx="120" cy="108" rx="8.2" ry="11" fill="#fff"/>'
        '<path d="M90.5 124Q100 133.5 109.5 124" fill="none" stroke="#fff" stroke-width="5.4" stroke-linecap="round"/>'
        '<ellipse cx="65" cy="124" rx="6" ry="3.6" fill="#ff6fae" opacity=".85"/><ellipse cx="135" cy="124" rx="6" ry="3.6" fill="#ff6fae" opacity=".85"/>'
        '<circle cx="100" cy="153" r="4.2" fill="#fff" opacity=".92"/>'
    ) % (a, stalk, YEL, YEL, AMB, g, g, g, uid, VISOR)


def mark(uid='k', size=None):
    """Logo utama (viewBox 64): kepala Titik tanpa latar. uid dipakai agar id gradient unik bila di-inline."""
    s = ' width="%s" height="%s"' % (size, size) if size else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"%s role="img" aria-label="kalfinsetiawan">%s<g transform="%s">%s</g></svg>'
            ) % (s, _defs(uid), _FIT, _titik(uid))


def mark_inline(uid='lg'):
    """Versi HTML-inline (tanpa xmlns/role, aria-hidden); antena diberi kelas .lg-ant untuk animasi hover."""
    return ('<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">%s<g transform="%s">%s</g></svg>'
            ) % (_defs(uid), _FIT, _titik(uid, cls=True))


def mark_favicon():
    """Favicon: tanpa telinga, perut, dan pipi; goresan lebih tebal agar tetap terbaca di 16px."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="6" y1="22" x2="58" y2="62" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<path d="M32 26C32 20 35 17.5 38 14.5" fill="none" stroke="#6366f1" stroke-width="4" stroke-linecap="round"/>'
            '<circle cx="40" cy="11" r="6.2" fill="%s" stroke="%s" stroke-width="2.6"/>'
            '<rect x="4" y="22" width="56" height="41" rx="20" fill="url(#g)"/>'
            '<rect x="10" y="30" width="44" height="26" rx="13" fill="%s"/>'
            '<ellipse cx="23" cy="41" rx="4" ry="5.4" fill="#fff"/><ellipse cx="41" cy="41" rx="4" ry="5.4" fill="#fff"/>'
            '<path d="M27.5 49.5Q32 53.5 36.5 49.5" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>') % (G1, G2, YEL, AMB, VISOR)


def _tile(inner, scale, rx=0):
    t = (1 - scale) * 32
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="bg" x1="0" y1="0" x2="64" y2="64" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<rect width="64" height="64" rx="%s" fill="url(#bg)"/><g transform="translate(%.2f %.2f) scale(%s)">%s</g></svg>') % (TILE1, TILE2, rx, t, t, scale, inner)


def mark_tile(scale=.96):
    """Ikon aplikasi ‘any’ (192/512): Titik di atas ubin gelap bersudut membulat."""
    return _tile(_defs('t', G1, G2) + '<g transform="%s">%s</g>' % (_FIT, _titik('t', stalk='#818cf8')), scale, 15)


def mark_full(scale=.74):
    """Ikon ‘full-bleed’ (tanpa sudut membulat) untuk apple-touch & maskable; Titik dalam zona aman."""
    return _tile(_defs('f', G1, G2) + '<g transform="%s">%s</g>' % (_FIT, _titik('f', stalk='#818cf8')), scale, 0)


def mark_mono(color='currentColor'):
    """Logo satu warna (cetak, stempel, tema gelap): badan penuh, visor dilubangi, mata & senyum mengisi lubang."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" color="#111315"><defs><mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">'
            '<rect width="200" height="200" fill="#fff"/><rect x="56" y="84" width="88" height="54" rx="27" fill="#000"/>'
            '<ellipse cx="80" cy="108" rx="8.2" ry="11" fill="#fff"/><ellipse cx="120" cy="108" rx="8.2" ry="11" fill="#fff"/>'
            '<path d="M90.5 124Q100 133.5 109.5 124" fill="none" stroke="#fff" stroke-width="5.4" stroke-linecap="round"/></mask></defs>'
            '<g transform="%s" fill="%s"><path d="M100 60C100 46 108 40 114 30" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/><circle cx="116" cy="24" r="10.5"/>'
            '<g mask="url(#m)"><ellipse cx="34" cy="122" rx="10" ry="14" transform="rotate(18 34 122)"/><ellipse cx="166" cy="122" rx="10" ry="14" transform="rotate(-18 166 122)"/>'
            '<rect x="38" y="58" width="124" height="108" rx="48"/></g></g></svg>') % (_FIT, color, color)
