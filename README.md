# nand2tetris-2nd-ed
「コンピュータシステムの理論と実装 第2版」のプロジェクトとそのメモ

# コンピュータシステムの理論と実装 第2版

- [日本語版の紹介ページ（O'Reilly Japan）](https://www.oreilly.co.jp/books/9784814400874/)
- [原著の紹介ページ（MIT Press）](https://mitpress.mit.edu/9780262539807/the-elements-of-computing-systems/)
- [Web版IDE](https://nand2tetris.github.io/web-ide)

# プロジェクトの進捗

| 番号 | 名前 | 進捗 |
| :--- | :--- | :--- |
| 01 | ブール論理 | 完了 |
| 02 | ブール算術 | 完了 |
| 03 | メモリ | 完了 |
| 04 | 機械語 | 完了 |
| 05 | コンピュータアーキテクチャ | 完了 |
| 06 | アセンブラ | 取り組み中 |
| 07 | 仮想マシンⅠ：処理 | 未着手 |
| 08 | 仮想マシンⅡ：制御 | 未着手 |
| 09 | 高水準言語 | 未着手 |
| 10 | コンパイラⅠ：構文解析 | 未着手 |
| 11 | コンパイラⅡ：コード生成 | 未着手 |
| 12 | OS | 未着手 |
| 13 | さらなる冒険へ | 未着手 |

# メモ
## Web版IDE
### ローカルファイルへのアクセス不可
#### 問題
実装をテストするには、Web版IDEからローカルファイルへアクセスする必要がある。
ただし、ブラウザがFirefoxやSafariの場合はアクセスできない。

#### 解決方法
ChromeやEdgeでは利用可能であり、ローカルファイルにアクセスできる（2025年4月28日時点）。

#### 原因
原因は、Web版IDE内部でローカルファイル選択に使っている`showDirectoryPicker`メソッドが、これらのブラウザでは未実装であることらしい。
- 参考：[[bug]: Settings menu under Safari doesn't support local project files?](https://github.com/nand2tetris/web-ide/issues/560#issuecomment-2654768606)

### プロジェクト05のMemoryのテストについて
#### 問題
Web版IDEでMemoryをテストすると、次のメッセージが表示されたところで実行が停止する。

```
Before you run this script, select the 'Screen' option from the 'View' menu
```

しかしWeb版IDEには「View」メニューが存在しないため、先に進めない。
また「Screen」は Memory.hdl を選択した時点で表示される（ただし、ウィンドウが小さいと非表示になる）。

#### 解決方法
デスクトップ版IDEを使えば、テストが止まらずに進む。
- デスクトップ版IDEは、公式サイト[From Nand to Tetris](https://www.nand2tetris.org/software)にあるNand to Tetris Software packageに同封

メッセージは一度表示されるものの、その後もテストが続行し、進捗に応じて別のメッセージが表示される。