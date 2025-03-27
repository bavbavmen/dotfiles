# dotfiles
my dotfiles
in docs/install ther the screaps to install 
also https://github.com/bavbavmen/dotfiles/tree/main/.local/share/nvim/lazy will do problems
git clone --bare git@github.com:bavbavmen/dotfiles.git ~/.config/dotfiles
/usr/bin/git --git-dir=$HOME/.config/dotfiles --work-tree=$HOME stash
/usr/bin/git --git-dir=$HOME/.config/dotfiles --work-tree=$HOME stash drop 
## open zsh

dot config --local status.showUntrackedFiles no

