###Cocos 版本关系说明

####Cocos2d-x 与 Cocos Studio 版本对应关系

*此部分数据来自[CocoaChina: Cocos Studio和Cocos2d-x版本对应关系](http://www.cocoachina.com/bbs/read.php?tid-182077-keyword-%B0%E6%B1%BE%B6%D4%D3%A6.html)，数据可能不完整，仅提供参考。*

* Studio 2.x

| CocosStudio 版本 | Cocos2d-x 版本 | Cocos2d-js 版本 | 备注 |
| :-------: |:-------:|:------:|:------|
v2.1.5<br>v2.1.2beta<br>v2.1 | v3.4final | v3.3 rc0+ | Cocos 新增 JSON 格式导出，Cocos2d-JS 仅支持此格式，v2.1 更名 Cocos |
v2.1beta | v3.4beta0 | 不支持 | 已分离出 reader，可以将 reader 拉取到其他版本 Cocos2d-x，以支持新版本的 CocosStudio |
v2.0.6 | v3.3final | 不支持 |
v2.0.5 | v3.3rc2 | 不支持 |	 
v2.0.2 | v3.3rc2 | 不支持 |	 
v2.0beta0 | v3.3rc0	| v3.1 |	

* Studio 1.x

|CocosStudio版本	| Cocos2d-x v3版本 | Cocos2d-x v2版本 | Cocos2d-js版本 |
| :-------: |:-------:|:------:|:------:|
1.6.0.0	| 3.2 |	2.2.5 | 3.1 |
1.5.0.1	| 3.2 |	2.2.5 |	3.0 RC2 |
1.5.0.0	| 3.0 |	2.2.4 |	3.0 RC2 |
1.4.0.1	| 3.0 |	2.2.3 |	3.0 RC2 |
1.4.0.0	| 3.0 |	2.2.3 |	3.0 RC2 |
1.3.0.1	| 3.0rc1 | 2.2.3 | 3.0 Alpha |
1.3.0.0	| 3.0rc0 | 2.2.3 |	 
1.2.0.1	| 3.0beta |	2.2.2 |	 
1.1.0.0	| | 2.2.1 |
1.0.0.2 	| | 2.2.0 |
1.0.0.1 	|
1.0.0.0	|

####Cocos2d-x 与 NDK 版本对应关系

| Cocos2-x 版本 | NDK 版本 | 备注 |
|:-----:|:-----:|:------|
|v3.0|r8e / r9d / r10c|因为 Android 5.0 某些问题，建议使用r10c，不建议使用r9d，原因可见[此贴](http://discuss.cocos2d-x.org/t/build-android-base-on-ndk-r10c/18543)，下同
|v3.1|r9d / r10c|
|v3.2|r9d / r10c|直接使用r10c会编译失败，必须先根据[此PR](https://github.com/cocos2d/cocos2d-x/pull/7526)修改
|v3.3|r10c|
|v3.4|r10c|
|v3.5|r10c|
|v3.6|r10c|
|v3.7|r10c|
|v3.8|r10c|
|v3.9|r10c|
|v3.10|r10c|

