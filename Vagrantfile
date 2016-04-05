# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder ".", "/home/vagrant/nir-alter"
  config.ssh.forward_agent = true

    config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
    vb.cpus = 1
  end

$SERVER_SETUP = <<-SCRIPT
    export DEBIAN_FRONTEND=noninteractive
    apt-get update
    apt-get install python-dev
SCRIPT

config.vm.provision "shell", inline: $SERVER_SETUP, privileged: true

end