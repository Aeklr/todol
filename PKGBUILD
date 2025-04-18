pkgname=todol
pkgver=1.0
pkgrel=1
pkgdesc="Simple Python CLI to-do list app with persistent storage"
arch=('any')
url="https://github.com/Aeklr/todol"
license=('GPL-3.0-only')
depends=('python')
source=("to-do.py" "LICENSE")
md5sums=('SKIP' 'SKIP') # To be replaced

package() {
	# Files for the app
	install -d "$pkgdir/usr/share/$pkgname"
    	install -m755 to-do.py "$pkgdir/usr/share/$pkgname/"

	# Symlink
	install -d "$pkgdir/usr/bin"
	ln -s "/usr/share/$pkgname/to-do.py" "$pkgdir/usr/bin/todol"

	# License
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}


