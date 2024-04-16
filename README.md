# 声明
只是发现了一个小bug（但是学校好像并没有想要修复的样子）

# 原理
二维码本质是网址，观察erke的链接可以发现
- [ ] 起始界面：http://erke.gdut.edu.cn/public/index.php/mobile/activity-detail?id=6558
- [ ] 签到界面：http://erke.gdut.edu.cn/public/index.php/mobile/activity-sign-result?id=6558&type=in&ts=1786329300000
- [ ] 签退界面：http://erke.gdut.edu.cn/public/index.php/mobile/activity-sign-result?id=6558&type=out&ts=1786329300000
- 其中in和out分别代表签到和签退，ts是识别码，其实还有一种形式是将ts换成token

1713274015472其实是2024-04-16 21:26:55北京时间（ms）的时间戳——是不是跟上面ts后面的数字很像，所以结论就是ts后面的数字就是签到和签退过期的时间，token后面的和ts类似。
## 一次使用
token生成的链接只能被唯一识别并在服务端产生一对一标记
## 多次使用
利用ts来实现多人扫码

已经打包成了exe文件，可在windows下运行，在目录处生成二维码，源文件是Qrcode.py
