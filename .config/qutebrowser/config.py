import catppuccin

catppuccin.setup(c, 'mocha', True)

config.load_autoconfig(False)

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:133.0) Gecko/20100101 Firefox/133.0', 'https://accounts.google.com/*')
config.set('content.images', True)
config.set('content.javascript.enabled', True)
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/user/.local/share/qutebrowser/userscripts/*')
config.set('content.local_content_can_access_file_urls', False, 'file:///home/user/.local/share/qutebrowser/userscripts/*')

c.content.javascript.clipboard = "access"
c.colors.webpage.preferred_color_scheme = "dark"
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.page = "always"



# hebrew sopport
config.unbind('.')
en_keys = "qwertyuiopasdfghjkl;'zxcvbnm,./"
he_keys = "/'קראטוןםפשדגכעיחלךף,זסבהנמצתץ."
c.bindings.key_mappings.update(dict(zip(he_keys, en_keys)))


