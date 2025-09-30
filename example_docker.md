# Dockerコンテナの使い方

## Dockerとは

Dockerはコンテナ技術を使った仮想化プラットホームです。軽量で高速に動作する事が特長です。

## インストール

Dockerをインストルするには、以下のコマンドを実行して下さい：

```bash
sudo apt-get install docker
```

## 基本的な使い方

コンテナを起動するにわ、以下のようにします：

```bash
docker run -it ubuntu bash
```

このコマンドで、ubuntuのコンテナが起動して、bashシェルが使えるようになります。

## イメージの管理

イメージの一覧を表示するには：

```bash
docker images
```

イメージを削除する時は：

```bash
docker rmi image_name
```

## まとめ

Dockerは簡単で便利なので、是非使ってみて下さい。コンテナを使えば、環境構築が簡単にできます。
