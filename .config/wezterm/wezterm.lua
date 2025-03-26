local wezterm = require('wezterm')

local config = wezterm.config_builder()

config.font = wezterm.font('Hack Nerd Font Mono')
config.font_size = 16.0

config.color_scheme = 'Catppuccin Mocha'
config.window_decorations = 'RESIZE'
config.enable_tab_bar = false

config.keys = {
   -- Move between windows
   {
      key = 'f',
      mods = 'CTRL|CMD',
      action = wezterm.action.ToggleFullScreen,
   },
}

return config
