## brave
curl -fsS https://dl.brave.com/install.sh | sh

## git hub ssh
ssh-keygen -t ed25519 -C "bavbav2003@gmail.com"
cat ~/.ssh/id_ed25519.pub

## wezterm
curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /etc/apt/keyrings/wezterm-fury.gpg
echo 'deb [signed-by=/etc/apt/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
sudo apt update
sudo apt install wezterm

## zsh
chsh -s $(which zsh)



***
## qtile 
#!/bin/bash

# Remove the EXTERNALLY-MANAGED file so pip works again
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

# Install the full Python 3 Suite, pip, git and all Dependencies
sudo apt update
sudo apt install python3-full python3-pip libpangocairo-1.0-0 python3-cffi python3-xcffib git -y

# Install cairocffi using pip
pip install --no-cache-dir cairocffi

# Clone the Qtile Source Code from GitHub
git clone https://github.com/qtile/qtile.git

# Install Qtile
cd qtile
pip install .

# Xsessions Desktop file
cat > ./temp << "EOF"
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Type=Application
Keywords=wm;tiling
EOF

sudo cp ./temp /usr/share/xsessions/qtile.desktop
sudo echo "Exec=/home/$USER/.local/bin/qtile start" | sudo tee -a /usr/share/xsessions/qtile.desktop

# Cleanup
rm ./temp
***

