install:
	install -Dm 0755 ./main.py /usr/bin/winblues-paint
	install -Dm 0644 ./share/win.blues.paint.desktop /usr/share/applications/win.blues.paint.desktop
	install -Dm 0644 ./share/win.blues.paint.svg /usr/share/icons/hicolor/scalable/apps/win.blues.paint.svg

