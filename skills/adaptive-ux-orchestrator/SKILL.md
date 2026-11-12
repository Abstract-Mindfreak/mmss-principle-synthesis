---
name: adaptive-ux-orchestrator
description: "Тонкий оркестратор двух UX-скиллов: mmss-adaptive-ux-laws-application (каталог Laws of UX + гибриды, поиск недостатков) и adaptive-ux-correction-invariant (жёсткие операционные инварианты внимания/плотности/режимов/потока/безопасных мутаций). Координирует последовательность, разрешает конфликты (инварианты имеют приоритет на жёстких ограничениях), поддерживает несколько режимов работы. Не дублирует логику детей; ссылается на них и на общих предков."
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parent: adaptive-universal-invariant-synthesizer
  orchestrates:
    - mmss-adaptive-ux-laws-application
    - adaptive-ux-correction-invariant
  lineage:
    - mmss-principle-synthesis
    - mmss-skill-boundary-combinator
    - adaptive-universal-invariant-synthesizer
  default_output: markdown_or_json
  default_language: ru
  invariant: P1_BOUNDARY_IDENTITY + hard-constraint priority
---

# Adaptive UX Orchestrator

## 1. Purpose

Координировать два специализированных UX-скилла без слияния их логики:

- **mmss-adaptive-ux-laws-application** — последовательное применение Laws of UX и гибридов, сбор observations и change proposals (finding shortcomings — primary goal).
- **adaptive-ux-correction-invariant** — диагностика нарушений жёстких операционных инвариантов (attention budget, density band, regime-from-load, unidirectional flow, distinct state lanes, safe-open, progressive detail, context preserve) и выдача минимальных ранжированных исправлений.

Оркестратор определяет порядок вызовов, передаёт промежуточные результаты, разрешает конфликты и формирует единый итоговый отчёт.

## 2. Ancestry & References

- Дети: `mmss-adaptive-ux-laws-application`, `adaptive-ux-correction-invariant`
- Общие предки: `adaptive-universal-invariant-synthesizer`, `mmss-principle-synthesis`, `mmss-skill-boundary-combinator` (P1)
- Полные формулы, envelope и repair-правила берутся из указанных скиллов; здесь только координация.

## 3. Operating Modes

| Mode ID | Name | Sequence | Когда использовать |
|---------|------|----------|--------------------|
| M1 | laws-first-filter | Laws → Invariant filter | Нужен широкий обзор по классике + отсечение опасных предложений |
| M2 | invariant-first | Invariant diagnosis → Laws enrichment | Сначала жёсткие ограничения, потом дополнительные эвристики |
| M3 | parallel-compare | Оба параллельно → conflict report | Нужно увидеть расхождения явно |
| M4 | rapid-laws-only | Только rapid-capture Laws | Быстрый захват мелочей без жёсткого фильтра |
| M5 | deep-invariant-only | Только Invariant | Когда важны только session-инварианты |

Режим выбирается пользователем или auto-select по сложности входа и приоритету (safety vs breadth).

## 4. Conflict Resolution Rule (жёсткий)

1. Любое предложение из Laws-скилла, которое нарушает один из hard-constraints инвариантного ядра (P_ATTENTION_BUDGET, P_DENSITY_BAND, P_SAFE_OPEN, P_UNIDIRECTIONAL_FLOW, P_DISTINCT_STATE_LANES и т.д.), получает статус `blocked_by_invariant` и не входит в итоговый actionable-список.
2. Предложения, совместимые с инвариантами, сохраняются и помечаются источником (`law`, `invariant`, `both`).
3. Если Laws предлагает усиление того же механизма, что уже есть в инварианте — оставляется более конкретная формулировка.
4. Boundary-identity (value, convention, context) соблюдается при передаче данных между скиллами.

## 5. Working Process

1. **Resolve mode** — явный запрос пользователя или auto-select.
2. **Ingest** — принять описание UI / элементы / скриншот-заметки / приоритеты. Зафиксировать gaps.
3. **Execute children** согласно выбранному режиму:
   - Передавать только необходимые данные (не весь контекст).
   - Сохранять provenance каждого observation/proposal.
4. **Merge & resolve**:
   - Собрать все observations и proposals.
   - Применить Conflict Resolution Rule.
   - Построить итоговую ранжированную карту (сначала blocked, потом actionable, потом nice-to-have).
5. **Emit** единый отчёт:
   - Краткий диагноз (какие инварианты нарушены / какие законы сработали).
   - Actionable corrections (с источником и приоритетом).
   - Blocked proposals (с указанием нарушенного инварианта).
   - Gaps & assumptions.
   - (Deep) цели и критерии успеха, если режим это требует.
6. При необходимости — один дополнительный проход уточнения (не больше).

## 6. Output Contract

По умолчанию — структурированный Markdown или JSON (mmss-envelope при запросе).

Минимальные поля:
- `mode_used`
- `invariant_violations` (список)
- `laws_triggered` (список)
- `actionable_proposals` (ранжированный, с source)
- `blocked_proposals` (с reason)
- `gaps`
- `assumptions`

Реализация изменений — вне скоупа оркестратора (как и у обоих детей).

## 7. Constraints

- Не дублировать и не переписывать логику дочерних скиллов.
- Не ослаблять hard-constraints инвариантного ядра.
- Не фабриковать UI-факты, законы или эффекты.
- Соблюдать epistemic distinctions предков (observation ≠ proven effect, proposal ≠ implemented).
- Minimum sufficiency: оркестратор остаётся тонким.
- Repair budget и provenance-правила наследуются от mmss-principle-synthesis.

## 8. Completion Standard

Проход завершён, когда выбранный режим отработал, конфликты разрешены по правилу раздела 4, gaps зафиксированы и единый отчёт возвращён.  
Дальнейшие проходы — только по явному запросу пользователя.
