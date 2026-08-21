# DriveLint

> 2026 공개SW 개발자대회 제출 | 팀명: 초보운전

Android Auto 앱(Car App Library 기반)의 Kotlin 소스코드를 정적 분석해 운전자 주의분산 방지 가이드라인(Design for Driving)의 MUST/하드캡 위반을 자동으로 검출하는 CLI 도구입니다.

소스코드에서 `XxxTemplate.Builder()` 호출 패턴을 텍스트로 분석하기 때문에 앱을 빌드하거나 실행할 필요가 없습니다.

## 설치

```bash
git clone <이 리포지토리>
cd drive-lint
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 사용법

프로젝트 검사

```bash
drivelint check ./검사할프로젝트경로
```

특정 파일 검사

```bash
drivelint check ./MyScreen.kt
```

위반이 하나도 없으면 종료 코드 0, 하나라도 있으면 1을 반환합니다
(CI 파이프라인에 그대로 연결 가능).

## 현재 지원하는 규칙

| 규칙 ID | 템플릿 | 내용 | 종류 |
|---|---|---|---|
| GRID-003 | Grid | 항목이 6개 초과 | 하드캡 |
| PANE-009 | Pane | 정보 행이 0개 | MUST |
| PANE-010 | Pane | 정보 행이 5개 이상 (최대 4) | 하드캡 |
| TAB-013 | Tab | 탭 개수가 2~4개 범위 밖 | 하드캡 |

## 개발

```bash
python3 -m unittest discover -s tests -v
```
