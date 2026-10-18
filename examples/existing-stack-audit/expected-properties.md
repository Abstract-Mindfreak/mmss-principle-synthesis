# Expected properties

The JSON syntax is valid. The following architectural defects are intentional:

- The `validate` identifier is duplicated across independent module definitions.
- The dependency `missing-normalizer` does not resolve to a declared module.

An audit should report both findings and avoid calling the fixture a valid architecture. These are expected audit criteria, not results of an executed model evaluation.
