"""Ikon & logo kalfinsetiawan.com — satu sumber untuk build.py dan make_assets.py.

Ikon bergaya garis pada grid 24x24 (stroke 1.8, ujung bulat), kecuali logo X yang berupa isian.
Logo merek pihak ketiga (X) dipakai hanya untuk menautkan ke profil resmi.
"""

# ---------- Set ikon (isi <svg viewBox="0 0 24 24">) ----------
ICONS = {
    # kontak & sosial
    'x': '<path fill="currentColor" stroke="none" d="M18.9 1.15h3.68l-8.04 9.19L24 22.85h-7.41l-5.8-7.58-6.64 7.58H.47l8.6-9.83L0 1.15h7.59l5.24 6.93zm-1.29 19.5h2.04L6.49 3.24H4.3z"/>',
    # Jurkon: gelembung percakapan berisi huruf J (jurnal koneksi)
    'jurkon': '<path d="M6 3.5h12A2.5 2.5 0 0 1 20.5 6v8.5A2.5 2.5 0 0 1 18 17h-5.2L8.6 20.6a.5.5 0 0 1-.85-.37V17H6a2.5 2.5 0 0 1-2.5-2.5V6A2.5 2.5 0 0 1 6 3.5z"/><path d="M13.25 7.2v3.9a2.15 2.15 0 0 1-4.3 0"/>',
    'github': '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>',
    'whatsapp': '<path d="M3.5 20.5l1.3-4.4A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c.2 2.6 3.6 5.9 6.3 6.2l1.2-1.4-2.2-1.1-.9.7c-.9-.4-1.9-1.3-2.4-2.3l.7-.9-1-2.2z"/>',
    'email': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    'theme': '<circle cx="12" cy="12" r="8.5"/><path fill="currentColor" d="M12 3.5v17a8.5 8.5 0 0 0 0-17z"/>',
    # ikon proyek
    'chat': '<path d="M4 5h16v11H9l-5 4z"/>',
    'bolt': '<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
    'phone': '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M10 8l2 2 2-2"/>',
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


# ---------- Logo: monogram K + titik koneksi ----------
G1, G2 = '#4f46e5', '#ec4899'          # indigo -> pink (warna merek)
# Huruf K: batang tegak, lengan atas berujung simpul (titik), kaki bawah.
K_PATH = 'M21 15.5V48.5M21.5 34L40.5 19.5M27.5 31.5L43 48.5'


def mark(uid='k', size=None, gloss=True, stroke=6.4, rx=16):
    """Logo utama (viewBox 64). uid dipakai agar id gradient unik bila di-inline."""
    s = ' width="%s" height="%s"' % (size, size) if size else ''
    g = ('<rect width="64" height="64" rx="%s" fill="url(#%sh)"/>' % (rx, uid)) if gloss else ''
    gd = ('<linearGradient id="%sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".55" stop-color="#fff" stop-opacity="0"/></linearGradient>' % uid) if gloss else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"%s role="img" aria-label="kalfinsetiawan"><defs><linearGradient id="%sg" x1="6" y1="2" x2="58" y2="62" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>%s</defs>'
            '<rect width="64" height="64" rx="%s" fill="url(#%sg)"/>%s'
            '<path d="%s" fill="none" stroke="#fff" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"/><circle cx="46" cy="16" r="5.2" fill="#fff"/></svg>') % (s, uid, G1, G2, gd, rx, uid, g, K_PATH, stroke)


def mark_inline(uid='lg'):
    """Versi HTML-inline (tanpa xmlns/role, aria-hidden)."""
    return mark(uid).replace(' xmlns="http://www.w3.org/2000/svg"', '').replace(' role="img" aria-label="kalfinsetiawan"', ' aria-hidden="true" focusable="false"')


def mark_favicon():
    """Favicon: tanpa gloss, goresan lebih tebal agar tetap tajam di 16px."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="6" y1="2" x2="58" y2="62" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<rect width="64" height="64" rx="15" fill="url(#g)"/>'
            '<path d="M20.5 14.5V49.5M21 34.5L40.5 19M27.5 31.5L44 49.5" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="46.5" cy="15.5" r="6" fill="#fff"/></svg>') % (G1, G2)


def mark_full(k_scale=.62):
    """Ikon ‘full-bleed’ (tanpa sudut membulat) untuk apple-touch & maskable; K dalam zona aman."""
    t = (1 - k_scale) * 32
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="64" y2="64" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<rect width="64" height="64" fill="url(#g)"/><g transform="translate(%.2f %.2f) scale(%s)"><path d="%s" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="46" cy="16" r="5.6" fill="#fff"/></g></svg>') % (G1, G2, t, t, k_scale, K_PATH)


def mark_mono(color='currentColor'):
    """Logo satu warna (mis. untuk cetak, stempel, tema gelap)."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" color="#111315"><path d="%s" stroke="%s" stroke-width="6.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="46" cy="16" r="5.2" fill="%s"/></svg>') % (K_PATH, color, color)
