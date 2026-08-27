# 룰 근거 자료 (결과보고서용)

DriveLint가 검출하는 각 규칙의 임계값이 Car App Library 실제 소스코드/공식 문서 어디에
근거하는지 정리한 문서. `androidx.car.app` 소스는 `androidx-main` 브랜치 기준.

## 왜 정적 분석이 필요한가 (배경)

`GridTemplate.Builder.build()` 등 템플릿 Builder는 **항목 개수를 자체적으로 검증하지 않는다.**
JVM에서 `.addItem()`을 100번 호출해도 `build()` 자체는 예외를 던지지 않는다 — 개수 제한은
`ConstraintManager#getContentLimit()`을 개발자가 직접 호출해 opt-in으로 확인해야 하며,
그 값도 **실제 차량(호스트)에 바인더로 연결됐을 때만 정확한 값을 받아온다.** 호스트 연결이
없으면 라이브러리에 내장된 보수적 기본값(fallback)으로 대체된다.

즉 컴파일 타임에도, 가벼운 유닛테스트로도 이 위반을 잡을 수 없고, 실제로는 차량/DHU에
연결해 해당 화면을 렌더링해봐야 드러난다. DriveLint는 이 간극을 정적 분석으로 메운다.

- Source: [ConstraintManager.java](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/car/app/app/src/main/java/androidx/car/app/constraints/ConstraintManager.java)
  — `getContentLimit()`이 `mHostDispatcher.dispatchForResult()`로 호스트에 원격 호출하며,
  실패 시 로컬 기본값(리소스)으로 폴백한다는 것을 코드로 확인.
- Source: [GridTemplate.java](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/car/app/app/src/main/java/androidx/car/app/model/GridTemplate.java)
  — `build()`에 항목 "개수"에 대한 검증 로직이 전혀 없음을 코드로 확인 (로딩 상태/아이템
  타입 검사만 존재).

## 규칙별 근거

### GRID-003 — Grid 항목 6개 초과 (하드캡)

라이브러리에 내장된 fallback 기본값(`content_limit_grid`)이 **6**.

```
content_limit_grid = 6
```

주석: "defaults for when the app fails to communicate with the host for the actual limits"
(호스트와 통신 실패 시 쓰는 기본값 — 즉 모든 차량에서 보장되는 안전한 최소 상한).

- Source: [integers.xml](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/car/app/app/src/main/res/values/integers.xml)

### PANE-010 — Pane 정보 행 5개 이상 (하드캡)

같은 리소스 파일의 `content_limit_pane` 값이 **4**.

```
content_limit_pane = 4
```

- Source: [integers.xml](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/car/app/app/src/main/res/values/integers.xml)

### PANE-009 — Pane 정보 행 0개 (MUST)

핸드오프 문서 원 조사 내용(공식 UX 가이드라인, `docs.partner.android.com/drivingux`)에 근거.
라이브러리 소스 자체에는 "0개 금지" 검증이 없으므로, 이건 API 하드캡이 아니라 **디자인
가이드라인 위반(MUST)**으로 분류.

### TAB-013 — Tab 개수 2~4개 범위 (하드캡)

`TabTemplate.Builder.addTab()` API 문서(Javadoc)에 직접 명시:

> "The number of tabs provided in the template should be between 2 and 4, with only one
> tab marked as active."

이건 리소스 fallback이 아니라 API 문서에 고정 범위로 못박혀 있음 — 차량 종류와 무관.

- Source: [TabTemplate.Builder | API reference](https://developer.android.com/reference/kotlin/androidx/car/app/model/TabTemplate.Builder)

## 확인 안 된 것 / 주의

- 위 fallback 기본값들이 "실제 차량 대부분"에서도 그대로 쓰이는지, 아니면 상당수 차량이 이보다
  더 관대한 값을 리턴하는지는 확인 못 함 — 문서/코드상 "안전한 하한선"이라는 것만 확인됨.
- `ConstraintManager` 값은 앱이 실제로 확인 로직을 넣었을 때만 의미가 있고, 지금 DriveLint는
  이 API 호출 여부와 무관하게 소스 텍스트의 `addItem`/`addRow`/`addTab` 호출 횟수만 정적으로
  세므로, 동적으로(반복문 등으로) 개수가 정해지는 코드는 놓칠 수 있음 (README/핸드오프에도
  명시된 스코프 제한).
