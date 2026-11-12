---
name: adaptive-ux-correction-invariant
description: "Практическая диагностика и минимальные UX-исправления на основе деформационно-устойчивых инвариантов внимания, плотности, режимов, однонаправленного потока, разделения состояний и безопасных мутаций. Компактный скилл; полные формулы, envelope и repair-правила наследуются от предков (adaptive-universal-invariant-synthesizer, mmss-principle-synthesis, mmss-skill-boundary-combinator, data-to-skill, session-to-skill). Используй для исправления интерфейсов, проверки соблюдения UX best-practice mechanisms и выдачи ранжированных минимальных правок."
metadata:
  version: "0.1.0"
  maturity: test_candidate
  parent: adaptive-universal-invariant-synthesizer
  lineage:
    - mmss-principle-synthesis
    - mmss-skill-boundary-combinator
    - data-to-skill
    - session-to-skill
    - adaptive-universal-invariant-synthesizer
  default_output: markdown_or_json
  default_language: ru
  invariant: P_UNIVERSAL_CONSTRUCTIVE_METHOD + P1_BOUNDARY_IDENTITY
---

# Adaptive UX Correction Invariant

## 1. Purpose

Практический инструмент для диагностики нарушений и выдачи минимальных UX-исправлений.  
Основан исключительно на деформационно-устойчивых инвариантах, извлечённых из сессии (Attention-Layout, Regime-Scaling, MIMO-Configurator, Research-Interface).  

Скилл намеренно компактен: полные формулы операторов, JSON-envelope, repair-budget и boundary-identity берутся из предков по ссылке. Не дублирует их.

## 2. Ancestry (обязательные ссылки)

- **adaptive-universal-invariant-synthesizer** — robust kernel, layered projection, information-loss accounting, variational minimality.
- **mmss-principle-synthesis** — provenance, epistemic distinctions, minimum sufficiency, ≤2 repair passes, default envelope.
- **mmss-skill-boundary-combinator** — P1 boundary-identity `(value, convention, context)`.
- **data-to-skill / session-to-skill** — selective P extraction pipeline.

При любом расширении или repair сначала применяй правила предков.

## 3. Robust Kernel (деформационно-устойчивое ядро)

| ID | Statement |
|----|-----------|
| P_ATTENTION_BUDGET | Жёсткие бюджеты внимания и когнитивной ёмкости; распределение максимизирует полезность при соблюдении ограничений. |
| P_DENSITY_BAND | Региональная информационная плотность удерживается внутри допустимого интервала; выход вызывает перераспределение или сжатие. |
| P_REGIME_FROM_LOAD | Дискретный режим интерфейса определяется безразмерным отношением нагрузки и масштабным фактором; переходы ограничены по скорости. |
| P_UNIDIRECTIONAL_FLOW | Действия → чистое состояние → чистые проекции → единственная точка применения побочных эффектов. Рендер не порождает повторных мутаций. |
| P_DISTINCT_STATE_LANES | Состояние исполнения, завершённость проверок, автоматический вывод и решение пользователя — четыре независимые дорожки. |
| P_SAFE_OPEN | Открытие и preview никогда не запускают вычисления или мутации. Любая мутация требует явного триггера и подтверждения. |
| P_PROGRESSIVE_DETAIL | Обычный режим компактен; расширенный раскрывает техническую плотность. Ошибки никогда не скрываются молча. |
| P_CONTEXT_PRESERVE | Контекст (версия, запрос, фильтры, выбранный объект) восстанавливается при любом возврате. |
| P_SNAPSHOT_AUTONOMY | Отчёты и экспорты потребляют только чистый неизменяемый снимок. |
| P_BOUNDARY_IDENTITY | Каждое пересечение границы представления переносит тройку (value, convention, context). |

## 4. Practical Operators (ссылки на предков)

IMPORTANCE, SCALE, DENSITY, ATTENTION, COGNITIVE_LOAD, REGIME_CLASSIFIER, RESOURCE_ALLOCATOR, DECOUPLE_CHANNELS, SNAPSHOT_EXPORT, FEEDBACK_MODULATION.

Полные формулы и ограничения — в UNIVERSAL_ATTENTION_LAYOUT_INVARIANT и UNIVERSAL_REGIME_SCALING_INVARIANT (через adaptive-universal-invariant-synthesizer).

## 5. Working Process

1. Принять текущее состояние UI / описание проблемы / макет как S. Зафиксировать boundary-identity.
2. Извлечь и сопоставить с операторами robust kernel (selective P extraction по правилам data-to-skill).
3. Диагностировать нарушения:
   - переполнение внимания / когнитивной ёмкости,
   - выход плотности из полосы,
   - несоответствие режима нагрузке,
   - смешение pure/impure,
   - схлопывание дорожек состояний,
   - небезопасное открытие,
   - потеря контекста,
   - отсутствие progressive detail.
4. Предложить минимальные ранжированные исправления (перераспределение долей, принудительный более низкий режим, разделение каналов, явные подтверждения, контракт восстановления контекста).
5. Выдать диагноз + список исправлений. По явному запросу — материализовать патч или локальный инвариант.
6. Проверить соблюдение жёстких ограничений; зафиксировать assumptions и information-loss.

## 6. Output Contract

- По умолчанию: Markdown-диагноз + ранжированные исправления (или JSON по mmss-envelope, если запрошен).
- Материализация нового SKILL.md — только после явного запроса и завершения repair-циклов.
- Коммерческая упаковка — только через adaptive-commercial-specializer.

## 7. Constraints

- Не вводить UX-законы, отсутствующие в session-инвариантах.
- Не дублировать полные формулы и envelope предков.
- Repair budget наследуется (уже использован 2 прохода при создании).
- Не фабриковать количественные targets или эмпирические baselines, которых нет в сессии.
- Color/contrast и light-field операторы намеренно вынесены за пределы robust kernel (presentation-specific); добавляются только по отдельному запросу.

## 8. Completion Standard

Завершать, когда выдан практический диагноз + минимальный набор исправлений или зафиксирован точный gap.  
Unknowns, partial results и failures остаются видимыми.  
Скилл остаётся usable без обращения к исходным доменным JSON сессии.
