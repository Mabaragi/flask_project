# Flask
export FLASK_APP=pybo
export FLASK_DEBUG=true


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
   ```python
   from pymongo import MongoClient

   my_mongo_uri = os.getenv('MY_MONGO_URI')
   client = MongoClient(my_mongo_uri)
   # app인스턴스의 속성으로 db를 저장, 다른 모듈에서 current_app.db로 접근
   app.db = client.temp

   ```
3. 다른 곳에서 mongo를 참조하려면, `current_app ` 을 임포트해서 사용
    - `current_app.db` 로 접근하여 mongo db 사용

**uri 보안**
- python-dotenv 패키지 활용
- 루트 디렉토리에 `.env` 파일 생성하고 URI를 포함시키면됨. .gitignore에 작성.
  
**Flask Shell**
`flask shell`

### 문서 지향적 데이터 모델링
- MongoDB는 BSON 형식을 사용하며 document 형태로 저장. 각 문서는 키-값 쌍을 가지고, 다른 문서를 임베딩 할 수 있음.
- MongoDB는 스키마가 고정되어 있지 않음(Flexible Schema)
**임베딩 vs 참조**
- 임베딩 : join이 필요없어 조회에서 유리하지만, 중복 데이터 관리가 어려워짐
- 참조 : RDBMS의 외래키와 유사한 방식으로 작동. 데이터 검색에서 불리함.

**애플리케이션 수준에서의 데이터 모델링**
- MongoDB는 스키마가 없지만, 애플리케이션 수준에서 데이터 구조를 하는게 유용할 수 있다.
- 일반적으로 NoSQL 데이터베이스를 사용하더라도 애플리케이션 수준에서 데이터구조를 정의하는 경우가 많다. 그 이유는 다음과 같다.
  - 데이터 무결성, 유효성 검증
  - 가독성, 유지보수
  - 비즈니스 로직
  - 데이터 접근 방법 표준화, 쿼리 최적화