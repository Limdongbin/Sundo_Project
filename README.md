## [프로젝트 개요]

- 프로젝트 명 : 해역 이용 영향평가 시스템

- 개발 인원 : 8명 (조경민, 임동빈, 이건화, 이정훈, 김시아, 정주희, 김명현, 이상미)

- 프로젝트 소개 : 해양환경과 해양생태계의 현황, 그리고 면허어장에 대한 정보를 시각적인 데이터를 활용하여 직관적으로 전달할 지리정보 웹사이트 개발 프로젝트

- 주요 기능 : 파이썬 크롤링을 활용한 실시간 관측소 정보 수집, 지도 및 레이어 표출, 각 레이어에 맞는 데이터 표출 등

- 개발 환경: Java(JDK 1.8), HTML/CSS/JavaScript, eGovFrame(eclipse) 4.1, QGIS, PostgreSQL, DBeaver, ibatis, Apatch Tomcat 9.0 등

- 프로젝트 구현 보고서 (PPT) : https://docs.google.com/presentation/d/1gdB1EgcZTTpz4AcfE-Qakk7LdlXfqpRG/edit?usp=drive_link&ouid=115501983965331557726&rtpof=true&sd=true

- 프로젝트 구현 동영상 : https://drive.google.com/file/d/1x1Pfi4bodiZmsClEFr0P3bBndqbhbkdj/view?usp=drive_link

## [내가 구현한 파트]

### 1. 레이어 발행

- QGIS를 이용해 .shp 또는 .csv파일의 데이터를 레이어로 표출.
- 표출한 레이어를 PostGreSQL 데이터베이스와 연결.
- GeoServer에서 레이어 발행 및 스타일 지정.
- 해당 폴리곤 또는 포인트에 데이터 값 출력.


### 2. 클러스터 기능 구현
클러스터? 밀집되어 있는 데이터 값. 지도의 확대/축소에 따라 표출되는 데이터의 밀집도가 변경된다.

- 해당하는 레이어의 벡터 소스를 생성.
- 클러스터 거리 설정.
- 클러스터의 스타일을 지정해준 뒤 클러스터 소스 생성.
- 클러스터 레이어 생성 및 지도 표출.
- 클러스터 선택 및 지도 이동 시 클러스터 변경.

### 3. 레이어 리스트 목록 (좌측 레이어 목록)

- 테이블 설계 시 category를 계층적으로 설계하여 SQL문을 활용해서 DB에서 직접 리스트를 출력.
- DB / 선택된 레이어 버튼 클릭 시 전체 레이어와 체크박스가 선택된 레이어 목록이 토글되어 표출된다.
- 초기화 버튼 클릭 시 체크박스 해제 및 표출 레이어들이 모두 초기화된다.
