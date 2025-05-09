-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here
local o = vim.opt

-- plugins
vim.g.snacks_animate = false -- cursser move in animainton

-- nvim
-- General
o.confirm = true -- Confirm to save changes before exiting modified buffer
o.cmdheight = 1
o.completeopt = "menuone,noselect"
o.confirm = true
o.cursorline = false
o.fileformats = "unix,dos"
o.hidden = true
o.laststatus = 3
o.mouse = "a"
o.showmode = false
o.splitbelow = false
o.splitright = true
o.termguicolors = true
o.timeoutlen = 250
o.undofile = true
o.swapfile = false
o.backup = false
o.wrap = false

-- Side numbers
o.number = true
o.relativenumber = true

-- Search
o.ignorecase = true
o.scrolloff = 3

-- Tabs
o.breakindent = true
o.copyindent = true
o.expandtab = true
o.shiftwidth = 4
o.softtabstop = 4
o.tabstop = 4
