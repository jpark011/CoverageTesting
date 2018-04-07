# CoverageTesting
Automated testing tool to test various coverage (node, branch, path, ...)

### Python
__Test Runner__ is used for automated testing.

### Types of Coverages:
- __Node Coverage:__ each statement is a single node.
- __Branch Coverage:__ each edge between statements is a branch.
- __Path Coverage:__ full sequence from start to end.

### Types of Data Usage:
- __def:__ definition of a variable.
- __use:__ usage of a variable.
- __DU-pair:__ def & use of a variable.
- __Last-def First-use:__ in an interface all we care about is last def of caller and first use of callee.
