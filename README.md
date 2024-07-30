![Testing Status](https://github.com/gaspardruan/YYMH/actions/workflows/python-app.yml/badge.svg)

This is a python script to download YYMH comic books. The available links are as followed:
- [manhuadizhi.com](https://manhuadizhi.com)
- [yymh.app](https://yymh.app)
- [yymh.cn](https://yymh.cn)

# Usage

Go to the desired comic book page and click the url, you will get the comic id. For example:
```
https://yymh.app/home/book/index/id/361
```
Then, simply run the script:
```
python yymh.py [id] [name]
```
[id] is what you've got above. [name] is decided on you.

# Others

`.cbz` format is actually same as `.zip`, which means you can change the suffix to `.zip` and double click to get
the image list. Then, you can deal with it as you want.
