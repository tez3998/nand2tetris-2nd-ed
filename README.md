# nand2tetris-2nd-ed
「コンピュータシステムの理論と実装 第2版」のプロジェクトとそのメモ

# コンピュータシステムの理論と実装 第2版

- [日本語版の紹介ページ（O'Reilly Japan）](https://www.oreilly.co.jp/books/9784814400874/)
- [原著の紹介ページ（MIT Press）](https://mitpress.mit.edu/9780262539807/the-elements-of-computing-systems/)
- [IDE](https://nand2tetris.github.io/web-ide)

# プロジェクトの進捗

| 番号 | 名前 | 進捗 |
| :--- | :--- | :--- |
| 01 | ブール論理 | 完了 |
| 02 | ブール算術 | 完了 |
| 03 | メモリ | 完了 |
| 04 | 機械語 | 完了 |
| 05 | コンピュータアーキテクチャ | 取り組み中 |
| 06 | アセンブラ | 未着手 |
| 07 | 仮想マシンⅠ：処理 | 未着手 |
| 08 | 仮想マシンⅡ：制御 | 未着手 |
| 09 | 高水準言語 | 未着手 |
| 10 | コンパイラⅠ：構文解析 | 未着手 |
| 11 | コンパイラⅡ：コード生成 | 未着手 |
| 12 | OS | 未着手 |
| 13 | さらなる冒険へ | 未着手 |

# メモ
## IDE
### ローカルファイルへのアクセス
実装結果をテストするときに、IDEからローカルファイルにアクセスする必要があるが、FirefoxやSafariではローカルファイルにアクセスできない。
この理由は、[ローカルファイルを選択する機能にshowDirectoryPicker()というメソッドを使っていて、このメソッドはFirefoxやSafariでは未実装であるから](https://github.com/nand2tetris/web-ide/issues/560#issuecomment-2654768606)らしい。
ChromeやEdgeであれば、ローカルファイルにアクセス可（2025年4月28日時点）。

### プロジェクト05のMemoryのテスト
プロジェクト05のMemoryをテストする際、Web版のIDEだと以下のメッセージが表示されたところでテストの実行が停止してしまう。

> Before you run this script, select the 'Screen' option from the 'View' menu

Web版のIDEを見てもViewメニューなんて無いし、Screenに関してはMemory.hdlを選択した時点で表示されている（ただし、Screenはウィンドウが小さすぎると表示されない）。

一方で、デスクトップ版（デスクトップ版は[公式サイト](https://www.nand2tetris.org/software)のNand to Tetris Software packageに同封）ではメッセージ自体は一度表示されるが、その後もテストが進み、進捗に応じて別のメッセージが表示される。
そのため、このようにフリーズしたら、デスクトップ版を試すのがおすすめ。

デスクトップ版にはViewメニューがあるので、おそらくこれが理由でテストが停止せずに進むのだと思う。これがWeb版のバグなのかどうかは不明。