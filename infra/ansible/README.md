# ansible-playbook-example

ansible playbook のサンプル

## Requirements

* pyenv
* direnv
* yarn
* Node.js

## 前提

* サーバの種類(type): jump, ap, db, etc
* サーバの環境(env): prod, dev, vagrant, etc

## セットアップ

```
$ pip install pip-tools
$ pip-sync requirements.txt requirements.dev.txt

$ ansible-galaxy install -r roles.yml

$ yarn

$ compile-servers

$ vagrant up
```

## playbookの実行

```
$ ansible-playbook install -i inventories/vagrant playbooks/all.yml
```

## servers.yml

各サーバの環境, 種類, ipアドレスなどを管理するファイル。
このファイルを元に compile-servers で sshcfg や inventoryファイルを生成する。

## binディレクトリ

direnvを使ってPATHを通している。
幾つかスクリプトを置いてある。

* compile-servers
* deploy_ssh_key_vagrant.sh

### compile-servers

servers.ymlを元に sshcfg や inventoryファイルを生成するコマンド。

### deploy_ssh_key_vagrant.sh

vagrantのプロビジョニングで実行するスクリプト。
ansible-playbookを実行するのに必要な公開鍵をvmに配置する。
ansible-playbookの実行はvagrantのプロビジョニングではなく、
ansible-playbookコマンドで実行する。

### package.json

nodeのプロジェクトではないが、nodeのモジュールを活用している。

* precommitでコミットメッセージのフォーマットとテストの実行
* standard-versionによるタグとCHANGELOGの生成

## ssh-keys

ssh鍵の置き場
