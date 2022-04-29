# 本專案是針對pyechart之研究
研究目標是希望能實現網頁上的『數據資料圖形視覺化』之介面設計研究

**注意1:**

本研究是windows10底下的測試環境(原始開源庫似乎是在Linux上),

而測試環境建議使用Thonny IDE，為了編寫方便我會使用SublimeText編寫。

不建議使用Pyzo或Mu之類的IDE測試,似乎會無法正常發揮功能。


## pyecharts-master 目錄說明:
這是原始開源庫,來源於https://pyecharts.org

本庫即是基於該框架的各種研究，

## pyecharts-flask-demo 目錄說明:
包含Flask的快速生成chart的簡易測試程式。

## firstTest.py 說明:
一支快速生成chart的簡易測試程式,它沒有flask之功能,只是簡單生成html檔案並顯示bar圖表的方法。

## myTestCharts.html 說明:
由firstTest.py所生成的檔案。

## pipinstall-UFlask.py 說明:
說明了如何pip安裝Flask網路服務框架之說明與安裝。

## pipinstallpyecharts-U.py 說明:
說明了如何安裝pyecharts插件之方法與測試。