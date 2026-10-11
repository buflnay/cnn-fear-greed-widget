# CNN 공포·탐욕지수 — 노션용 비공식 위젯

**이 위젯은 CNN이 공식 제공하거나 후원하는 제품이 아닙니다.** CNN 웹사이트의 비공식 데이터 주소를 읽어 개인 사용용 시각화를 표시합니다. CNN의 데이터 제공 방식 변경, 접근 제한 또는 이용 조건에 따라 언제든 실패할 수 있습니다. 공식 지수를 확인하려면 [CNN 원본](https://www.cnn.com/markets/fear-and-greed)을 이용하세요.

## 어떻게 동작하나요?

1. GitHub Actions가 하루 두 차례 CNN 데이터에 접근합니다.
2. 성공하면 `data/latest.json`을 업데이트한 뒤 GitHub Pages에 파일을 배포합니다.
3. `index.html`이 공개된 JSON을 읽고 바늘·수치·전일/1주/1개월/1년 전 수치를 보여줍니다.
4. 실패하면 없는 데이터를 만들지 않고 마지막 정상 데이터를 유지합니다. 72시간 넘게 갱신되지 않으면 지연 경고가 뜹니다.

> **비용/보안:** GitHub Free의 공개 저장소 + GitHub Pages + GitHub Actions 무료 이용 범위를 상정합니다. 저장소와 위젯 주소는 **공개**됩니다. API 키, 계좌, 매매기록, 노션 토큰 같은 개인정보는 절대 넣지 마세요. 공개 위젯에는 오직 지수 데이터만 담습니다.

## 배포 (처음 한 번만)

1. [GitHub](https://github.com)에 로그인해 새 저장소 `cnn-fear-greed-widget`을 **Public**으로 만들고 기본 브랜치를 `main`으로 설정합니다.
2. 이 ZIP을 풀고 파일·폴더를 **그대로** 저장소에 업로드합니다. `.github/workflows/cnn-widget.yml` 폴더 경로가 유지되어야 합니다.
3. 저장소 **Settings → Pages → Build and deployment → Source: GitHub Actions**를 선택합니다.
4. **Actions → Update CNN gauge and deploy site → Run workflow**를 한 번 실행합니다.
5. Actions가 성공하면 Pages 주소는 보통 `https://<깃허브아이디>.github.io/cnn-fear-greed-widget/`입니다.
6. 노션 미국주식 페이지에서 `/임베드`를 선택하고 위 Pages 주소를 입력합니다.

### 실패하면?

- `403`/`418` 또는 스키마 오류: CNN의 비공식 데이터 엔드포인트가 외부 접근을 막거나 변경한 것입니다. 이는 자동으로 해결되지 않습니다.
- 위젯에는 `데이터 연결 대기`가 표시될 수 있습니다. 허위 지수 수치는 넣지 않았습니다.
- GitHub의 예약 실행은 지연될 수 있으며, 공개 저장소에서 활동이 없으면 60일 후 예약 워크플로가 비활성화될 수 있습니다. 정기적으로 Actions 실행 결과를 확인하세요.
- 외부 임베드 사이트가 노션 iframe을 차단하면 주소가 열려도 노션에 표시되지 않을 수 있습니다.

## 구성

- `index.html`: PC/모바일 반응형 CNN 게이지 위젯
- `data/latest.json`: 최신 지수(최초에는 값 없는 자리 표시)
- `scripts/update.py`: 데이터 수집 및 검증
- `.github/workflows/cnn-widget.yml`: 자동 수집·무료 배포
- `.nojekyll`: Pages의 불필요한 Jekyll 변환 방지

본 위젯은 개인용 시장 참고 도구이며 투자 판단을 대신하지 않습니다.
