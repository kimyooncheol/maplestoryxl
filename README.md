# 메이플스토리 디스코드 봇
![logo](https://ssl.nx.com/s2/game/maplestory/renewal/common/logo.png)
## Project Info
- maple.gg에서 유저 정보 크롤링
- openpyxl을 사용해 크롤링 데이터로 Excel파일 생성
## Change Logs
- 1.0 mapel.gg에서 유저 정보 크롤링후 Excel데이터로 제공하는 기능 추가
- 1.01 크롤링시 서버 부하를 줄이기 위해 코드 최적화
- 1.1 가독성을 위해 셀의 색 차이를 넣음 
- 1.2 함수형 프로그램으로 코드 최적화 
- 1.3 무릉 층수 데이터를 기반으로 갈 수 있는 보스 정보를 추가함
- 1.31 길드 관리자가 조회되지 않는 오류 수정
## How to use
- [Download](https://github.com/kimyooncheol/maplestoryxl/archive/master.zip)
- ![how_1](https://github.com/kimyooncheol/maplestoryxl/blob/master/how_to_use/how_1.PNG?raw=true)<br>
  xl.py를 실행하고 조회할 길드명과 월드명을 입력한다.<br>
- ![how_2](https://github.com/kimyooncheol/maplestoryxl/blob/master/how_to_use/how_2.PNG?raw=true)<br>
  크롤링이 완료되면 xl.py과 동일 폴더에 당일 날짜로 Excel파일이 생성되어 있다.<br>
- ![how_3](https://github.com/kimyooncheol/maplestoryxl/blob/master/how_to_use/how_3.PNG?raw=true)<br>  
  정상적으로 생성된 Excel 
   
## Need to fix
- xl.py 최적화
## Bugs
- 
## Used Packages
```
- requsets: maple.gg에서 유저 정보를 크롤링 하기 위해 사용됨
- bs4: 크롤링 데이터를 파싱하기 위해 사용됨
- numpy: 배열을 다루기 위해 사용됨
- openpyxl: 파싱된 데이터를 Excel화 시키기 위해 사용됨
- Datetime: Excel이름에 날짜를 넣기 위해 사용됨
```
## Authors
- 김윤철
## License
This project is licensed under the MIT License

