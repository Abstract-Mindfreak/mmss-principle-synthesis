# Requirement-based module: required-field validator

Design one small module for validating a required field in a record.

## Explicit requirements

1. The input is a record and the configured field name.
2. The result states whether the field is present.
3. A missing field produces a finding that identifies the field name.
4. Do not add type, format, or value constraints unless separately required.

Treat these requirements as the design basis. No research source is needed or should be invented. Identify any additional assumptions explicitly.
