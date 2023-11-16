# Flask

***WSGI Application***
- Web Server Gateway Interface 애플리케이션
- 웹서버와 파이썬 웹 애플리케이션(프레임워크) 사이의 표준 인터페이스

***Flask Run***

- 플라스크 웹 서버 실행 명령어
- 기본적으로 app.py 파일을 기본 애플리케이션으로 인식함.

***순환참조 문제***
- app 객체를 전역으로 사용하면 순환참조 문제가 발생함
- 해결책으로 Application Factory 패턴 사용
  - create_app 함수를 정의해서, 함수만을 임포트 하고 앱 객체를 생성하여 사용


***라우팅 함수***
- `@app.route('/')` 애노테이션으로, URL과 매핑하는 함수를 라우팅 함수라고 한다.
  
***블루프린트(Blueprint)***
- 라우팅 함수를 체계적으로 관리하기 위해 사용.
- URL과 함수의 매핑을 관리
- `bp = Blueprint('main', __name__, url_prefix='/')`
  - `main` : alias,  `__name__` : 파일명, `url_prefix` : 기본적으로 붙일 url 접두어
  - 애노테이션으로 `@bp.route('/')` 사용하면 됨.

# MongoDB
1. Flask-PyMongo 라이브러리 설치
2. `__init__.py` 파일의 `create_app` 함수에 Mongo DB 설정
   ```
   
   ```
3. 다른 곳에서 mongo를 참조하려면, `current_app ` 을 임포트해서 사용

**uri 보안**
- python-dotenv 패키지 활용
- 루트 디렉토리에 `.env` 파일 생성하고 URI를 포함시키면됨. .gitignore에 작성.