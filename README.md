# pep8
파이썬 컨벤션(pep8) 검사하는 스크립트


### 설치
```
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

### 실행
```
(venv) $ python run.py
./run.py : pass
```

### 예외 폴더 설정
```
(venv) $ python run.py --ignore venv migrations
./run.py : pass
```
