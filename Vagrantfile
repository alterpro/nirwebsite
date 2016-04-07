# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "debian/contrib-jessie64"
  config.vm.network "forwarded_port", guest: 8000, host: 8111
  config.vm.synced_folder ".", "/home/vagrant/nir-alter"
  config.ssh.forward_agent = true

    config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
    vb.cpus = 1
  end

# $SERVER_SETUP = <<-SCRIPT
#     export DEBIAN_FRONTEND=noninteractive
#     apt-get update
#     apt-get install python-dev
# SCRIPT

# config.vm.provision "shell", inline: $SERVER_SETUP, privileged: true
config.vm.provision :shell, :path => "install/install.sh"
end
