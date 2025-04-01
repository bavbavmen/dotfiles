XDG_CONFIG_HOME=$HOME/.config

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# PATH
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH
export PATH=$HOME/.cargo/bin:$PATH
export PATH=/opt/nvim-linux-x86_64/bin/:$PATH
export PATH=$HOME/.local/lib/nvim-linux-x86_64/bin/:$PATH

# Path to your Oh My Zsh installation.

export ZSH_CUSTOM="$HOME/.config/zsh/custom"
export ZSH="$HOME/.config/ohmyzsh"

ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(zsh-autosuggestions aliases ubuntu systemadmin sudo git history ansible vscode docker docker-compose zsh-fzf-history-search zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# qmk
export QMK_HOME='~/qmk_firmware'

# homebrew
test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bashrc


# User configuration
export EDITOR='nvim'

# my

## list dir
alias l="exa --icons"
alias lla="l -la"
alias lal=lla
alias la="l -a"

## installer ( apt )
alias in="sudo apt install"
alias aptlistdow="apt list --manual-installed"

## generic terminal 
alias e="exit"

## NeoVim
alias v="nvim"
alias vim="nvim"

## bat
alias bat=batcat
alias b=batcat

## git
alias undo-git-reset-head="git reset 'HEAD@{1}'"
alias gcma="git commit -am"
alias gcam="git commit -am"
alias gcm="git commit -m"
alias giff="git diff"
alias glog="git log --graph"
alias gpl="git pull"
alias gps="git push"
alias gpus=gps
alias gpush=gps
alias gstt="git status"
alias gst="git status"

## less
alias -g L='| less'

## grep
alias -g G='| grep'
alias g=grep

# scripts
bindkey '^ ' autosuggest-accept

alias dot='/usr/bin/git --git-dir=$HOME/.config/dotfiles/ --work-tree=$HOME'











# trash

# fzf
# bindkey -s '^P' 'locate / | fzf^M'
# bindkey '^O' 'locate / | fzf'

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
