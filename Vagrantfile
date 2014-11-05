# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    # Build Vagrant box based on Fedora 20
    config.vm.box = "chef/fedora-20"

    config.vm.provision "shell", inline: "yum update -y"
    config.vm.provision "shell", inline: "yum install -y docker-io python-pip"
    config.vm.provision "shell", inline: "systemctl start docker"
    config.vm.provision "shell", inline: "systemctl enable docker"
    config.vm.provision "shell", inline: "usermod -a -G docker vagrant"
    config.vm.provision "shell", inline: "docker pull dfarrell07/helium:dev"
    config.vm.provision "shell", inline: "pip install -r /vagrant/requirements.txt"

end
