# GL-Antique 修正用スクリプト

GL-Antiqueを修正するスクリプトです。主に縦書きの問題を修正します。

## 修正方法

現状ではFontForgeにバグがあるので、下記パッチを適用したFontForgeを使っ
てください。

「FontForge用縦書きパッチ」
http://www.akenotsuki.com/eyeben/fonts/kura.html#ffpatch

ff_generate.py と同じディレクトリに GL-Antique.sfd を置き、シェルから次
のコマンドを実行してください。

make GL-Antique.ttf

GL-AntiquePlusの修正も同様に、次のコマンドで行えます。

make GL-AntiquePlus.ttf

## 修正内容

ff_generate.py スクリプトは次の修正を行います。

### 1. バージョン番号の変更

オリジナルと区別するため、バージョン番号を変更します。

### 2. GSUBテーブルの修正

縦書き用グリフが使えるようにGSUBテーブルを修正します。

### 3. 縦書き用メトリクスの設定

縦書き用メトリクスを設定します。
