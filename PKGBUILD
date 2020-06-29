# Maintainer: tyjak <dev at tyjak dot net>
_pkgname='quickswitch-for-i3'
pkgname='quickswitch-i3'
pkgver=2.8.0
pkgrel=1
pkgdesc="quickly change to and locate windows in i3"
arch=(any)
url="https://github.com/tyjak/quickswitch-for-i3"
license=('WTFPL')
groups=()
depends=('i3-wm' 'python' 'python-i3-py' 'dmenu')
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=("https://github.com/tyjak/$_pkgname/archive/$pkgver.tar.gz")
md5sums=('SKIP')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
